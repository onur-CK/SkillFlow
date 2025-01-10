# SkillFlow

## Overview

SkillFlow is an innovative platform designed to connect skilled individuals with local users/customers seeking affordable services. The website enables users to offer a wide range of skills, from tutoring and language lessons to specialized services, all at reasonable prices.

Service providers can create detailed listings, showcasing their expertise, rates, and availability, while users/customers can browse through these offerings and book appointments directly through the platform. Listings are organized in an easy-to-navigate card format, providing clear descriptions of the service, skill level, and pricing.

Users can sign up for an account to access features such as service ratings, reviews, and the ability to schedule or track appointments. SkillFlow aims to foster a community-driven environment, where individuals not only access essential services but also turn their talents into a source of extra income.

With additional features like profile pages to track both services offered and received, SkillFlow is the perfect platform for anyone looking to share their expertise or find affordable, local services.



--- Link to live project

--- Link to repo

--- Tecnologies used with "colorful buttons"

## Table of Contents
1. [Project Overview](#project-overview)
    - [SkillFlow Goals](#skillflow-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
2. [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User Needs and Expectations](#user-needs-and-expectations)
    - [User Stories](#user-stories)
        - [Epic 1: User Management](#epic-1-user-management)
        - [Epic 2: Job Management](#epic-2-job-management)
        - [Epic 3: Review and Rating System](#epic-3-review-and-rating-system)
        - [Epic 4: Appointment System](#epic-4-appointment-system)
        - [Epic 5: Environment Initialization and Environment Setup](#epic-3-environment-initialization-and-environment-setup)
        - [Epic 6: Design and User Interface Setup](#epic-3-design-and-user-interface-setup)
3. [Database](#database)
    - [SkillFlow Database Schema](#skillflow-database-schema)
        - [ServiceCategory Table](#servicecategory-table)
        - [UserProfile Table](#userprofile-table)
        - [User Table](#user-table)
        - [Post Table](#post-table)
        -------------------------------------------------
        - [Comment Table](#comment-table)     (Check this one after working on comments/rating/like and dislike features)    
        --------------------------------------------------
4. [Design and Layout](#design-and-layout)
    - [Design Principles](#design-principles)
        - [Color Palette](#color-palette)
        - [Typography](#typography)
        - [Page Structure](#page-structure)
    - [User Journey](#user-journey)
        - [Before Login](#before-login)
        - [After Login](#after-login)
        - [Profile and Navigation](#profile-and-navigation)
    - [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    - [Programming Languages](#programming-languages)
    - [Frameworks](#frameworks)
    - [Database Solutions](#database-solutions)
    - [Media Management Tools](#media-management-tools)  ------------------------ (Change the topic after using cloudinary) 
    - [Supporting Libraries and Packages](#supporting-libraries-and-packages)
    - [Development Tools](#development-tools)
6. [Development Workflow](#development-workflow)
    - [Agile Project Management](#agile-project-management)
    - [GitHub Workflow](#github-workflow)
        - [User Stories as Issues](#user-stories-as-issues)
        - [Bug Tracking and Resolution](#bug-tracking-and-resolution)
    - [Iterative Development Approach](#iterative-development-approach)
    - [Backlog and Progress](#backlog-and-progress)
7. [Core Features](#core-features)
    - [Landing Page](#landing-page)
    - [Service Listings and Details](#service-listings-and-details)
    - [User Account Management](#user-account-management)
    - [Site Navigation](#site-navigation)
    - [Planned Future Features](#planned-future-features)
8. [Testing](#testing)
    - [Bug Management](#bug-management)
        - [Known Issues](#known-issues)
        - [Resolved Issues](#resolved-issues)
9. [Deployment](#deployment)
    - [SkillFlow Deployment](#skillflow-deployment)
    - [Cloudinary for Media](#cloudinary-for-media)
    - [Version Control Practices](#version-control-practices)
        - [Forking the Repository](#forking-the-repository)
        - [Cloning the Repository](#cloning-the-repository)
10. [Credits and Resources](#credits-and-resources)
    - [Media and Assets](#media-and-assets)
    - [Guides and Tutorials](#guides-and-tutorials)
        - [Django Documentation](#django-documentation)
        - [Bootstrap Documentation](#bootstrap-documentation)
        - [Learning Platforms and Videos](#learning-platforms-and-videos)
    - [Contributors](#contributors)
    - [Acknowledgments](#acknowledgments)


#wireframes

![Create account wireframe](https://github.com/user-attachments/assets/97a923fa-d13f-4e3a-8b93-e2145cb527f6)
![My Profile wireframe](https://github.com/user-attachments/assets/4985c489-6445-4da8-a343-e8f94227c715)
![MainPage wireframe](https://github.com/user-attachments/assets/dcd055c7-eb1c-41be-a5fd-d5eac3ee774a)
![login page wireframe](https://github.com/user-attachments/assets/ea3ab44b-2cfa-4149-a580-668de25ed0fc)
![Create Service Listing wireframe](https://github.com/user-attachments/assets/e2dda422-5a1e-427d-8e4f-b1d46f75885e)




##django-documentation
- Django installation: pip install django
- Django version control: python -m django --version
- Creating the project structure: django-admin startproject skillflow .




##resolved-issues (bugs ,causes and fixes)
- Bug: When the hamburger menu was opened on smaller screens, the "Login" button appeared misaligned, remaining at the bottom right corner of the screen instead of being centrally aligned beneath the dropdown menu.
- Cause: The "Login" button was placed in a separate <li> element, which caused it to behave independently of the dropdown menu. This structure prevented the button from dynamically aligning with the dropdown when it was opened.
- Fix: To resolve the issue, the HTML structure was modified to place the "Login" button as a sibling of the dropdown menu within the same parent container.



- Bug: Directory listing shown instead of index.html. When launching the project using Live Server, the browser displayed a "Listing Directory" page with all project files instead of automatically loading index.html.
- Cause: This issue occurred because multiple .html files(to work on later) existed in the root directory. Although index.html was present, Live Server may have been unable to correctly prioritize it due to one or more of the following factors:

File Priority Conflict: The presence of other .html files might have confused Live Server, especially if their names were similar to index.html or were empty files.

Directory Scanning: Live Server may have scanned all files and, in the absence of a clear default, displayed the directory listing.

Accidental Launch: An unintended file might have been selected(by live server) when starting Live Server, causing it to serve the directory or an unrelated file.
- Fix: Remove unnecessary HTML files, ensure correct file namings, restart live server, have a simple file structure.
[https://www.reddit.com/r/vscode/comments/x4y1l7/live_server_showing_listing_directory_with_a/]



- Bug: When launching the website, index.html was displaying as the homepage instead of the intended about_us.html landing page.
- Cause: The URL pattern configuration had the index view mapped to the root URL ('/'), while about_us.html was not accessible through any URL pattern.
- Fix: Modified urls.py to map the root URL ('/') to the about_us view and moved the index view to '/home/' and '/index/' paths. Additionally, added the necessary about_us view function in views.py to properly render the landing page.



![return view error](https://github.com/user-attachments/assets/26e5235e-6772-44f5-a3ca-8b41be354d72)
- Bug: The sign_up view function failed to return an HttpResponse object for GET requests, resulting in a ValueError. As a consequence, users could not access the sign-up page.
- Cause: The view was not properly handling GET requests, leading to the absence of a valid HTTP response. The function was missing the necessary return statement for rendering the sign-up form.
[https://stackoverflow.com/questions/69280755/valueerror-at-the-view-leads-views-home-page-didnt-return-an-httpresponse-obj/69280887]
- Fix: The issue was resolved by adding a return render(request, 'skillflow/sign_up.html') statement to ensure the proper rendering of the sign-up form for GET requests. This ensures the view returns an HTTP response with the necessary content for the user.



- Bug: User signup process was not redirecting to index.html after successful registration, and initially it was unclear whether the issue was with account creation or page redirection.
- Cause: Multiple issues diagnosed after debugging:
  - Form validation errors weren't visible to users, making it impossible to determine if accounts were being created
  - Redundant return statement in signup view
  - Missing authentication handling in login view
  - Incorrect form submission handling
- Fix: Implemented several solutions:
  - Added error display functionality to show validation messages, which revealed form submission issues
  - Updated views.py to properly handle authentication
  - Added POST request handling for login functionality
  - Configured correct login and redirect URLs in settings.py
  - Removed redundant code from signup view
  - Added proper form debugging and logging to track the user creation process



(Django model with choices for field.)[https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django]
- Bug: Initial confusion about why the Service model required two seemingly redundant category-related code blocks:
CATEGORY_CHOICES = [
    ('home-care', 'Home Care'),
    ('education', 'Education'),
    ('creative', 'Creative'),
    ('health', 'Health'),
    ('events', 'Events'),
]
category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
- Cause: The apparent redundancy is actually a required Django model pattern where each part serves a distinct purpose:
   - CATEGORY_CHOICES defines the available options and their display labels for the dropdown menu
   - category field creates the actual database column and constrains input to valid choices
- Fix: No changes were needed as this is the correct implementation. The dual declaration enables:
   - Form dropdown population with predefined options
   - Database-level validation of category values
   - Proper display of human-readable category names in templates
   - Data consistency throughout the application



- Bug: The edit profile page was returning a "OperationalError: no such table: skillflow_userprofile" error when attempting to access the user profile edit page.
- Cause: The database table for UserProfile model had not been created because database migrations were not generated and applied after creating the UserProfile model. Additionally, the user signup process wasn't creating UserProfile instances for new users.
- Fix: Implemented a two-part solution:
  1. Generated and applied database migrations using `python manage.py makemigrations` and `python manage.py migrate` to create the necessary database table.
  [Django Documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/)
  2. Modified the signup view to automatically create a UserProfile instance when a new user registers, and updated the edit_profile view to handle cases where a profile might not exist, using get_or_create() instead of direct access.



- Bug: Authentication-based navigation inconsistency. When clicking the SkillFlow logo in the navigation bar, non-authenticated users were incorrectly being directed to the login form instead of seeing the welcome content. This created a disjointed user experience and prevented potential users from learning about the platform before signing up.
- Cause: The root URL pattern ('') was not properly handling authentication states, and the navigation logic did not differentiate between authenticated and non-authenticated users. This occurred due to:
  1. Missing conditional routing in the URL configuration
  2. Absence of a dedicated home view to handle authentication status checks
  3. Direct routing to index view which had @login_required decorator
  4. Inconsistent navigation patterns across templates
- Fix: Implemented a comprehensive solution through several coordinated changes:
  1. Added a new 'home' view in views.py that checks authentication status:

     def home(request):
         if request.user.is_authenticated:
             return redirect('index')
         return render(request, 'skillflow/about_us.html')

  2. Updated the root URL pattern in urls.py to use this new view:

     path('', views.home, name='home')

  3. Modified template navigation to consistently use the 'home' URL
  4. Maintained the @login_required decorator on the index view for security

Impact: This fix ensures that:
1. Non-authenticated users see the welcoming "About Us" content when first visiting the site
2. Authenticated users are properly directed to their personalized dashboard with service cards
3. Navigation flow aligns with user expectations and improves overall UX
4. Security is maintained through proper authentication checks

 

- Bug: When accessing the edit profile page, users encountered a "OperationalError: no such column: skillflow_userprofile.first_name" error, preventing them from viewing or editing their profile information. This critical error occurred despite the UserProfile model being properly defined in the codebase.
- Cause: The database schema was out of sync with the model definitions. While the UserProfile model included fields for first_name, last_name, email, and bio, these columns were not properly created in the database because migrations were either missing or not applied. This discrepancy between the model definition and the actual database structure led to the operational error when attempting to access these non-existent columns.
- Fix: The issue was resolved by reconstructing and applying the database migrations properly. First, new migrations were generated using `python manage.py makemigrations` to create the necessary database schema changes based on the current model definitions. Then, these migrations were applied to the database using `python manage.py migrate`, which created the missing columns and synchronized the database structure with the model definitions. This ensured all required fields were properly created in the database table.




- Bug: The "Edit Profile" button was non-responsive despite correct HTML structure and styling. Users were unable to access the profile editing form after their initial profile setup.
- Cause: The JavaScript functionality was incorrectly embedded within the `integrity` attribute of the Bootstrap script tag. This meant that the JavaScript code responsible for handling the form visibility toggle was never executed. This occurred because:
  1. All custom JavaScript code was inadvertently placed inside the Bootstrap script's integrity attribute
  2. The script was treated as a hash value rather than executable code
  3. No error was thrown, making the issue harder to diagnose
- Fix: The solution involved properly separating the scripts:
  1. Maintained the Bootstrap script with its integrity hash:
     
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
         integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
         crossorigin="anonymous"></script>
     
  2. Added custom JavaScript in a separate script tag:
     
     <script>
         function showEditForm() {
             document.getElementById('profileForm').style.display = 'block';
             document.getElementById('infoDisplay').style.display = 'none';
         }
     </script>
    
This separation ensured proper execution of both the Bootstrap framework and the custom form handling code, restoring the edit profile functionality.
Impact: Users can now seamlessly toggle between viewing and editing their profile information, improving the overall user experience and functionality of the profile management system.




- Bug: Form fields retained unsaved changes after canceling edit mode. When users made changes to their profile information and clicked "Cancel" instead of "Save Changes", the modified data persisted in the form fields when reopening the edit form, rather than showing the last saved values.
- Cause: The form lacked state management for handling user input. The JavaScript implementation didn't maintain a reference to the original/saved values, so when the form was toggled between display and edit modes, it retained whatever values were last entered in the input fields. This occurred because:
  1. The form fields were simply being hidden and shown without resetting their values
  2. No mechanism existed to store and restore the original values
  3. The form state was tied only to DOM visibility, not to data persistence
- Fix: Implemented a comprehensive state management solution:
  1. Added an `originalValues` object to store the initial form state:
    
     let originalValues = {
         firstName: '',
         lastName: '',
         email: '',
         bio: ''
     };
 
  2. Captured original values when the page loads:
     
     document.addEventListener('DOMContentLoaded', function() {
         originalValues.firstName = document.getElementById('firstName').value;
         --> other field values
     });
   
  3. Modified the `hideEditForm` function to reset fields to their original values:
  
     function hideEditForm() {
         --> Reset form fields to original values
         document.getElementById('firstName').value = originalValues.firstName;
         --> ... reset other fields
         --> Update UI state
         document.getElementById('profileForm').style.display = 'none';
         document.getElementById('infoDisplay').style.display = 'block';
     }
    
This solution ensures that canceling edit mode properly restores the last saved state of the profile, maintaining data integrity and improving user experience by clearly distinguishing between saved and unsaved changes.



- Bug: Service creation failed with two sequential errors: first a TemplateSyntaxError for an invalid 'add_class' filter, followed by an IntegrityError regarding a NULL constraint on the provider_id field. This created a chain of issues where the form couldn't be properly rendered and, when finally submitted, failed to associate with a user.
- Cause: Multiple issues were identified:
The template attempted to use an add_class filter ({{ form.category|add_class:"form-control custom-input" }}), which isn't a built-in Django template filter
This led to duplicate form field definitions in an attempt to style the form
The service creation view wasn't associating the new service with the logged-in user before saving
- Fix: Implemented a two-part solution:

Modified the ServiceForm in forms.py to include Bootstrap classes directly in the widget definitions:
[Django HTML Attributes](https://www.geeksforgeeks.org/how-to-add-html-attributes-to-input-fields-in-django-forms/)
[Django Text-area Form Attr](https://stackoverflow.com/questions/66707030/django-textarea-form)    
[Django Min-max Digit Value](https://stackoverflow.com/questions/37024650/specify-max-and-min-in-numberinput-widget)
    class ServiceForm(forms.ModelForm):
        class Meta:
            widgets = {
                'category': forms.Select(attrs={
                    'class': 'form-control custom-input'
                }),
                ... other fields
            }

Updated the service view to properly associate the new service with the current user:
    if form.is_valid():
        service = form.save(commit=False)
        service.provider = request.user  ---> Associate with current user
        service.save()

This fix ensured proper form rendering with correct styling and maintained data integrity by properly associating new services with their providers.



- Bug: The Edit Profile form was not displaying properly when users clicked the "Edit Profile" button. The page would only show the "Account Information" header without revealing the form fields, preventing users from updating their profile information.
- Cause: The form visibility was controlled by an overly restrictive conditional statement in the template. The code {% if profile.first_name or profile.last_name or profile.email or profile.bio %} was wrapping both the display and form sections, which meant that for new users with no profile data, neither the information display nor the edit form would be rendered.
- Fix: Restructured the template logic to ensure the form is always accessible:

Separated the conditional logic for the display section from the form section
Modified the template to show the form by default for new users
Kept the display toggle functionality simple without unnecessary JavaScript complications 



[Django Documentation Static Files](https://docs.djangoproject.com/en/5.0/howto/static-files/)
- Bug: Static files (specifically styles.css) were not being served properly, resulting in a 404 error when accessing deeper URL paths like `/service/<id>/edit/`. The error appeared in the console as "GET /service/static/css/styles.css HTTP/1.1" 404 4352.
- Cause: The issue arose from two compounding factors:
  1. Using relative paths (`../../static/css/styles.css`) for static files, which broke when accessing URLs at different directory depths
  2. Improper Django static files configuration - missing proper static file settings and directory structure
- Fix: Implemented a comprehensive solution to properly configure static files in Django:
  1. Updated settings.py to include proper static file configurations:
     -->>
     STATIC_URL = 'static/'
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     STATICFILES_DIRS = [
         os.path.join(BASE_DIR, 'static'),
     ]
      
  2. Modified templates to use Django's static template tags instead of relative paths:
     -->>
     {% load static %}
     <link href="{% static 'css/styles.css' %}" rel="stylesheet">
     
  3. Ran `python manage.py collectstatic` to collect all static files into the static root directory

This solution ensures static files are served correctly regardless of URL depth and follows Django's recommended practices for static file handling.




- Bug: When multiple users attempted to book the same service time slot, the system would raise a "UNIQUE constraint failed: skillflow_appointment.availability_id" error. This created a race condition where two users could try to book the same availability slot simultaneously, resulting in a broken booking experience.

- Cause: The issue arose due to multiple factors:
  1. The Appointment model had a OneToOneField relationship with Availability, meaning each availability slot could only have one appointment
  2. The booking process lacked proper validation to check if an availability slot was already booked
  3. No database transaction management was in place to handle concurrent booking attempts
  4. The system wasn't properly updating the `is_booked` status of availability slots

- Fix: Implemented a comprehensive solution through several coordinated changes:
  1. Added proper validation checks in the booking view:
     
     if availability.is_booked:
         messages.error(request, 'Sorry, this time slot has already been booked.')
         return redirect('book_appointment', service_id=service_id)
     
  [Database Transaction](https://www.geeksforgeeks.org/transaction-atomic-with-django/)
  [Database Transaction](https://docs.djangoproject.com/en/5.1/topics/db/transactions/)
  2. Implemented database transaction management to ensure data consistency:
     
     with transaction.atomic():
         appointment = Appointment.objects.create(
             availability=availability,
             client=request.user
         )
         availability.is_booked = True
         availability.save()
     
  3. Added error handling with user feedback through Django messages
  4. Updated the availability queryset to only show unbooked slots:
     
     availabilities = Availability.objects.filter(
         service=service,
         is_booked=False,
         [date__gte](https://forum.djangoproject.com/t/timezone-warning-from-date-filtering-via-the-orm/11776)
         [date__gte](https://www.w3schools.com/django/ref_lookups_gte.php)
         date__gte=timezone.now().date()
     ).order_by('date', 'start_time')
     

This fix ensures that:
1. Users can't double-book availability slots
2. The booking process is atomic and handles concurrent attempts properly
3. Users receive clear feedback when a slot is no longer available
4. Only available future time slots are displayed for booking





##Modular Code Architecture -------------------------- Check the topic name
Modular Code Design for 'SkillFlow'
At SkillFlow, we employ a modular code structure, akin to building with LEGO blocks, to ensure flexibility, maintainability, and efficiency throughout our development process. Each part of our system is designed to function independently while integrating seamlessly into the larger framework. This approach enables us to:

Enhance Collaboration:
Developers can work on different modules simultaneously without interfering with others. This streamlines teamwork and accelerates development timelines.

Simplify Updates and Changes:
By isolating functionality into discrete components, updates or changes can be made to specific modules without impacting unrelated parts of the system. This reduces risk and simplifies the implementation of new features.

Facilitate Debugging and Testing:
Modular design allows us to identify, isolate, and resolve bugs more efficiently. Each module can be tested independently, ensuring higher code quality and reliability.

Promote Code Reusability:
Common functionalities are encapsulated in reusable components, reducing redundancy and ensuring consistency across the platform.

Future-Proof the System:
A modular architecture provides the flexibility to expand or refactor the platform as the needs of our users evolve, ensuring SkillFlow remains robust and adaptable.

Code Structure Highlights
Service-Oriented Modules: Each service (e.g., appointment scheduling, user reviews/ratings or likes/dislikes) is implemented as a separate module to maintain clear boundaries and responsibilities.
Styling Components: The UI follows a consistent theme, using subdued tones like grey and orangered to enhance user experience while maintaining a professional aesthetic.
Feature Segmentation: Features such as user profiles, skill listings, and ratings are built independently to allow focused improvements and scalability.
This modular approach reflects our commitment to delivering a platform that is not only user-friendly but also developer-friendly. It aligns with our vision of making SkillFlow a dynamic and reliable service-sharing platform that adapts to the needs of our community.




#Building the Login Form Component: Modular Development ------------------------------------- check the topic name

Overview
• This document outlines our approach to creating the SkillFlow login form by leveraging existing Bootstrap classes and custom CSS from our signup form
• This methodology demonstrates the efficiency of modular development and component reusability in modern web development

Development Process

1. Component Structure
   • Built the login form by reusing the following classes from our signup form:
     - .form-card - Main container styling
     - .custom-input - Input field styling
     - .custom-submit - Button styling
     - .custom-link - Link styling

2. Bootstrap Integration
   • Utilized Bootstrap's built-in classes:
     - .container and .row for layout
     - .col-md-6 for responsive column sizing
     - .mb-3 and .mb-4 for consistent spacing
     - .form-control for input styling
     - .btn and .w-100 for button styling

3. Custom Styling Reuse
   • Maintained consistent branding by reusing our custom CSS:
     - Form card styling with dark theme (#161b22)
     - Custom input styling with dark background (#0d1014)
     - Consistent border and padding styles
     - Unified color scheme across components

Benefits of This Approach

1. Rapid Development
   • Reduced development time by reusing existing components
   • Minimized the need for new CSS writing
   • Quick implementation of consistent styling

2. Maintainability
   • Centralized styling in one CSS file
   • Easy updates across multiple components
   • Reduced CSS redundancy

3. Consistency
   • Identical styling between signup and login forms
   • Consistent user experience across components
   • Unified dark theme implementation

4. Scalability
   • Easy to replicate pattern for future components
   • Modular structure allows for easy modifications
   • Reduced technical debt

Best Practices Implemented

1. Component Reusability
   • Used existing class structures
   • Maintained consistent naming conventions
   • Leveraged Bootstrap's utility classes

2. Code Organization
   • Clear separation of concerns
   • Modular CSS structure
   • Consistent class naming

3. Performance
   • Minimal additional CSS
   • Optimized class reuse
   • Reduced stylesheet size

Conclusion
• This approach to building the login form demonstrates the power of modular development and component reusability
• By leveraging existing styles and Bootstrap classes, we created a consistent, maintainable, and efficient component that aligns perfectly with our application's design system
• The success of this implementation reinforces our "building blocks" approach to development, showing how well-structured initial components can speed up future development while maintaining high quality and consistency






Kanban board image
![Kanban Board ](https://github.com/user-attachments/assets/042f91f3-e415-41fe-8b0d-47476ee6a6a2)



[Django date query from newest to oldest] (https://stackoverflow.com/questions/30314741/django-date-query-from-newest-to-oldest)


[Bootstrap Table] (https://getbootstrap.com/docs/4.0/content/tables/)
[table] freecodecamp link !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!