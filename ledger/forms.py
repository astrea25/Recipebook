from django import forms

from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        exclude = ['recipe']
