# The Dream Chocolate House

## Overview
The Fictional Chocolate House project is a Python application designed to manage seasonal chocolate flavors, ingredient inventory, and customer suggestions. This project uses Django as the web framework and SQLite as the database backend, focusing on backend logic and data management rather than front-end development.

## Features
- **Seasonal Flavors Management**: Add, view, and manage seasonal chocolate flavors with details such as availability, price, and season.
- **Ingredient Inventory**: Track ingredients used in flavors, including stock quantity and measurement units.
- **Customer Suggestions**: Allow customers to submit flavor suggestions along with any allergy concerns.
- **Validation**: Implement data validation to ensure proper input (e.g., non-negative prices, valid dates).

## Technologies Used
- **Django**: Web framework for building the application.
- **SQLite**: Lightweight database for storing flavor, ingredient, and suggestion data.
- **HTML/CSS**: Basic web technologies for rendering the user interface.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django
- SQLite (comes bundled with Django)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SN-Varshith/The-Dream-Chocolate-House.git
   cd chocolate_house

2. Install required packages:
   pip install django

3. Run the database migrations:
   python manage.py migrate

4. Run the development server:
   python manage.py runserver

Access the application by navigating to http://127.0.0.1:8000/ in your web browser.
  


Test Steps
To validate the application, follow these test steps:

1. Test Seasonal Flavor Creation
Navigate to the "Add Seasonal Flavor" page.  http://127.0.0.1:8000/add-seasonal-flavor/
Fill in the fields:

Name: "Coconut Delight"
Description: "Delicious coconut flavored chocolates"
Availability Start: "2024-05-22"
Availability End: "2024-09-22"
Season: "Spring"
Price: "450.00"
Is Available: Check the box

Submit the form and verify:
The new flavor appears in the list of seasonal flavors.
http://127.0.0.1:8000/seasonal-flavors/


2. Test Validation for Price
Navigate to the "Add Seasonal Flavor" page.   http://127.0.0.1:8000/add-seasonal-flavor/
Fill in the fields:

Name: "Coconut Delight" (Redundant name)
Description: "Rich chocolate flavor"
Availability Start: "22-05-2024" (invalid date)
Availability End: "2024-09-22"
Season: "Spring"
Price: "-350" (invalid input)

Submit the form and verify:
An error message 
"Seasonal flavor with this Name already exists."
"Enter a valid date."
"Price must be greater than 0."  is displayed in red.


3. Test Ingredient Addition
Navigate to the "Add Ingredient" page.  http://127.0.0.1:8000/add-ingredient/
Fill in the fields:
Ingredient Name: "Chocolate Powder"
Quantity in Stock: "50.00"
Unit: "kg"
Submit the form and verify:
The ingredient appears in the ingredient list. http://127.0.0.1:8000/ingredients/


4. Test Ingredient Addition
Navigate to the "Add Ingredient" page.  http://127.0.0.1:8000/add-ingredient/
Fill in the fields:
Ingredient Name: "Chocolate Powder"
Quantity in Stock: "-50.00"
Unit: "kg"
Submit the form and verify:

An error message 
"Ingredient with this Ingredient name already exists."
"Ensure this value is greater than or equal to 0."



5. Test Customer Suggestion Submission
Navigate to the "Add Customer Suggestion" page. 
http://127.0.0.1:8000/add-customer-suggestion/

Fill in the fields:

Customer Name: "Amith Sharan"
Flavor Suggestion: "Millet Chocolate"
Allergy Concerns: "Allergic to eggs"

Submit the form and verify:
The suggestion appears in the suggestions list.
http://127.0.0.1:8000/customer-suggestions/


Error Handling
The application implements error handling to manage various edge cases:

1. **Date Validation**: Validates dates to ensure they are in the correct format (YYYY-MM-DD).
2. **Price Validation**: Ensures prices are non-negative.
3. **Ingredient Name Uniqueness**: Ensures ingredient names are unique to prevent duplication.
4. **Quantity Validation**: Ensures quantities cannot be negative.
5. **Django Validation Messages**: Utilizes Django's built-in validation messages styled in red for better visibility.




ORM Abstraction Implementation

In this project, we utilized Django's Object-Relational Mapping (ORM) to handle database operations seamlessly. The ORM allows us to interact with the database using Python objects instead of writing raw SQL queries. Below is an overview of how the ORM was implemented in the project.

Models
The following models were defined in models.py to represent the main entities of the application:

1.SeasonalFlavor: Represents the seasonal flavors available in the chocolate house.

Attributes include name, description, availability_start, availability_end, season, price, and is_available.
The name field is unique to prevent duplicate entries.

class SeasonalFlavor(models.Model):
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
        return self.name

2.Ingredient: Represents the ingredients used for making flavors.

Attributes include ingredient_name, quantity_in_stock, unit, and last_updated.
The ingredient_name field is unique to prevent redundancy.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100, unique=True)
    quantity_in_stock = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=[('kg', 'Kilograms'),
                                                    ('g', 'Grams'),
                                                    ('l', 'Liters'),],
                               default='kg')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ingredient_name

3.CustomerSuggestion: Captures customer suggestions for new flavors.

Attributes include customer_name, flavor_suggestion, allergy_concerns, and submitted_on.

class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.CharField(max_length=200, default=" ")  
    allergy_concerns = models.CharField(max_length=200, default="None")
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.flavor_suggestion}"


Benefits of Using ORM
1. Abstraction: The ORM abstracts away the complexities of SQL, allowing developers to focus on application logic rather than database intricacies.
2. Portability: Code written using the ORM is more portable across different database backends.
3. Security: It helps protect against SQL injection attacks through parameterized queries.
4. Simplified Database Operations: The ORM simplifies database operations by providing a high-level interface for creating, reading, updating, and deleting data.
5. Improved Code Readability: The ORM improves code readability by using Python objects and methods to interact with the database, making the code more intuitive and easier to understand.



Example to create a new seasonal flavor using Django's ORM:

new_flavor = SeasonalFlavor.objects.create(
    name='Mint Chocolate',
    description='A refreshing mint chocolate flavor.',
    availability_start='2024-05-01',
    availability_end='2024-09-30',
    season='Spring',
    price=3.99,
    is_available=True
)

Querying Data-
Retrieve seasonal flavors as follows:
flavors = SeasonalFlavor.objects.filter(is_available=True)
for flavor in flavors:
    print(flavor.name)

Accessing the Django Admin Page
After starting the server, you can access the admin page at http://127.0.0.1:8000/admin/

Log in using the credentials:
username: admin_L7_informatics
Password: L7informatics@123


## Docker-based Build and Run

### Prerequisites
Make sure you have Docker installed on your machine. You can download it from [Docker's official website](https://www.docker.com/get-started).

### Building the Docker Image
To build the Docker image, run the following command in your terminal from the root directory of your project:

```bash
docker build -t chocolate_house .
```

Running the Docker Container
Once the image is built, you can run it using the following command:
```bash
docker run -p 8000:8000 chocolate_house
```

Stopping the Application
```bash
docker stop $(docker ps -aq --filter name=chocolate_house)
```

