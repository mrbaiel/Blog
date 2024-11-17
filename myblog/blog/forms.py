from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    toemail = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'body',
            'name',
        ]