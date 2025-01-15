from django.db import models # Import the models module for creating database models
from django.contrib.auth.models import User # Import the User model for authentication
from django.utils import timezone

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
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2) 
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Availability(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Boolean Field Source Code Link: https://docs.djangoproject.com/en/5.1/ref/models/fields/
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.provider.username} - {self.date} ({self.start_time}-{self.end_time})"

class Appointment(models.Model):
    availability = models.OneToOneField(Availability, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]
    
    availability = models.OneToOneField('Availability', on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} with {self.availability.provider.username}"
    

class WeeklySchedule(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    SCHEDULE_TYPES = [
        ('recurring', 'Recurring'),
        ('single', 'Single')
    ]
    schedule_type = models.CharField(
        max_length=10,
        choices=SCHEDULE_TYPES,
        default='recurring'
    )
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    specific_date = models.DateField(null=True, blank=True) # Single time block slot 

    class Meta:
        # Meta options source link: https://docs.djangoproject.com/en/5.1/ref/models/options/
        unique_together = ['provider', 'service', 'day_of_week']  # One time slot per day per service
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
    
    def create_availabilities(self, weeks_ahead=4):
        # Creates individual availability slots for the next few weeks based on this schedule
        # Source link of time units creation : https://medium.com/django-unleashed/python-timedelta-with-examples-and-use-cases-81def9140880
        from datetime import datetime, timedelta
        
        today = datetime.now().date()
        for week in range(weeks_ahead):
            # Calculate the next occurrence of this weekday
            days_ahead = self.day_of_week - today.weekday()
            if days_ahead <= 0:  # Target day already happened this week
                days_ahead += 7
            days_ahead += week * 7

            # Calculate the target date for the next occurrence of the specified weekday, considering the current date and week offset.
            target_date = today + timedelta(days=days_ahead)
            
            # Create availability if it doesn't exist
            Availability.objects.get_or_create(
                provider=self.provider,
                service=self.service,
                date=target_date,
                start_time=self.start_time,
                end_time=self.end_time,
                location=self.location,
                defaults={'is_booked': False}
            )
            
            