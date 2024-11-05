from django.db import models
from django.core.validators import MinValueValidator

class SeasonalFlavor(models.Model):
    """
    Represents a seasonal flavor of chocolate.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    availability_start = models.DateField()
    availability_end = models.DateField()
    season = models.CharField(max_length=20, choices=[('Spring', 'Spring'), 
                                                    ('Summer', 'Summer'), 
                                                    ('Fall', 'Fall'), 
                                                    ('Winter', 'Winter')],
                           default='Spring')  
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0,message="Price cannot be negative")])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """Returns a string representation of the SeasonalFlavor."""
        return self.name
    

class Ingredient(models.Model):
    """
    Represents an ingredient inventory.
    """
    ingredient_name = models.CharField(max_length=100, unique=True)
    quantity_in_stock = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=[('kg', 'Kilograms'),
                                                    ('g', 'Grams'),
                                                    ('l', 'Liters'),],
                               default='kg')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient_name

class CustomerSuggestion(models.Model):
    """
    Represents a suggestion submitted by a customer regarding flavors.
    """
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.CharField(max_length=200, default=" ")  
    allergy_concerns = models.CharField(max_length=200, default="None")
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.flavor_suggestion}"


