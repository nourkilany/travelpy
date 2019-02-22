from django.shortcuts import render
from django.contrib.auth import( 
	authenticate,
	get_user_model,
	login,
	logout
	

)
from .forms import EditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from travelPyUserStory.models import Story
from travelPyCarRent.models import CarRental
from travelPyHotelBooking.models import HotelReservation
from django.contrib import auth



def login_view(request):
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)

		request.session['user_id'] = user.id
		return HttpResponseRedirect('/user/profile/')
	context={
		'form':form,
}	
		
	
	return render(request,"travelPyAuth/login.html",context)

def register_view(request):
	form=UserRegisterForm(request.POST or None)
	print("hit")

	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		print('saved')
		login(request,user)
		request.session['user_id'] = user.id
		return HttpResponseRedirect('/user/profile')
		

	context={
		'form':form,
}
	return render(request,"travelPyAuth/signup.html",context)


@login_required(login_url='/user/login/')
def profile_view(request):
	userID = request.session['user_id']
	userData = User.objects.filter(id = userID).first()
	
	stories = Story.objects.filter(user_id = userID)
	hotel_resv = HotelReservation.objects.filter(user_id = userID)
	car_rents = CarRental.objects.filter(user_id= userID)
	userData_dict={'userdata':userData,
					'user_stories':stories,
					'car_rents':car_rents,
					'hotel_resv':hotel_resv
					}
	return render(request,"travelPyAuth/profile.html",context=userData_dict)


def edit_profile(request):
	
	my_user= User.objects.get(id = request.session['user_id'])
	if request.method == "POST":
		form = EditForm(request.POST, instance = my_user)
		if form.is_valid():
			my_user=User.objects.get(id= request.session['user_id'])
			my_user.first_name=request.POST.get('first_name')
			my_user.last_name=request.POST.get('last_name')
			my_user.email=request.POST.get('email')
			my_user.save()
			return HttpResponseRedirect('/user/profile/')

	context={}
	return render(request,"travelPyAuth/edit.html",context)


	

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login')