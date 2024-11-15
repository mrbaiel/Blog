from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    toemail = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)