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
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    # Boolean Field Source Code Link: https://docs.djangoproject.com/en/5.1/ref/models/fields/
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Ordering and Constraints Source Link: https://docs.djangoproject.com/en/5.1/ref/models/options/
    class Meta:
        ordering = ['date', 'start_time']
        # Ensure no overlapping time slots for the same provider and service
        constraints = [
            models.UniqueConstraint(
                fields=['provider', 'service', 'date', 'start_time'],
                name='unique_availability'
            )
        ]

    def __str__(self):
        return f"{self.service.title} - {self.date} ({self.start_time}-{self.end_time})"

    def clean(self):
        from django.core.exceptions import ValidationError
        # Ensure date is not in the past
        if self.date < timezone.now().date():
            raise ValidationError('Cannot create availability for past dates')
        
        # Ensure end_time is after start_time
        if self.end_time <= self.start_time:
            raise ValidationError('End time must be after start time')
    

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

    class Meta:
        unique_together = ['provider', 'service', 'day_of_week', 'start_time']
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
    
    def create_availabilities(self):
        """
        Creates availability slots for the next 4 weeks based on the weekly schedule.
        """
        from datetime import date, timedelta
        
        # Get today's date
        today = date.today()
        
        # Find the next occurrence of this weekday
        days_ahead = self.day_of_week - today.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        next_date = today + timedelta(days=days_ahead)
        
        # Create availabilities for the next 4 weeks
        for week in range(4):
            availability_date = next_date + timedelta(weeks=week)
            
            # Create the availability slot
            Availability.objects.create(
                provider=self.provider,
                service=self.service,
                date=availability_date,
                start_time=self.start_time,
                end_time=self.end_time,
                location=self.location,
                is_booked=False
            )

        
            