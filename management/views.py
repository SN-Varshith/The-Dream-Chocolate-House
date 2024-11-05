from django.shortcuts import render, redirect
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion
from .forms import SeasonalFlavorForm, IngredientForm, CustomerSuggestionForm

def home(request):
    return render(request, 'management/home.html')

# Seasonal 
def seasonal_flavor_list(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'management/seasonal_flavor_list.html', {'flavors': flavors})

def add_seasonal_flavor(request):
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            print("Flavor added successfully!")
            return redirect('seasonal_flavor_list')
        else:
            print(form.errors)
    else:
        form = SeasonalFlavorForm()
    return render(request, 'management/add_seasonal_flavor.html', {'form': form})

# Ingredient
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'management/ingredient_list.html', {'ingredients': ingredients})

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'management/add_ingredient.html', {'form': form})

# Customer Suggestion 
def customer_suggestion_list(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'management/customer_suggestion_list.html', {'suggestions': suggestions})

def add_customer_suggestion(request):
    if request.method == 'POST':
        form = CustomerSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_suggestion_list')
    else:
        form = CustomerSuggestionForm()
    return render(request, 'management/add_customer_suggestion.html', {'form': form})
