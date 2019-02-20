from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoryForm, CommentForm   
from .models import Story
from pprint  import pprint
from django.contrib.auth.models import User

# Create your views here.


def all(request):
    context = {'stories':Story.objects.filter(city_id = 1)}
    for story in context['stories']:
        pprint(story.id)
        
    return render(request, 'all.html',context)


def read_story(request, story_id):
    context = {'story': Story.objects.get(id = story_id)}
    return render(request, 'story.html',context)



def new_story(request):
    form = StoryForm()
    if request.method =="POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = Story.objects.create(
                story_title = request.POST.get("story_title"),
                story_body  = request.POST.get('story_body'),
                user_id     = 10,   # user_id ->
                city_id     = 1     # city_id ->
                )
            return HttpResponseRedirect('/stories/'+str(story.id)+'/')
    return render(request,'new.html', {'form':form})
    


def edit_story(request, story_id):
    # instance = get_object_or_404(, id=story_id) 
    story = Story.objects.get(id = story_id)
    if request.method == "POST":
        form = StoryForm(request.POST, instance = story)
        if form.is_valid():
            story = Story.objects.get(id =story_id)
            story.story_title = request.POST.get("story_title"),
            story.story_body  = request.POST.get("story_body"),

            # Solving weird format in story_title and story_body
            story.story_title = story.story_title[0] 
            story.story_body  = story.story_body [0]
            story.save()
            return HttpResponseRedirect('/stories/'+story_id+'/')
    else:
        form = StoryForm(instance = story)
    return render(request,'edit.html', {'form':form})