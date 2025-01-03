from django.db import models # Import the models module for creating database models
from django.contrib.auth.models import User # Import the User model for authentication

# Define the UserProfile model, extending the built-in User model with additional fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Link to the User model 
    bio = models.TextField(max_length=200, blank=True)  # Optional bio field with a max length of 200 characters
    
    def __str__(self):
        # Returns the username of the associated User instance as a string representation of the model.
        return self.user.username
    