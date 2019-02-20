from django import forms
from .models import Story,Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('story_title','story_body')
        widgets = {
            'story_title': forms.TextInput( attrs={'class': 'form-control ', 'type':"text",'id':"fname",'placeholder':"All great stories have great names like 'Lorem Ipsum'"}),
            'story_body': forms.Textarea( attrs={'class': 'form-control ','id':"message", 'cols':'50', 'rows':'25' , 'placeholder':'Once upon a time ...'}),
            }


class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ('comment_body',)
       widgets = {
            'comment_body': forms.Textarea( attrs={'class': 'form-control ','id':"message",  'cols':'25','rows':'2' , 'placeholder':'Cool Story Bruh  ...'}),
            }