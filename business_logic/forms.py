from django import forms
from authentication.models import FoodiUser

class UserPrefrencesForm(forms.Form):
    foodPrefrence = forms.MultipleChoiceField(choices=[('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Japanese', 'Japanese')], widget=forms.CheckboxSelectMultiple)
    restricstions = forms.ChoiceField(choices=[('vegetarian', 'Vegetarian'), ('vegan', 'Vegan')], widget=forms.RadioSelect)
    city = forms.ChoiceField(choices=[('new-york', 'New York'), ('los-angeles', 'Los Angeles'), ('chicago', 'Chicago')], widget=forms.Select)