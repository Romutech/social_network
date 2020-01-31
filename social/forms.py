from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = "Ajouter un commentaire"
    class Meta:
        model = Comment
        fields = ('content',)
       