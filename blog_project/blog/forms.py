from django import forms
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
    # required=False :-its used for comments is not mandetory(that ia optional)*********you can provide or leave empty


from blog.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        # only three field are required
        fields=('name','email','body')