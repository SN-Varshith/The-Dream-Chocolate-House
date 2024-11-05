from django import forms
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion

class SeasonalFlavorForm(forms.ModelForm):
    class Meta:
        model = SeasonalFlavor
        fields = ['name', 'description', 'availability_start', 'availability_end', 'season','price','is_available']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'quantity_in_stock', 'unit']

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['customer_name', 'flavor_suggestion', 'allergy_concerns']
