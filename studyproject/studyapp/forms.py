from django import forms
from .models import Community, Comment

class CommuForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']