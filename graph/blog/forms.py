from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Post

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
  

class SupprForm(forms.Form):
	suppr = forms.CharField(max_length = 255)


class NouveauContactForm(forms.Form):
    description = forms.CharField()
    photo = forms.ImageField()
