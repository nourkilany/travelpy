from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoryForm, CommentForm   
from .models import Story

# Create your views here.


def all(request):
    return render(request, 'all.html',)


def read_story(request, story_id):
    context = {'story': Story.objects.get(id = story_id)}
    return render(request, 'story.html',context)


def new_story(request):
    form = StoryForm()
    if request.method =="POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            body = request.POST.get('story_body')
            body = body.replace('\n', '<br />')
            story = Story.objects.create(
                story_title = request.POST.get("story_title"),
                story_body  = request.POST.get("story_body"),
                user_id     = 99,   # user_id ->
                city_id     = 2     # city_id ->
                )
            return HttpResponseRedirect('/story/')
    return render(request,'newstory.html', {'form':form})
    


def edit_story(request, story_id):
    story = Story.objects.get(id = story_id)
    if request.method == "POST":
        form = StoryForm(request.POST, instance = story)
        if form.is_valid():
            story = Story.objects.get(id =story_id)
            story.story_title = request.POST.get("story_title"),
            story.story_body  = request.POST.get("story_body"),
            story.save()
            return HttpResponseRedirect('/story/'+story_id+'/')
    else:
        form = StoryForm(instance = story)
    return render(request,'newstory.html', {'form':form})