from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StoryForm, CommentForm   

# Create your views here.


def all(request):
    return render(request, 'all.html',)



def story(request, id):
    return render(request, 'story.html',)


def new(request):
    print('Page required')
    form = StoryForm()
    if request.method =="POST":
        print('POST request arrived')
        print(form)
        form = StoryForm(request.POST)
        if form.is_valid():
            print('valid')

            form.save()
            print('saved')
            return HttpResponseRedirect('/story/')
        print (form.is_valid())

    return render(request,'newstory.html', {'form':form})
