"""
ASGI config for skillflow project.

ASGI (Asynchronous Server Gateway Interface) is a specification that describes
how async-capable Python web servers, frameworks, and applications communicate
with each other. This is the ASGI configuration for the skillflow project.

Key aspects:
- Provides support for asynchronous request handling
- Enables WebSocket support and other async protocols
- Acts as an interface between the web server and Django application
"""
# Source Link: https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
import os

from django.core.asgi import get_asgi_application

# Set the Django settings module path for the ASGI application
# This ensures Django knows which settings to use when running the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillflow.settings')

"""
Initialize the ASGI application
This creates an ASGI-compatible application object that web servers can use
to communicate with Django application
"""
application = get_asgi_application()
