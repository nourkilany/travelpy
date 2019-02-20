from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoryForm, CommentForm   
from .models import Story,Comment
from pprint  import pprint
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.


def all(request):
    try:
        context = {'stories':Story.objects.filter(city_id = 1)}
        return render(request, 'all.html',context)
    except Story.DoesNotExist:
        raise Http404



def read_story(request, story_id):
    print("hit")
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                comment_body = request.POST.get("comment_body"),
                story_id = story_id,
                user = request.user
            )
            return HttpResponseRedirect('/stories/'+str(story_id)+'/')
    
    try:
        context = {
        'story': Story.objects.get(id = story_id),
        'comments': Comment.objects.filter(story_id = story_id),
        'form':form,
        'username':User.username
        }
        return render(request, 'story.html',context)
    except Story.DoesNotExist:
        raise Http404

  



def new_story(request):
<<<<<<< HEAD
    if  request.user.is_authenticated():
        print ("GOT IN ")
        form = StoryForm()
        if request.method =="POST":
            form = StoryForm(request.POST)
            if form.is_valid():
                story = Story.objects.create(
                    story_title = request.POST.get("story_title"),
                    story_body  = request.POST.get('story_body'),
                    user_id = request.user.id,
                    city_id     = 100     # city_id ->
                    )
                return HttpResponseRedirect('/stories/'+str(story.id)+'/')
        return render(request,'new.html', {'form':form})
    else:
        return HttpResponseRedirect('/auth/signup/')
=======
    form = StoryForm()
    print(request.session['user_id'])
    if request.method =="POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = Story.objects.create(
                story_title = request.POST.get("story_title"),
                story_body  = request.POST.get('story_body'),
                user_id     = request.session['user_id'],   # user_id ->
                city_id     = 100     # city_id ->
                )
            return HttpResponseRedirect('/stories/'+str(story.id)+'/')
    return render(request,'new.html', {'form':form})
>>>>>>> b964f6d7cc7e35793402970a4a741bc2e114463b
    

def edit_story(request, story_id):
    # instance = get_object_or_404(, id=story_id) 
    story = Story.objects.get(id = story_id)
    if request.method == "POST":
        form = StoryForm(request.POST, instance = story)
        if form.is_valid():
            try:
                story = Story.objects.get(id =story_id)
                story.story_title = request.POST.get("story_title"),
                story.story_body  = request.POST.get("story_body"),
            # Solving weird format in story_title and story_body
                story.story_title = story.story_title[0] 
                stsory.story_body  = story.story_body [0]
                story.save()
                return HttpResponseRedirect('/stories/'+story_id+'/')
            except Story.DoesNotExist:
                raise Http404
    else:
        form = StoryForm(instance = story)
    return render(request,'edit.html', {'form':form})