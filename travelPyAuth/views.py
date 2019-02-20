from django.shortcuts import render
from django.contrib.auth import( 
	authenticate,
	get_user_model,
	login,
	logout
	

)
from .forms import EditForm
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponse, HttpResponseRedirect



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
		return HttpResponseRedirect('/auth/home/')
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
		
		login(request,user)
		request.session['user_id'] = user.id
		print("ID ", request.session['user_id'])
		x=user.id
		y=user.username
		print(x,y)
		userData_dict={'id':x,
		'username':y,
		"aaa":"aaaaaaaaaaaaa"}
		print(userData_dict)
		return HttpResponseRedirect('/auth/home/')
		

		#if next:
		#	return redirect(next)
	#	return redirect('/')
	context={
		'form':form,
}
	return render(request,"travelPyAuth/signup.html",context)

def home_view(request):
	userID = request.session['user_id']
	userData = User.objects.filter(id = userID).first()
	userData_dict={'userdata':userData,
					'ay7aga':"aaaaaaa"}
	print(userData.username)
	print(userData.id)
	return render(request,"travelPyAuth/about.html",context=userData_dict)


def edit_profile(request):
    # instance = get_object_or_404(, id=story_id) 
	
	my_user= User.objects.get(id = request.session['user_id'])
	if request.method == "POST":
		form = EditForm(request.POST, instance = my_user)
		if form.is_valid():
			my_user=User.objects.get(id= request.session['user_id'])
			my_user.email=request.POST.get('email')
			my_user.save()
			return HttpResponseRedirect('/auth/home/')

	context={}
	return render(request,"travelPyAuth/signup.html",context)


	

