# SkillFlow

## Overview

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





