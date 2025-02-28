# Deployment Guide for SkillFlow

## Table of Contents
* [Deployment](#deployment)
  * [Initial Deployment](#initial-deployment)
    * [Creating the Repository](#creating-the-repository)
    * [Setting up the Development Environment](#setting-up-the-development-environment)
    * [Creating a Heroku Application](#creating-a-heroku-application)
    * [Configuring Environment Variables](#configuring-environment-variables)
    * [Configuring Django Settings](#configuring-django-settings)
    * [Deploying to Heroku via CLI](#deploying-to-heroku-via-cli)
  * [Database Setup](#database-setup)
    * [Local Development with SQLite](#local-development-with-sqlite)
    * [Production Database with PostgreSQL](#production-database-with-postgresql)
    * [Executing Database Migrations](#executing-database-migrations)
  * [Static and Media Files](#static-and-media-files)
    * [Configuring Static Files](#configuring-static-files)
    * [Implementing Whitenoise for Static Files](#implementing-whitenoise-for-static-files)
  * [Security Configuration](#security-configuration)
    * [Django Secret Key Management](#django-secret-key-management)
    * [HTTPS and SSL Configuration](#https-and-ssl-configuration)
    * [Cross-Site Request Forgery Protection](#cross-site-request-forgery-protection)
  * [Local Deployment](#local-deployment)
    * [Cloning the Repository](#cloning-the-repository)
    * [Setting up a Virtual Environment](#setting-up-a-virtual-environment)
    * [Installing Dependencies](#installing-dependencies)
    * [Running the Application Locally](#running-the-application-locally)
  * [Continuous Deployment](#continuous-deployment)
    * [Automating Deployments with GitHub](#automating-deployments-with-github)


## Deployment

The deployment process for SkillFlow has been meticulously planned and executed to ensure a seamless transition from development to production. This guide provides comprehensive instructions for setting up both local development environments and production deployments.

### Initial Deployment

Below are the detailed steps taken to deploy SkillFlow to Heroku, along with the necessary console commands.

#### Creating the Repository

1. Create a new repository in GitHub named "SkillFlow"
2. Clone the repository locally following [GitHub's cloning instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

#### Setting up the Development Environment

1. Create a virtual environment:
   
   python -m venv .venv
   

2. Add `.venv` to your `.gitignore` file to prevent version control tracking of the virtual environment

3. Activate the virtual environment:
   * Powershell On Windows: `.venv\Scripts\Activate.ps1`
   * Command Prompt On Windows: `.venv\Scripts\activate.bat`
   * Bash - macOS/Linux: `source .venv/bin/activate`

"Before executing the commands, ensure that you navigate to the project directory where the .venv folder is located."

4. Install Django with version 5.1.4:
   
   pip install django==5.1.4
   

5. Install Gunicorn for production server:
   
   pip install gunicorn
   

6. Install database adapters and cloud storage libraries:
   
   pip install dj-database-url psycopg2-binary
   pip install python-dotenv
   pip install whitenoise
   

7. Create requirements file:
   
   pip freeze > requirements.txt
   

8. Create the SkillFlow project:
   
   django-admin startproject skillflow .
   

9. Create the main app:
   
   python manage.py startapp skillflow
   

10. Add the app to INSTALLED_APPS in settings.py:
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'skillflow',
    ]
    

11. Run initial migrations:
    
    python manage.py migrate
    

12. Test the server locally:
    
    python manage.py runserver
    

#### Creating a Heroku Application

The following steps assume an existing Heroku account and active login:

1. Log into [Heroku Dashboard](https://dashboard.heroku.com/)

2. Click "New" in the top-right corner and select "Create new app"

3. Provide a unique name for your application (e.g., "skillflow-community-django")

4. Select the appropriate region (e.g., Europe)

5. Add PostgreSQL database to the Heroku app:
   * Navigate to the "Resources" tab
   * Under "Add-ons", search for "Heroku Postgres"
   * Select "Hobby Dev - Free" plan
   * Click "Submit Order Form"

#### Configuring Environment Variables

1. Create a `.env` file in your project's root directory and add it to `.gitignore`

2. Configure the following environment variables in your `.env` file:
   
   DATABASE_URL=your_database_url_from_heroku
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   

3. Configure the same environment variables in Heroku:
   * Go to your app's "Settings" tab
   * Click "Reveal Config Vars"
   * Add the following variables:
     - SECRET_KEY: your_django_secret_key
     - DATABASE_URL: Your database url (postgres://username:password@hostname:port/dbname)
     - DEBUG: False (for production)

#### Configuring Django Settings

1. Update the settings.py file to use environment variables:
   ```python
   import os
   import dj_database_url
   from pathlib import Path
   from dotenv import load_dotenv

   # Load environment variables from .env file
   load_dotenv()

   # Set DEBUG based on environment variable
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'

   # Secret key configuration
   SECRET_KEY = os.getenv('SECRET_KEY')

   # Database configuration
   DATABASES = {
       'default': dj_database_url.config(
           default=os.environ.get('DATABASE_URL'),
           conn_max_age=600,
           ssl_require=True
       )
   }
   ```

2. Configure allowed hosts:
   ```python
   ALLOWED_HOSTS = ['skillflow-community-django-7358f56ac457.herokuapp.com', 'localhost', '127.0.0.1']
   ```

3. Configure static files:
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static')
   ]
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

4. Create a Procfile in the project root:
   ```
   web: gunicorn skillflow.wsgi
   ```

#### Deploying to Heroku via CLI

1. Install Heroku CLI if not already installed:
   * Follow instructions at [Heroku CLI Installation](https://devcenter.heroku.com/articles/heroku-cli)

2. Log in to Heroku via CLI:
   
   heroku login -i
   

3. Add Heroku remote to your Git repository:
   
   heroku git:remote -a your-heroku-app-name
   

4. Push your code to Heroku:
   
   git push heroku main
   

5. Run migrations on Heroku:
   
   heroku run python manage.py migrate
   

6. Create a superuser on Heroku (optional):
   
   heroku run python manage.py createsuperuser
   

### Database Setup

SkillFlow leverages Django's ORM system to interact with the database, allowing for seamless transitions between development and production environments.

#### Local Development with SQLite

For local development, SQLite provides a convenient, file-based database solution:

1. Configure development settings in `.env`:
   ```
   DATABASE_URL=sqlite:///db.sqlite3
   ```

2. Update settings.py to use SQLite for local development:
   ```python
   # Use SQLite for local development if DATABASE_URL is not set
   if 'DATABASE_URL' not in os.environ:
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
   ```

#### Production Database with PostgreSQL

For production, SkillFlow uses Heroku's PostgreSQL offering:

1. The DATABASE_URL is automatically set by Heroku when the PostgreSQL add-on is provisioned

2. The dj_database_url package parses this URL and configures Django accordingly

3. SSL is required for security in production:
   ```python
   DATABASES = {
       'default': dj_database_url.config(
           default=os.environ.get('DATABASE_URL'),
           conn_max_age=600,
           ssl_require=True
       )
   }
   ```

#### Executing Database Migrations

Database migrations must be executed to create the necessary tables:

1. For local development:
   
   python manage.py makemigrations
   python manage.py migrate
   

2. For production (Heroku):
   
   heroku run python manage.py migrate
   

### Static and Media Files

SkillFlow uses a combination of static files (CSS, JavaScript) to create a responsive, modern user interface.

#### Configuring Static Files

Static files in Django require specific configuration:

1. Define static file directories in settings.py:
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static')
   ]
   ```

2. Collect static files for production:
   
   python manage.py collectstatic
   

#### Implementing Whitenoise for Static Files

Whitenoise is used to serve static files efficiently in production:

1. Add Whitenoise to middleware in settings.py:
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Add after security middleware     
   ]
   ```

2. Configure Whitenoise storage:
   ```python
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

### Security Configuration

Security is a paramount concern for SkillFlow, with multiple layers of protection implemented.

#### Django Secret Key Management

The Django SECRET_KEY is securely managed:

1. In development, it's stored in the .env file (which is not committed to version control)

2. In production, it's set as a Heroku config variable

3. The settings.py file loads it from environment variables:
   ```python
   SECRET_KEY = os.environ.get("SECRET_KEY")
   ```

#### HTTPS and SSL Configuration

HTTPS is enforced in production:

1. Configure SSL settings in settings.py:
   ```python
   if not DEBUG:  # Production settings
       # Forces HTTPS
       SECURE_SSL_REDIRECT = True
       # Ensures the request is through HTTPS
       SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
       # HSTS settings
       SECURE_HSTS_SECONDS = 31536000  # 1 year
       SECURE_HSTS_INCLUDE_SUBDOMAINS = True
       SECURE_HSTS_PRELOAD = True
       # XSS Filter
       SECURE_BROWSER_XSS_FILTER = True
       # Cookie settings
       SESSION_COOKIE_SECURE = True
       CSRF_COOKIE_SECURE = True
   ```

#### Cross-Site Request Forgery Protection

CSRF protection is implemented:

1. Django's built-in CSRF middleware is enabled:
   ```python
   MIDDLEWARE = [
       # ... other middleware
       'django.middleware.csrf.CsrfViewMiddleware',
       # ... other middleware
   ]
   ```

2. All forms include the {% csrf_token %} template tag

3. CSRF cookie security is enhanced in production:
   ```python
   CSRF_COOKIE_SECURE = True
   CSRF_COOKIE_HTTPONLY = True
   ```

### Local Deployment

Following these steps will set up a local development environment for SkillFlow.

#### Cloning the Repository

1. Navigate to the [SkillFlow GitHub repository](https://github.com/onur-CK/SkillFlow)

2. Click the "Code" button and copy the repository URL

3. Open your terminal/command prompt

4. Navigate to the directory where you want to clone the repository

5. Run the following command:
   ```
   git clone https://github.com/onur-CK/SkillFlow.git
   ```

#### Setting up a Virtual Environment

1. Navigate to the cloned repository:
   ```
   cd SkillFlow
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   * Powershell On Windows: `.venv\Scripts\Activate.ps1`
   * Command Prompt On Windows: `.venv\Scripts\activate.bat`
   * Bash - macOS/Linux: `source .venv/bin/activate`

#### Installing Dependencies

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Create a .env file in the project root with the following variables:
   ```
   DATABASE_URL=sqlite:///db.sqlite3
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

#### Running the Application Locally

1. Apply migrations:
   ```
   python manage.py migrate
   ```

2. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```
   python manage.py runserver
   ```

4. Access the application at http://127.0.0.1:8000/

### Continuous Deployment

SkillFlow employs continuous deployment practices to streamline the deployment process.

#### Automating Deployments with GitHub

Heroku can be configured to automatically deploy from GitHub:

1. In the Heroku Dashboard, navigate to your app's "Deploy" tab

2. Under "Deployment method", select "GitHub"

3. Connect to your GitHub repository

4. Under "Automatic deploys", select the branch you want to deploy from (usually "main")

5. Enable "Wait for CI to pass before deploy" if using CI/CD services

6. Click "Enable Automatic Deploys"

This comprehensive deployment guide ensures that SkillFlow can be deployed consistently and securely, whether for local development or production use. The configuration leverages industry best practices for Django applications, with a focus on security, performance, and maintainability.