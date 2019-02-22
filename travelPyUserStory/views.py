from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoryForm, CommentForm   
from .models import Story,Comment
from travelPyLands.models import City
from pprint  import pprint
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required




# Create your views here.


def all(request,city_id):
    print(city_id)
    city = City.objects.filter(id = city_id).first()
    print()
    try:
        context = {'stories':Story.objects.filter(city_id = city_id).order_by('-id'),
        'city_name': city.city_name,
        'city_id':city_id
        }
        return render(request, 'all.html',context)
    except Story.DoesNotExist:
        raise Http404



def read_story(request, story_id):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = Comment.objects.create(
                    comment_body = request.POST.get("comment_body"),
                    story_id = story_id,
                    user = request.user
                )
            except Exception as e:
                raise Http404
            return HttpResponseRedirect('/stories/'+str(story_id)+'/')
    
    try:
        story = Story.objects.get(id = story_id)
        if story.user_id == request.user.id: 
            is_author =  True
        else:
            is_author = False
        # print("USERNAME "+request.user.username)
        context = {
        'story': Story.objects.get(id = story_id),
        'comments': Comment.objects.filter(story_id = story_id),
        'form':form,
        'username':request.user.username,
        'is_author':is_author,
        }
        return render(request, 'story.html',context)
    except Story.DoesNotExist:
        raise Http404

  


@login_required(login_url='/user/login/')
def new_story(request, city_id): 
    form = StoryForm()
    if request.method =="POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = Story.objects.create(
                story_title = request.POST.get("story_title"),
                story_body  = request.POST.get('story_body'),
                user_id = request.user.id,
                city_id     = city_id     # city_id ->
                )
            return HttpResponseRedirect('/stories/'+str(story.id)+'/')
    return render(request,'new.html', {'form':form})

    
@login_required(login_url='/user/login/')
def edit_story(request, story_id):
    story = Story.objects.get(id = story_id)
    if story.user_id == request.user.id: 
            is_author =  True
    else:
        is_author = False
    
    if not is_author:
        return HttpResponseRedirect(request,"401 Unauthorized Access", status = 401)
    
    if request.method == "POST":
        form = StoryForm(request.POST, instance = story)
        if form.is_valid():
            try:
                story = Story.objects.get(id =story_id)
                story.story_title = request.POST.get("story_title"),
                story.story_body  = request.POST.get("story_body"),
                story.story_title = story.story_title[0] 
                story.story_body  = story.story_body [0]
                story.save()
                return HttpResponseRedirect('/stories/'+story_id+'/')
            except Story.DoesNotExist:
                raise Http404
    else:
        form = StoryForm(instance = story)
    
    return render(request,'edit.html', {'form':form, 'is_author':is_author, 'username':request.user.username})