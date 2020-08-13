from django import forms

class  CommentForm(forms.Form):
    content_type = forms.IntegerField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(widget = forms.Textarea(attrs={'rows':4 }), label='')
    parent_id = forms.IntegerField(widget = forms.HiddenInput, required = False)

