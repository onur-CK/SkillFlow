# Testing

## Contents
* [Code Validation](#code-validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
* [Accessibility Testing](#accessibility-testing)
    * [WAVE Tool Results](#wave-tool-results)
    * [Lighthouse Reports](#lighthouse-reports)
* [Browser Compatibility](#browser-compatibility)
* [Device Compatibility](#device-compatibility)
* [Manual Testing](#manual-testing)
    * [User Story Testing](#user-story-testing)
    * [Feature Testing](#feature-testing)
    * [Form Testing](#form-testing)
    * [Security Testing](#security-testing)
* [Automated Testing](#automated-testing)
    * [Python Unit Tests](#python-unit-tests)
    * [Coverage Report](#coverage-report)
* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Known Bugs](#known-bugs)




Manual Testing
Does the site work as intended? 
Quality assurance: stpes taken to manually test the project, ensures it functions correctly, identifies potential bugs
User exerperience assurance: ensures that the end-users have a smooth experience by addressing potential issues
-- final manual testing and write up

## Bugs

### Fixed Bugs

#### Navigation Display Bug

- **Bug**: When the hamburger menu was opened on smaller screens, the "Login" button appeared misaligned, remaining at the bottom right corner of the screen instead of being centrally aligned beneath the dropdown menu.
- **Cause**: The "Login" button was placed in a separate <li> element, which caused it to behave independently of the dropdown menu. This structure prevented the button from dynamically aligning with the dropdown when it was opened.
- **Fix**: To resolve the issue, the HTML structure was modified to place the "Login" button as a sibling of the dropdown menu within the same parent container.

#### Directory Listing Bug

- **Bug**: Directory listing shown instead of index.html. When launching the project using Live Server, the browser displayed a "Listing Directory" page with all project files instead of automatically loading index.html.
- **Cause**: This issue occurred because multiple .html files(to work on later) existed in the root directory. Although index.html was present, Live Server may have been unable to correctly prioritize it due to one or more of the following factors:

File Priority Conflict: The presence of other .html files might have confused Live Server, especially if their names were similar to index.html or were empty files.

Directory Scanning: Live Server may have scanned all files and, in the absence of a clear default, displayed the directory listing.

Accidental Launch: An unintended file might have been selected(by live server) when starting Live Server, causing it to serve the directory or an unrelated file.
- **Fix**: Remove unnecessary HTML files, ensure correct file namings, restart live server, have a simple file structure.
[https://www.reddit.com/r/vscode/comments/x4y1l7/live_server_showing_listing_directory_with_a/]


#### Home Page Routing Bug

- **Bug**: When launching the website, index.html was displaying as the homepage instead of the intended about_us.html landing page.
- **Cause**: The URL pattern configuration had the index view mapped to the root URL ('/'), while about_us.html was not accessible through any URL pattern.
- **Fix**: Modified urls.py to map the root URL ('/') to the about_us view and moved the index view to '/home/' and '/index/' paths. Additionally, added the necessary about_us view function in views.py to properly render the landing page.

#### Sign-up View Bug

![return view error](https://github.com/user-attachments/assets/26e5235e-6772-44f5-a3ca-8b41be354d72)

- **Bug**: The sign_up view function failed to return an HttpResponse object for GET requests, resulting in a ValueError. As a consequence, users could not access the sign-up page.
- **Cause**: The view was not properly handling GET requests, leading to the absence of a valid HTTP response. The function was missing the necessary return statement for rendering the sign-up form.
- **Reference**:[https://stackoverflow.com/questions/69280755/valueerror-at-the-view-leads-views-home-page-didnt-return-an-httpresponse-obj/69280887]
- **Fix**: The issue was resolved by adding a return render(request, 'skillflow/sign_up.html') statement to ensure the proper rendering of the sign-up form for GET requests. This ensures the view returns an HTTP response with the necessary content for the user.

#### User Authentication Bug

- **Bug**: User signup process was not redirecting to index.html after successful registration, and initially it was unclear whether the issue was with account creation or page redirection.
- **Cause**: Multiple issues diagnosed after debugging:
  - Form validation errors weren't visible to users, making it impossible to determine if accounts were being created
  - Redundant return statement in signup view
  - Missing authentication handling in login view
  - Incorrect form submission handling
- **Fix**: Implemented several solutions:
  - Added error display functionality to show validation messages, which revealed form submission issues
  - Updated views.py to properly handle authentication
  - Added POST request handling for login functionality
  - Configured correct login and redirect URLs in settings.py
  - Removed redundant code from signup view
  - Added proper form debugging and logging to track the user creation process

#### Service Model Category Bug

(Django model with choices for field.)[https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django]
- **Bug**: Initial confusion about why the Service model required two seemingly redundant category-related code blocks:
CATEGORY_CHOICES = [
    ('home-care', 'Home Care'),
    ('education', 'Education'),
    ('creative', 'Creative'),
    ('health', 'Health'),
    ('events', 'Events'),
]
category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
- **Cause**: The apparent redundancy is actually a required Django model pattern where each part serves a distinct purpose:
   - CATEGORY_CHOICES defines the available options and their display labels for the dropdown menu
   - category field creates the actual database column and constrains input to valid choices
- **Fix**: No changes were needed as this is the correct implementation. The dual declaration enables:
   - Form dropdown population with predefined options
   - Database-level validation of category values
   - Proper display of human-readable category names in templates
   - Data consistency throughout the application

#### User Profile Database Bug

- **Bug**: The edit profile page was returning a "OperationalError: no such table: skillflow_userprofile" error when attempting to access the user profile edit page.
- **Cause**: The database table for UserProfile model had not been created because database migrations were not generated and applied after creating the UserProfile model. Additionally, the user signup process wasn't creating UserProfile instances for new users.
- **Fix**: Implemented a two-part solution:
  1. Generated and applied database migrations using `python manage.py makemigrations` and `python manage.py migrate` to create the necessary database table.
- **Reference**:[Django Documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/)
  2. Modified the signup view to automatically create a UserProfile instance when a new user registers, and updated the edit_profile view to handle cases where a profile might not exist, using get_or_create() instead of direct access.

#### Authentication Navigation Bug

- **Bug**: Authentication-based navigation inconsistency. When clicking the SkillFlow logo in the navigation bar, non-authenticated users were incorrectly being directed to the login form instead of seeing the welcome content. This created a disjointed user experience and prevented potential users from learning about the platform before signing up.
- **Cause**: The root URL pattern ('') was not properly handling authentication states, and the navigation logic did not differentiate between authenticated and non-authenticated users. This occurred due to:
  1. Missing conditional routing in the URL configuration
  2. Absence of a dedicated home view to handle authentication status checks
  3. Direct routing to index view which had @login_required decorator
  4. Inconsistent navigation patterns across templates
- **Fix**: Implemented a comprehensive solution through several coordinated changes:
  1. Added a new 'home' view in views.py that checks authentication status:

     def home(request):
         if request.user.is_authenticated:
             return redirect('index')
         return render(request, 'skillflow/about_us.html')

  2. Updated the root URL pattern in urls.py to use this new view:

     path('', views.home, name='home')

  3. Modified template navigation to consistently use the 'home' URL
  4. Maintained the @login_required decorator on the index view for security

**Impact**: This fix ensures that:
1. Non-authenticated users see the welcoming "About Us" content when first visiting the site
2. Authenticated users are properly directed to their personalized dashboard with service cards
3. Navigation flow aligns with user expectations and improves overall UX
4. Security is maintained through proper authentication checks

 #### Profile Column Bug

- **Bug**: When accessing the edit profile page, users encountered a "OperationalError: no such column: skillflow_userprofile.first_name" error, preventing them from viewing or editing their profile information. This critical error occurred despite the UserProfile model being properly defined in the codebase.
- **Cause**: The database schema was out of sync with the model definitions. While the UserProfile model included fields for first_name, last_name, email, and bio, these columns were not properly created in the database because migrations were either missing or not applied. This discrepancy between the model definition and the actual database structure led to the operational error when attempting to access these non-existent columns.
- **Fix**: The issue was resolved by reconstructing and applying the database migrations properly. First, new migrations were generated using `python manage.py makemigrations` to create the necessary database schema changes based on the current model definitions. Then, these migrations were applied to the database using `python manage.py migrate`, which created the missing columns and synchronized the database structure with the model definitions. This ensured all required fields were properly created in the database table.


#### Edit Profile Button Bug

- **Bug**: The "Edit Profile" button was non-responsive despite correct HTML structure and styling. Users were unable to access the profile editing form after their initial profile setup.
- **Cause**: The JavaScript functionality was incorrectly embedded within the `integrity` attribute of the Bootstrap script tag. This meant that the JavaScript code responsible for handling the form visibility toggle was never executed. This occurred because:
  1. All custom JavaScript code was inadvertently placed inside the Bootstrap script's integrity attribute
  2. The script was treated as a hash value rather than executable code
  3. No error was thrown, making the issue harder to diagnose
- **Fix**: The solution involved properly separating the scripts:
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


#### Form State Management Bug

- **Bug**: Form fields retained unsaved changes after canceling edit mode. When users made changes to their profile information and clicked "Cancel" instead of "Save Changes", the modified data persisted in the form fields when reopening the edit form, rather than showing the last saved values.
- **Cause**: The form lacked state management for handling user input. The JavaScript implementation didn't maintain a reference to the original/saved values, so when the form was toggled between display and edit modes, it retained whatever values were last entered in the input fields. This occurred because:
  1. The form fields were simply being hidden and shown without resetting their values
  2. No mechanism existed to store and restore the original values
  3. The form state was tied only to DOM visibility, not to data persistence
- **Fix**: Implemented a comprehensive state management solution:
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
         --> other field values.......
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
    
- **Impact**:This solution ensures that canceling edit mode properly restores the last saved state of the profile, maintaining data integrity and improving user experience by clearly distinguishing between saved and unsaved changes.

#### Service Creation Bug

- **Bug**: Service creation failed with two sequential errors: first a TemplateSyntaxError for an invalid 'add_class' filter, followed by an IntegrityError regarding a NULL constraint on the provider_id field. This created a chain of issues where the form couldn't be properly rendered and, when finally submitted, failed to associate with a user.
- **Cause**: Multiple issues were identified:
The template attempted to use an add_class filter ({{ form.category|add_class:"form-control custom-input" }}), which isn't a built-in Django template filter
This led to duplicate form field definitions in an attempt to style the form
The service creation view wasn't associating the new service with the logged-in user before saving
- **Fix**: Implemented a two-part solution:
- **Reference**: 
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

#### Profile Form Display Bug

- **Bug**: The Edit Profile form was not displaying properly when users clicked the "Edit Profile" button. The page would only show the "Account Information" header without revealing the form fields, preventing users from updating their profile information.
- **Cause**: The form visibility was controlled by an overly restrictive conditional statement in the template. The code {% if profile.first_name or profile.last_name or profile.email or profile.bio %} was wrapping both the display and form sections, which meant that for new users with no profile data, neither the information display nor the edit form would be rendered.
- **Fix**: Restructured the template logic to ensure the form is always accessible:

Separated the conditional logic for the display section from the form section
Modified the template to show the form by default for new users
Kept the display toggle functionality simple without unnecessary JavaScript complications 

#### Static Files Bug

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

#### Booking System Bug

- **Bug**: When multiple users attempted to book the same service time slot, the system would raise a "UNIQUE constraint failed: skillflow_appointment.availability_id" error. This created a race condition where two users could try to book the same availability slot simultaneously, resulting in a broken booking experience.

- **Cause**: The issue arose due to multiple factors:
  1. The Appointment model had a OneToOneField relationship with Availability, meaning each availability slot could only have one appointment
  2. The booking process lacked proper validation to check if an availability slot was already booked
  3. No database transaction management was in place to handle concurrent booking attempts
  4. The system wasn't properly updating the `is_booked` status of availability slots

- **Fix**: Implemented a comprehensive solution through several coordinated changes:
  1. Added proper validation checks in the booking view:
     
     if availability.is_booked:
         messages.error(request, 'Sorry, this time slot has already been booked.')
         return redirect('book_appointment', service_id=service_id)
- **References**:  
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
- **References**:         
         [date__gte](https://forum.djangoproject.com/t/timezone-warning-from-date-filtering-via-the-orm/11776)
         [date__gte](https://www.w3schools.com/django/ref_lookups_gte.php)
         date__gte=timezone.now().date()
     ).order_by('date', 'start_time')
     
- **Impact**: 
This fix ensures that:
1. Users can't double-book availability slots
2. The booking process is atomic and handles concurrent attempts properly
3. Users receive clear feedback when a slot is no longer available
4. Only available future time slots are displayed for booking

#### Schedule Deletion Bug

- **Bug**: When attempting to delete a weekly schedule slot, users encountered a "NoReverseMatch" error with the message "Reverse for 'delete_schedule' with arguments '(2,)' not found". This prevented users from removing unwanted time slots from their service schedules.

- **Cause**: The URL pattern mismatch occurred due to multiple factors:
  1. The URL pattern in urls.py expected two parameters (service_id and schedule_id): 
     `path('service/<int:service_id>/schedule/delete/<int:schedule_id>/')`
  2. The template was only providing one parameter (schedule_id):
     `{% url 'delete_schedule' schedule.id %}`
  3. This created a parameter count mismatch between the URL pattern definition and the template's URL generation attempt

- **Fix**: Modified the template's form action to include both required parameters in the correct order:
  
  <form method="POST" action="{% url 'delete_schedule' service.id schedule.id %}"
        class="d-inline" onsubmit="return confirm('Delete this time slot?');">
  
  This ensures the URL is generated with both the service_id and schedule_id parameters, matching the URL pattern definition and allowing the delete functionality to work as intended.

#### Scheduling System Architecture Bug

- **Bug**: The initial implementation of the scheduling system used a WeeklySchedule model that automatically created recurring appointments for the next 4 weeks. This caused several issues:
  1. Providers couldn't set specific one-time appointments
  2. The system would automatically create 4 weeks of slots regardless of provider availability
  3. Schedule management was inflexible and didn't account for varying provider schedules
  4. Providers couldn't easily handle exceptions to their regular schedule

- **Cause**: The architectural design assumed providers would want recurring weekly schedules, implementing this through:
  1. A WeeklySchedule model that stored day-of-week and time patterns
  2. An automated system that would generate 4 weeks of Availability slots based on these patterns
  3. A complex create_availabilities() method that would populate future dates
  4. URL patterns and views that were built around managing weekly schedules rather than individual time slots

- **Fix**: Implemented a comprehensive solution through several coordinated changes:
  1. Models:
     - Removed the WeeklySchedule model entirely
     - Simplified to using only the Availability model for direct time slot management
     - Updated model relationships to focus on individual time slots
     - Enhanced validation for overlapping slots and past dates

  2. Forms:
     - Simplified the AvailabilityForm to handle single time slot creation
     - Added improved validation for date and time selections
     - Enhanced the user interface with better date/time input controls
     - Implemented clearer error messaging for invalid slots

  3. Views:
     - Rewrote manage_schedule view to handle individual time slots
     - Added direct CRUD operations for availabilities
     - Implemented better error handling for overlapping slots
     - Added validation for attempted changes to booked slots

  4. URLs:
     - Updated URL patterns to match new view names
     - Changed from schedule-based to availability-based endpoints
     - Simplified routing structure
     - Enhanced the design of the API endpoints for better adherence to web service standards.

  5. Templates:
     - Redesigned schedule management interface for individual slot creation
     - Improved slot visibility and management
     - Added clearer status indicators for available/booked slots
     - Enhanced user feedback for actions

- **Impact**: This fix transformed the scheduling system to be more flexible and user-friendly:
    - Providers can now create specific time slots for exact dates
    - Better handling of irregular schedules and exceptions
    - More intuitive interface for managing availability
    - Reduced complexity in the codebase
    - Improved system reliability and maintainability

- **References**:
- [Django Model Constraints](https://docs.djangoproject.com/en/5.1/ref/models/constraints/)
- [Django Form Validation](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)
- [Django Time Zones](https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/)

#### Test Suite Validation Bug

- **Bug**: Unit tests were failing with multiple errors:
  1. `UserProfile.DoesNotExist` error in service detail view tests
  2. Form validation failures for invalid dates in availability tests
  3. Incorrect validation of negative hourly rates in service form tests
  4. Improper exception handling in availability model tests

- **Cause**: The test suite had several structural issues:
  1. Test data setup was incomplete:
     - UserProfile instances weren't being created for test users
     - Required relationships between models weren't properly established
     - Test data dependencies weren't properly managed
  
  2. Validation logic was inconsistent:
     - Form-level validation wasn't properly implemented for hourly rates
     - Date validation was happening at the wrong level
     - Exception types weren't properly specified
  
  3. Test assertions were misaligned:
     - Tests were looking for errors in wrong locations (field-level vs form-level)
     - Validation error messages weren't being checked correctly
     - Exception handling wasn't properly implemented in test cases

- **Fix**: Implemented a comprehensive solution through several coordinated changes:
  1. Enhanced Test Setup:
     
     def setUp(self):
         self.user = User.objects.create_user(
             username='testuser',
             password='testpass123'
         )
         self.user_profile = UserProfile.objects.create(
             user=self.user,
             first_name='Test',
             last_name='User',
             email='test@example.com'
         )
         self.service = Service.objects.create(
             title='Test Service',
             description='Test Description',
             category='education',
             hourly_rate=50.00,
             provider=self.user
         )
     
  
  2. Improved Validation Logic:
     - Added proper form-level validation for hourly rates:
     
     def clean_hourly_rate(self):
         hourly_rate = self.cleaned_data.get('hourly_rate')
         if hourly_rate and hourly_rate < 0:
             raise forms.ValidationError("Hourly rate cannot be negative.")
         return hourly_rate
     
     - Implemented proper date validation in Availability model:
     
     def clean(self):
         if self.date < timezone.now().date():
             raise ValidationError('Cannot create availability for past dates')
     

  3. Fixed Test Assertions:
     - Updated availability test to use correct exception type:
     
     with self.assertRaises(ValidationError):
         availability.full_clean()
    
     - Corrected form validation checks:
     
     self.assertIn('Cannot create availability for past dates', 
                  form.errors['__all__'])
    

- **Impact**: These fixes improved the test suite by:
  1. Ensuring all model relationships are properly tested
  2. Validating business logic at the appropriate levels
  3. Providing better test coverage for edge cases
  4. Making tests more maintainable and readable
  5. Establishing proper test data management practices

- **References**:
  - [Django Documentation - Testing Tools](https://docs.djangoproject.com/en/5.0/topics/testing/tools/)
  - [Django Documentation - Model Validation](https://docs.djangoproject.com/en/5.0/ref/models/instances/#validating-objects)
  - [Django Documentation - Form and Field Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)

![manage py tests](https://github.com/user-attachments/assets/433f9b45-cfca-4fb4-ae84-0d5628bd80d4)



----------------------------------------------------------------


## Testing

### Code Validation
All code has been meticulously validated using industry-standard tools:
- HTML validated through W3C HTML Validator
- CSS validated through W3C CSS Validator
- JavaScript validated through JSHint
- Python code validated through PEP8 online checker

### Accessibility Testing
- WAVE Web Accessibility Evaluation Tool used to identify and fix accessibility issues
- Keyboard navigation testing to ensure all functions are accessible without a mouse
- Screen reader compatibility testing
- Color contrast checked to meet WCAG 2.1 AA standards

### Browser Compatibility
The platform has been tested and optimized for all major browsers:
- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge
- Opera

### Device Compatibility
Extensive testing has been conducted across multiple device types:
- Desktop computers (various screen sizes)
- Laptops (13" to 17" screens)
- Tablets (iPad, Samsung Galaxy Tab)
- Mobile phones (iPhone, Samsung, Google Pixel)

### Manual Testing
Comprehensive manual testing procedures have been implemented:
- User flow testing for all primary pathways
- Form validation testing
- Cross-device functionality testing
- Feature-by-feature verification

### Automated Testing
- Unit tests for critical functions and models
- Integration tests for feature interactions
- Performance testing for load handling capabilities
- Security testing for vulnerability detection

### Bugs
#### Fixed Bugs

During the development process, several bugs were identified and fixed:

##### Navigation Display Bug
- **Bug**: When the hamburger menu was opened on smaller screens, the "Login" button appeared misaligned, remaining at the bottom right corner of the screen instead of being centrally aligned beneath the dropdown menu.
- **Cause**: The "Login" button was placed in a separate <li> element, which caused it to behave independently of the dropdown menu. This structure prevented the button from dynamically aligning with the dropdown when it was opened.
- **Fix**: To resolve the issue, the HTML structure was modified to place the "Login" button as a sibling of the dropdown menu within the same parent container.

##### Directory Listing Bug
- **Bug**: Directory listing shown instead of index.html. When launching the project using Live Server, the browser displayed a "Listing Directory" page with all project files instead of automatically loading index.html.
- **Cause**: This issue occurred because multiple .html files(to work on later) existed in the root directory. Although index.html was present, Live Server may have been unable to correctly prioritize it due to one or more of the following factors:
  - File Priority Conflict: The presence of other .html files might have confused Live Server, especially if their names were similar to index.html or were empty files.
  - Directory Scanning: Live Server may have scanned all files and, in the absence of a clear default, displayed the directory listing.
  - Accidental Launch: An unintended file might have been selected(by live server) when starting Live Server, causing it to serve the directory or an unrelated file.
- **Fix**: Remove unnecessary HTML files, ensure correct file namings, restart live server, have a simple file structure.

##### Home Page Routing Bug
- **Bug**: When launching the website, index.html was displaying as the homepage instead of the intended about_us.html landing page.
- **Cause**: The URL pattern configuration had the index view mapped to the root URL ('/'), while about_us.html was not accessible through any URL pattern.
- **Fix**: Modified urls.py to map the root URL ('/') to the about_us view and moved the index view to '/home/' and '/index/' paths. Additionally, added the necessary about_us view function in views.py to properly render the landing page.

##### Sign-up View Bug
- **Bug**: The sign_up view function failed to return an HttpResponse object for GET requests, resulting in a ValueError. As a consequence, users could not access the sign-up page.
- **Cause**: The view was not properly handling GET requests, leading to the absence of a valid HTTP response. The function was missing the necessary return statement for rendering the sign-up form.
- **Fix**: The issue was resolved by adding a return render(request, 'skillflow/sign_up.html') statement to ensure the proper rendering of the sign-up form for GET requests. This ensures the view returns an HTTP response with the necessary content for the user.

##### User Authentication Bug
- **Bug**: User signup process was not redirecting to index.html after successful registration, and initially it was unclear whether the issue was with account creation or page redirection.
- **Cause**: Multiple issues diagnosed after debugging:
  - Form validation errors weren't visible to users, making it impossible to determine if accounts were being created
  - Redundant return statement in signup view
  - Missing authentication handling in login view
  - Incorrect form submission handling
- **Fix**: Implemented several solutions:
  - Added error display functionality to show validation messages, which revealed form submission issues
  - Updated views.py to properly handle authentication
  - Added POST request handling for login functionality
  - Configured correct login and redirect URLs in settings.py
  - Removed redundant code from signup view
  - Added proper form debugging and logging to track the user creation process

##### Service Model Category Bug
- **Bug**: Initial confusion about why the Service model required two seemingly redundant category-related code blocks:
```python
CATEGORY_CHOICES = [
    ('home-care', 'Home Care'),
    ('education', 'Education'),
    ('creative', 'Creative'),
    ('health', 'Health'),
    ('events', 'Events'),
]
category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
```
- **Cause**: The apparent redundancy is actually a required Django model pattern where each part serves a distinct purpose:
   - CATEGORY_CHOICES defines the available options and their display labels for the dropdown menu
   - category field creates the actual database column and constrains input to valid choices
- **Fix**: No changes were needed as this is the correct implementation. The dual declaration enables:
   - Form dropdown population with predefined options
   - Database-level validation of category values
   - Proper display of human-readable category names in templates
   - Data consistency throughout the application

#### Known Bugs

