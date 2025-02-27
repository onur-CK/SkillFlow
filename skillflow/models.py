# Import the models module for creating database models
from django.db import models
# Import the User model for authentication
from django.contrib.auth.models import User
from django.utils import timezone

"""
This module defines the database models for the SkillFlow application.
Each class represents a database table and
includes field definitions and methods.
"""


"""
Define the UserProfile model, extending the built-in
User model with additional fields
"""
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#extending-the-existing-user-model


class UserProfile(models.Model):
    """
    Extended user profile model that adds additional
    fields to Django's built-in User model.
    Uses OneToOneField for direct user association.
    """

    # https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#extending-user.
    """
    Link to the User model with CASCADE deletion to ensure
    profile is deleted when user is deleted
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Link to the User model
    # TextField for longer form content with max_length validation
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#textfield
    bio = models.TextField(
        max_length=200, blank=True
    )  # Optional bio field with a max length of 200 characters
    # CharField for shorter text content
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#charfield
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # EmailField for validated email addresses
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#emailfield
    email = models.EmailField(blank=True)

    def __str__(self):
        """
        Returns the username of the associated User instance
        as a string representation of the model.
        """
        return self.user.username


class Service(models.Model):
    """
    Model for service listings with categorization and provider association.
    Includes price tracking and creation timestamp.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    # Predefined choices for service categories
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-choices
    CATEGORY_CHOICES = [
        ("home-care", "Home Care"),
        ("education", "Education"),
        ("creative", "Creative"),
        ("health", "Health"),
        ("events", "Events"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # DecimalField for precise monetary values
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#decimalfield
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    # Link to service provider (User)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    # Automatic timestamp for creation time
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.DateTimeField.auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Availability(models.Model):
    # Model for managing service provider availability slots.
    # Includes validation and uniqueness constraints.
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # https://docs.djangoproject.com/en/5.1/ref/models/options/
    class Meta:
        # Orders availabilities by date and time
        ordering = ["date", "start_time"]
        # Prevents duplicate time slots
        # Ensure no overlapping time slots for the same provider and service
        # https://docs.djangoproject.com/en/5.1/ref/models/constraints/#uniqueconstraint
        constraints = [
            models.UniqueConstraint(
                fields=["provider", "service", "date", "start_time"],
                name="unique_availability",
            )
        ]

    def __str__(self):
        return (
            f"{self.service.title} - "
            f"{self.date} ({self.start_time}-{self.end_time})"
        )

    def clean(self):
        """
        Validates availability slots:
        -> Prevents past dates
        -> Ensures end time is after start time
        """
        from django.core.exceptions import ValidationError

        # Ensure date is not in the past
        if self.date < timezone.now().date():
            raise ValidationError("Cannot create availability for past dates")

        # Ensure end_time is after start_time
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time")


# https://docs.djangoproject.com/en/5.1/topics/db/examples/one_to_one/
class Appointment(models.Model):
    """
    Model for managing service appointments.
    Links availability slots with clients and tracks appointment status.
    """

    """
    One-to-one relationship ensures each
    availability can only have one appointment
    """
    availability = models.OneToOneField(Availability, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    # Status choices for appointment tracking
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#choices
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.client.username} with "
            f"{self.availability.provider.username}"
        )


# https://docs.djangoproject.com/en/5.1/topics/db/models/#model-inheritance
class WeeklySchedule(models.Model):
    """
    Model for managing recurring weekly schedules.
    Allows providers to set regular availability patterns.
    """

    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    # Days of week choices using integer values
    DAYS_OF_WEEK = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        # https://docs.djangoproject.com/en/5.1/ref/models/options/#unique-together
        unique_together = ["provider", "service", "day_of_week", "start_time"]
        ordering = ["day_of_week", "start_time"]

    def __str__(self):
        return (
            f"{self.get_day_of_week_display()} "
            f"{self.start_time}-{self.end_time}"
        )

    def create_availabilities(self):
        """
        Creates availability slots for the next 4 weeks
        based on the weekly schedule.Generates recurring
        slots while avoiding duplicates.
        """
        from datetime import date, timedelta

        # Get today's date
        today = date.today()

        # Calculate next occurrence of scheduled weekday
        days_ahead = self.day_of_week - today.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        next_date = today + timedelta(days=days_ahead)

        # Generate slots for next 4 weeks
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
                is_booked=False,
            )
