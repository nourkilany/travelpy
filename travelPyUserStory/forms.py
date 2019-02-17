from django import forms
from .models import Story,Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('story_title','story_body','user_id','city')
        widgets = {
            'story_title': forms.TextInput( attrs={'class': 'form-control ', 'type':"text",'id':"fname",'placeholder':"All great stories have great names like 'baluka bika bako'"}),
            'story_body': forms.Textarea( attrs={'class': 'form-control ','id':"message", 'cols':'50', 'rows':'25' , 'placeholder':'Once upon a time ...'}),
            'city_id': forms.TextInput( attrs={'class': 'form-control ','id':"message",  'value':'99'}),
            'user_id': forms.TextInput( attrs={'class': 'form-control ','id':"message", 'value':'99'}),
            }


class CommentForm(forms.ModelForm):
    pass