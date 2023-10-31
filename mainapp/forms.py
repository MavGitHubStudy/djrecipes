from django import forms
from .models import *


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    cooking_time = forms.PositiveSmallIntegerField()
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
