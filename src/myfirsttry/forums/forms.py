from django import forms
from .models import ForumPost


# class ForumPostCreateForm(forms.Form):
#     topic = forms.CharField()
#     category = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)


class ForumPostModelForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic','category','message']
    
