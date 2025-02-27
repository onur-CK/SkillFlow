"""
Django's command-line utility for administrative tasks.

This script is automatically created when starting a Django project and serves as the
primary entry point for all Django management commands. It's used to run server,
create migrations, apply migrations, create superusers, and much more.

"""

# Source: https://docs.djangoproject.com/en/5.1/ref/django-admin/
import os
import sys


def main():
    """Run administrative tasks.

    This function sets up the Django environment and executes the command-line
    arguments provided by the user.

    Source: https://docs.djangoproject.com/en/5.1/topics/settings/#designating-the
    -settings
    """
    # Set the DJANGO_SETTINGS_MODULE environment variable to point to settings file
    # This tells Django which settings module to use for skillflow project
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skillflow.settings")
    try:
        # Import the command execution function from Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Provide helpful error message if Django isn't installed or available
        # Source: https://docs.djangoproject.com/en/5.1/intro/tutorial01/
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Pass the command-line arguments to Django's command executor
    # This is what processes commands like 'runserver', 'makemigrations', etc.
    # Source: https://docs.djangoproject.com/en/5.1/ref/django-admin/#available-commands
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Execute the main function when script is run directly
    # Source: https://docs.python.org/3/library/__main__.html
    main()
