from django.db import models # Import the models module for creating database models
from django.contrib.auth.models import User # Import the User model for authentication

# Define the UserProfile model, extending the built-in User model with additional fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Link to the User model 
    bio = models.TextField(max_length=200, blank=True)  # Optional bio field with a max length of 200 characters
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        # Returns the username of the associated User instance as a string representation of the model.
        return self.user.username
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    CATEGORY_CHOICES = [
        ('home-care', 'Home Care'),
        ('education', 'Education'),
        ('creative', 'Creative'),
        ('health', 'Health'),
        ('events', 'Events'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title