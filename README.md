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


