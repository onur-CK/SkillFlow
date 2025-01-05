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
  2. Modified the signup view to automatically create a UserProfile instance when a new user registers, and updated the edit_profile view to handle cases where a profile might not exist, using get_or_create() instead of direct access.





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



