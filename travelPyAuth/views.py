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
from django.contrib import auth



def login_view(request):
	#next=request.GET.get('next')
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)

		request.session['user_id'] = user.id
		print("ID ", request.session['user_id'])
		x=user.id
		y=user.username
		print(x,y)
		#st=user.objects.get(id=int(user.id))
		#context={'user':st}
		#return HttpResponse("Hello")
		userData_dict={'id':x,
		'username':y,
		"aaa":"aaaaaaaaaaaaa"}
		print(userData_dict)
		return HttpResponseRedirect('/user/profile/')
	#	if next:
	#		return redirect(next)
	#	return redirect('/')
	context={
		'form':form,
}	
		
	
	return render(request,"travelPyAuth/login.html",context)

def register_view(request):
	#next=request.GET.get('next')
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
		# print("ID ", request.session['user_id'])
		# x=user.id
		# y=user.username
		# print(x,y)
		# userData_dict={'id':x,
		# 'username':y,
		# "aaa":"aaaaaaaaaaaaa"}
		# print(userData_dict)
		return HttpResponseRedirect('/user/profile')
		

		#if next:
		#	return redirect(next)
	#	return redirect('/')
	context={
		'form':form,
}
	return render(request,"travelPyAuth/signup.html",context)


@login_required(login_url='/user/login/')
def profile_view(request):
	# if request.user.is_authenticated():
	userID = request.session['user_id']
	userData = User.objects.filter(id = userID).first()
	stories = Story.objects.filter(user_id = userID)
	# hotel_resv = Story.objects.filter(user_id = userID)
	car_rents = CarRental.objects.filter(user_id= userID)
	userData_dict={'userdata':userData,
					'user_stories':stories,
					'car_rents':car_rents
					}
	print(userData.username)
	print(userData.id)
	return render(request,"travelPyAuth/profile.html",context=userData_dict)
	# else:
		# return HttpResponseRedirect('/user/login')


def edit_profile(request):
    # instance = get_object_or_404(, id=story_id) 
	
	my_user= User.objects.get(id = request.session['user_id'])
	if request.method == "POST":
		form = EditForm(request.POST, instance = my_user)
		if form.is_valid():
			my_user=User.objects.get(id= request.session['user_id'])
			my_user.email=request.POST.get('email')
			my_user.save()
			return HttpResponseRedirect('/user/profile/')

	context={}
	return render(request,"travelPyAuth/edit.html",context)


	

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login')