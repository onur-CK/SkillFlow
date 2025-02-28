# SkillFlow

### What is SkillFlow?

SkillFlow is a comprehensive web-based platform designed to bridge the gap between skilled individuals and those seeking affordable, local services. In today's gig economy, many talented individuals possess valuable skills but lack an efficient way to connect with potential clients, while others struggle to find reliable, affordable service providers in their community. SkillFlow addresses this challenge by providing a user-friendly marketplace where service providers can showcase their expertise and clients can easily find and book the services they need.

## Table of Contents
1. [Project Overview](#project-overview)
   - [SkillFlow Goals](#skillflow-goals)
   - [User Goals](#user-goals)
   - [Site Owner Goals](#site-owner-goals)
   - [What is SkillFlow?](#what-is-skillflow)
   - [Why Does SkillFlow Exist?](#why-does-skillflow-exist)
   - [Who is it For?](#who-is-it-for)
   - [Expectations](#expectations)
2. [User Experience (UX)](#user-experience-ux)
   - [Target Audience](#target-audience)
   - [User Requirements and Expectations](#user-requirements-and-expectations)
   - [User Stories](#user-stories)
3. [Planning Phase](#planning-phase)
   - [Strategy](#strategy)
   - [Scope](#scope)
   - [Structure](#structure)
   - [Skeleton](#skeleton)
   - [Surface](#surface)
4. [Database Design](#database-design)
   - [SkillFlow Database Schema](#skillflow-database-schema)
   - [Models](#models)    
   - [ServiceCategory Table](#servicecategory-table)
   - [UserProfile Table](#userprofile-table)
   - [User Table](#user-table)
   - [Post Table](#post-table)
5. [Design and Layout](#design-and-layout)
   - [Design Principles](#design-principles)
   - [Color Palette](#color-palette)
   - [Typography](#typography)
   - [Page Structure](#page-structure)
   - [User Journey](#user-journey)
   - [Wireframes](#wireframes)
6. [Development Workflow](#development-workflow)
   - [Agile Project Management](#agile-project-management)
   - [GitHub Workflow](#github-workflow)
   - [User Stories as Issues](#user-stories-as-issues)
   - [Bug Tracking and Resolution](#bug-tracking-and-resolution)
   - [Iterative Development Approach](#iterative-development-approach)
   - [Backlog and Progress](#backlog-and-progress)
   - [Modular Code Architecture](#modular-code-architecture)
7. [Features](#features)
   - [Site Navigation](#site-navigation)
   - [User Authentication & Profiles](#user-authentication--profiles)
   - [Service Management](#service-management)
   - [Appointment/Booking System](#appointmentbooking-system)
   - [Information Architecture](#information-architecture)
   - [Interactive UI Elements](#interactive-ui-elements)
   - [Service Discovery](#service-discovery)
   - [Planned Future Features](#planned-future-features)
8. [Testing](#testing) 
9. [Deployment](#deployment)
10. [Credits and Resources](#credits-and-resources)
    - [Tutorials](#tutorials)
    - [Media and Assets](#media-and-assets)
    - [Guides and Tutorials](#guides-and-tutorials)
    - [Django Documentation](#django-documentation)
    - [Bootstrap Documentation](#bootstrap-documentation)
    - [Learning Platforms and Videos](#learning-platforms-and-videos)
    - [Contributors](#contributors)
    - [Acknowledgments](#acknowledgments)
11. [Technologies Used](#technologies-used)
   - [Programming Languages](#programming-languages)
   - [Frameworks](#frameworks)
   - [Database Solutions](#database-solutions)
   - [Media Management Tools](#media-management-tools)
   - [Supporting Libraries and Packages](#supporting-libraries-and-packages)
   - [Development Tools](#development-tools)    

## Project Overview

SkillFlow is an innovative platform designed to connect skilled individuals with local users/customers seeking affordable services. The website enables users to offer a wide range of skills, from tutoring and language lessons to specialized services, all at reasonable prices.

Service providers can create detailed listings, showcasing their expertise, rates, and availability, while users/customers can browse through these offerings and book appointments directly through the platform. Listings are organized in an easy-to-navigate card format, providing clear descriptions of the service, skill level, and pricing.

Users can sign up for an account to access features such as service ratings, reviews, and the ability to schedule or track appointments. SkillFlow aims to foster a community-driven environment, where individuals not only access essential services but also turn their talents into a source of extra income.

With additional features like profile pages to track both services offered and received, SkillFlow is the perfect platform for anyone looking to share their expertise or find affordable, local services.

### SkillFlow Goals
- Create a user-friendly marketplace for skill exchange and service provision
- Foster a community of skilled individuals and service seekers
- Provide an efficient booking and scheduling system
- Ensure transparent pricing and service descriptions
- Enable skill monetization for service providers

### User Goals
- Find affordable, quality services in their local area
- Book appointments easily and manage schedules effectively
- Access detailed information about service providers
- Communicate directly with service providers
- Track service history and manage bookings

### Site Owner Goals
- Build a sustainable platform for skill exchange
- Generate revenue through platform fees
- Maintain high user satisfaction and engagement
- Expand the service provider network
- Ensure platform security and reliability

### Why Does SkillFlow Exist?

The platform was created to address several key market needs:

1. **Democratizing Service Access**: Traditional service marketplaces often have high barriers to entry, making it difficult for skilled individuals to offer their services and for clients to find affordable options. SkillFlow removes these barriers by providing a straightforward platform where anyone with valuable skills can create a service listing.

2. **Community Building**: Unlike generic job boards or classified ads, SkillFlow focuses on building a community-driven ecosystem where service providers can build their reputation and clients can make informed decisions based on detailed profiles and transparent pricing.

3. **Simplified Scheduling**: The platform streamlines the booking process through an integrated scheduling system, eliminating the back-and-forth communication typically required to arrange services.

4. **Economic Empowerment**: By providing a platform where individuals can monetize their skills, SkillFlow enables people to create additional income streams while helping others access needed services at reasonable rates.

### Who is it For?

SkillFlow serves two primary user groups:

#### Service Providers:
- Skilled professionals looking to offer their services on a flexible schedule
- Individuals with expertise in areas like education, home care, creative arts, health and wellness, or event planning
- Freelancers seeking to build a client base and manage their bookings efficiently
- People looking to monetize their skills and earn extra income

#### Clients:
- Individuals seeking affordable, local services across various categories
- People who prefer to support their local community rather than large service companies
- Users looking for personalized service experiences with direct provider communication
- Those who value transparent pricing and easy scheduling functionality

### Expectations

SkillFlow is designed to be:
- **User-Friendly**: The platform features an intuitive interface that makes it easy for both providers and clients to navigate and use effectively.
- **Transparent**: All service listings include clear pricing and detailed descriptions.
- **Professional**: While maintaining accessibility, the platform encourages professional conduct and quality service delivery.
- **Community-Focused**: The system is built around fostering positive interactions and building trust within the service marketplace.

## User Experience (UX)

### Target Audience
- Skilled professionals seeking to monetize their expertise
- Local community members seeking affordable services
- Students and young professionals offering tutoring services
- Freelancers looking for a reliable platform
- Small business owners expanding their reach

### User Requirements and Expectations
- Intuitive navigation and clear user interface
- Secure user authentication and data protection
- Reliable booking and scheduling system
- Clear communication channels
- Transparent pricing and service descriptions
- Mobile-responsive design
- Quick loading times and smooth performance

## Planning Phase

### Strategy

During the planning phase for SkillFlow, we did a lot of research to understand the issues in the current service marketplace. What we found was a big gap between people with skills who want to offer their services and clients who are looking for affordable, quality options.

**Strategic Priorities:**
1. Create an intuitive platform that minimizes barriers to entry for service providers
2. Develop a robust booking system that streamlines the appointment process
3. Implement security features to protect user data and build trust
4. Design a responsive interface that works seamlessly across all devices
5. Establish a scalable architecture that can accommodate future growth

### Scope

Based on our strategic analysis, we defined the scope of SkillFlow to include essential features that deliver maximum value to users while maintaining a manageable development timeline. We utilized the MoSCoW method (Must have, Should have, Could have, Won't have) to prioritize features:

**Must Have Features:**
- User registration and authentication system
- Service listing creation and management
- Appointment booking functionality
- User profiles for service providers and clients
- Category-based service organization

**Should Have Features:**
- Availability management system
- User-to-user messaging
- Notification system for bookings and updates
- Advanced search and filtering options
- Responsive design for all device types

**Could Have Features:**
- Rating and review system
- Payment integration
- Featured listings for premium users
- Social media sharing functionality
- Advanced analytics for service providers

**Won't Have (for initial release):**
- Real-time video consultation
- Subscription-based membership tiers
- Mobile applications (focusing on responsive web design instead)
- AI-powered service matching
- Marketplace for physical products

### Structure

SkillFlow is built on a hierarchical structure designed to provide intuitive navigation and efficient access to information. The site architecture follows a logical flow that guides users through the service discovery and booking process:

1. **Top Level:**
   - Home page with platform introduction
   - Category-based service navigation
   - User authentication portal

2. **Middle Level:**
   - Service listings organized by category
   - User dashboard with personalized content
   - Booking management interface

3. **Detail Level:**
   - Individual service detail pages
   - Appointment scheduling interface
   - User profile management
   - Communication tools

The information architecture is designed to minimize the number of clicks required to complete key actions, ensuring a smooth user experience throughout the platform.

### Skeleton

The skeleton framework of SkillFlow was developed through wireframing and prototyping to visualize the interface before full-scale development. We focused on:

1. **Navigation Design:**
   - Consistent navigation bar with context-aware elements
   - Intuitive category filtering system
   - Breadcrumb navigation for deeper page levels

2. **Interface Design:**
   - Clean, card-based layout for service listings
   - Form-based interfaces for data entry
   - Modal dialogs for quick actions

3. **Content Organization:**
   - Hierarchical content structure
   - Progressive disclosure of information
   - Contextual help and guidance

### Surface

The visual design of SkillFlow is crafted to create a professional, trustworthy impression while maintaining an approachable and engaging user experience. Key design decisions include:

1. **Color Scheme:**
   - Primary: Turquoise Blue (#00beef) for branding and call-to-action elements
   - Secondary: Orange Red (#FF4500) for highlighting and contrast
   - Background: Dark theme (#0D1014, #161B22) for modern, professional appearance
   - Text: White (#FFFFFF) for optimal readability against dark backgrounds

2. **Typography:**
   - System default sans-serif fonts for optimal loading performance
   - Consistent text hierarchy with clear heading styles
   - Appropriate font sizing for readability across devices

3. **Visual Elements:**
   - Subtle animations for interactive elements
   - Icon-based category identification
   - Consistent spacing and alignment throughout

## Database Design

### SkillFlow Database Schema
The database architecture for SkillFlow is designed to efficiently manage users, services, availabilities, and appointments through carefully structured relationships that support the platform's core functionality.

### Models

#### UserProfile Model
Extends Django's built-in User model to store additional user information.

- **Fields:**
  - `user` (OneToOneField → User): Direct link to Django's User model with CASCADE deletion
  - `first_name` (CharField): User's first name (max 30 characters)
  - `last_name` (CharField): User's last name (max 30 characters)
  - `email` (EmailField): Contact email address
  - `bio` (TextField): User description/biography (max 200 characters)

- **Relationships:**
  - OneToOne with Django's User model
  - Implicitly referenced by Service via User FK
  - Implicitly referenced by Availability via User FK
  - Implicitly referenced by Appointment via User FK

#### Service Model
Stores details about services offered by providers.

- **Fields:**
  - `title` (CharField): Service title (max 100 characters)
  - `description` (TextField): Detailed service description
  - `category` (CharField): Service category from predefined choices
  - `hourly_rate` (DecimalField): Service cost per hour
  - `provider` (ForeignKey → User): User offering the service
  - `created_at` (DateTimeField): Automatic timestamp of creation

- **Relationships:**
  - ManyToOne with User (provider)
  - OneToMany with Availability (service can have multiple availability slots)
  - Indirectly linked to Appointments through Availability

#### Availability Model
Manages time slots when services are available for booking.

- **Fields:**
  - `provider` (ForeignKey → User): Service provider
  - `service` (ForeignKey → Service): Associated service offering
  - `date` (DateField): Date of availability
  - `start_time` (TimeField): Start time of the slot
  - `end_time` (TimeField): End time of the slot
  - `location` (CharField): Meeting location (max 200 characters)
  - `is_booked` (BooleanField): Flag indicating if slot is booked (default: False)
  - `created_at` (DateTimeField): Automatic timestamp of creation

- **Constraints:**
  - UniqueConstraint on provider, service, date, and start_time to prevent duplicate slots
  - Custom validation to ensure future dates and valid time ranges

- **Relationships:**
  - ManyToOne with User (provider)
  - ManyToOne with Service
  - OneToOne with Appointment (each availability can have at most one appointment)

#### Appointment Model
Tracks bookings made by clients for specific availability slots.

- **Fields:**
  - `availability` (OneToOneField → Availability): The booked time slot
  - `client` (ForeignKey → User): User booking the service
  - `status` (CharField): Current status from predefined choices (pending, confirmed, cancelled)
  - `created_at` (DateTimeField): Automatic timestamp of creation

- **Relationships:**
  - OneToOne with Availability (ensures each slot can only be booked once)
  - ManyToOne with User (client)
  - Indirectly linked to Service via Availability

### Relationship Diagram
```
User (Django built-in)
  ↑ OneToOne
  |
UserProfile
  |
  |                         ┌── OneToOne ──────┐
  |                         ↓                  |
  └── via User FK → Service → Availability ←───┘
                               ↑
                               | OneToOne
                               ↓
                           Appointment ← via User FK
```

### Model Relationships Explained

1. **User & UserProfile:**
   - Each Django User has exactly one UserProfile via a OneToOne relationship
   - When a User is deleted, their associated UserProfile is also deleted (CASCADE)

2. **User & Service:**
   - A User (as provider) can create multiple Service listings
   - Each Service belongs to exactly one User (provider)
   - Service deletion does not affect the User

3. **Service & Availability:**
   - A Service can have multiple Availability slots
   - Each Availability slot is associated with exactly one Service
   - When a Service is deleted, all its Availability slots are also deleted (CASCADE)

4. **User & Availability:**
   - A User (as provider) can create multiple Availability slots
   - Each Availability belongs to exactly one User (provider)
   - When a User is deleted, all their Availability slots are also deleted (CASCADE)

5. **Availability & Appointment:**
   - An Availability slot can have at most one Appointment (OneToOne)
   - When an Availability is deleted, its associated Appointment is also deleted (CASCADE)
   - The `is_booked` flag on Availability indicates whether an Appointment exists

6. **User & Appointment:**
   - A User (as client) can make multiple Appointments
   - Each Appointment is associated with exactly one User (client)
   - When a User is deleted, all their Appointments are also deleted (CASCADE)

This relational design ensures data consistency while efficiently supporting key platform operations:
- Service providers can create and manage multiple service listings
- Each service can offer multiple availability slots
- Clients can book available slots, creating appointments
- The system prevents double-booking through the OneToOne relationship between Availability and Appointment
- Appointment status can be tracked independently of availability status

### Data Integrity Enforcement
The model design includes several mechanisms to maintain data integrity:
- Database-level constraints (OneToOne, ForeignKey relationships)
- Model-level validation (clean method in Availability)
- Form-level validation
- Transaction management for critical operations (e.g., booking creation)

## Design and Layout

### Design Principles
- Clean and minimalist interface
- Consistent branding throughout
- Clear visual hierarchy
- Responsive design for all devices
- Accessible color contrast
- Intuitive navigation patterns

### Color Palette
- Primary: #00beef (Turquoise Blue)
- Secondary: #FF4500 (Orange Red)
- Background: #0D1014 (Dark)
- Text: #FFFFFF (White)
- Accent: #161B22 (Dark Gray)

### Typography
- Primary Font: System default sans-serif
- Secondary Font: Font Awesome for icons
- Text Sizes: Responsive and scaled appropriately
- Font Weights: Regular (400) and Bold (700)

### Page Structure
- Header with navigation
- Main content area
- Sidebar for filters (where applicable)
- Footer with additional links
- Mobile-responsive layout

### User Journey
1. Landing Page
2. Service Browse/Search
3. Service Details
4. Booking Process
5. User Dashboard
6. Profile Management

### Wireframes

![Create account wireframe](https://github.com/user-attachments/assets/97a923fa-d13f-4e3a-8b93-e2145cb527f6)
![My Profile wireframe](https://github.com/user-attachments/assets/4985c489-6445-4da8-a343-e8f94227c715)
![MainPage wireframe](https://github.com/user-attachments/assets/dcd055c7-eb1c-41be-a5fd-d5eac3ee774a)
![login page wireframe](https://github.com/user-attachments/assets/ea3ab44b-2cfa-4149-a580-668de25ed0fc)
![Create Service Listing wireframe](https://github.com/user-attachments/assets/e2dda422-5a1e-427d-8e4f-b1d46f75885e)

## Development Workflow

### Modular Code Architecture
Modular Code Design for 'SkillFlow'
At SkillFlow, we employ a modular code structure, akin to building with LEGO blocks, to ensure flexibility, maintainability, and efficiency throughout our development process. Each part of our system is designed to function independently while integrating seamlessly into the larger framework. This approach enables us to:

#### Enhance Collaboration:
Developers can work on different modules simultaneously without interfering with others. This streamlines teamwork and accelerates development timelines.

#### Simplify Updates and Changes:
By isolating functionality into discrete components, updates or changes can be made to specific modules without impacting unrelated parts of the system. This reduces risk and simplifies the implementation of new features.

#### Facilitate Debugging and Testing:
Modular design allows us to identify, isolate, and resolve bugs more efficiently. Each module can be tested independently, ensuring higher code quality and reliability.

#### Promote Code Reusability:
Common functionalities are encapsulated in reusable components, reducing redundancy and ensuring consistency across the platform.

#### Future-Proof the System:
A modular architecture provides the flexibility to expand or refactor the platform as the needs of our users evolve, ensuring SkillFlow remains robust and adaptable.

#### Code Structure Highlights
- Service-Oriented Modules: Each service (e.g., appointment scheduling, service card posting) is implemented as a separate module to maintain clear boundaries and responsibilities.
- Styling Components: The UI follows a consistent theme, using subdued tones like grey and orangered to enhance user experience while maintaining a professional aesthetic.
- Feature Segmentation: Features such as user profiles and service listings are built independently to allow focused improvements and scalability.

### Building the Login Form Component: Modular Development
• This document outlines our approach to creating the SkillFlow login form by leveraging existing Bootstrap classes and custom CSS from our signup form
• This methodology demonstrates the efficiency of modular development and component reusability in modern web development

##### Development Process

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

##### Benefits of This Approach

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

##### Best Practices Implemented

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

# SkillFlow

## Core Features

### Site Navigation
- **Responsive Navigation Bar**: Dynamically adjusts based on authentication status
- **Dark-themed Modern Interface**: Consistent branding across all pages
- **Mobile-responsive Design**: Ensures functionality across all devices

[![Navbar Logged Out](https://github.com/user-attachments/assets/03b1522c-e5f2-46e6-ad8b-d1cd1160ed31)](#)
[![Navbar Logged In](https://github.com/user-attachments/assets/navbar-logged-in.png)](#)

### User Authentication & Profiles
- **Secure Registration Process**: Easy account creation
- **Customizable User Profiles**: Add personal information and bio
- **Role-based Functionality**: Differentiate between service providers and clients

[![Sign Up Page](https://github.com/user-attachments/assets/signup-page.png)](#)
[![Edit Profile](https://github.com/user-attachments/assets/edit-profile.png)](#)

### Service Management
- **Service Creation & Editing**: Providers can create, edit, and manage service listings
- **Category-based Organization**: Five main categories for easy browsing
- **Detailed Listing Information**: Title, description, hourly rate, and provider details

[![Service Creation](https://github.com/user-attachments/assets/service-creation.png)](#)
[![Service Listings](https://github.com/user-attachments/assets/service-listings.png)](#)

### Appointment Booking System
- **Comprehensive Booking Management**: For both providers and clients
- **Availability Slot Creation**: Providers set their available time slots
- **Real-time Booking Status**: Track pending, confirmed, and cancelled appointments

[![Book Appointment](https://github.com/user-attachments/assets/book-appointment.png)](#)
[![Manage Schedule](https://github.com/user-attachments/assets/manage-schedule.png)](#)

### Service Discovery
- **Interactive Category Filtering**: Browse services by five main categories
- **Detailed Service Cards**: Quick overview of service details
- **Full Service View**: Comprehensive information and booking options

[![Category Filtering](https://github.com/user-attachments/assets/category-filtering.png)](#)
[![Service Details](https://github.com/user-attachments/assets/service-details.png)](#)

### User Experience Features
- **Toast Notifications**: Clear feedback for user actions
- **Dynamic Form Handling**: Real-time character counting
- **Responsive Design**: Optimal viewing on all devices

[![Toast Notifications](https://github.com/user-attachments/assets/toast-notifications.png)](#)
[![Responsive Design](https://github.com/user-attachments/assets/responsive-design.png)](#)

## Key Categories
- **Home Care**: Maintenance and organization services
- **Education**: Tutoring and mentoring opportunities
- **Creative**: Arts and design services
- **Health**: Wellness and fitness support
- **Events**: Planning and coordination assistance

## Future Enhancements
- Advanced search functionality
- Enhanced user profiles
- Expanded service categories
- Integrated messaging system
- Enhanced booking features

### Navigation & Layout
- Responsive navigation bar with dynamic content based on authentication status
- Dark-themed modern interface with consistent branding
- Comprehensive footer with site information, help resources and social media links
- Mobile-responsive design ensuring functionality across all devices

### User Authentication & Profiles
- Secure user registration and login system
- Customizable user profiles with personal information and bio
- Account management features including profile editing and account deletion
- Role-based functionality (service provider vs client)

### Service Management
- Service creation and editing functionality for providers
- Category-based service organization (Home Care, Education, Creative, Health, Events)
- Detailed service listings with title, description, hourly rate, and provider information and email if user has given
- Interactive category filtering system with animated icons

### Appointment/Booking System
- Comprehensive booking management for both providers and clients
- Availability slot creation and management for service providers
- Real-time booking status tracking (pending, confirmed, cancelled)
- Double-booking prevention and conflict management
- Location and time slot specification for services

### Information Architecture
- Clear user feedback system through toast notifications
- Informative error handling and validation messages
- Comprehensive help center with user guides
- Detailed legal information and cancellation policies
- About Us section explaining platform purpose and categories

### Interactive UI Elements
- Dynamic form handling with real-time character counting
- Interactive toast notifications for user actions
- Hover effects for enhanced user interaction
- Responsive buttons and navigation elements
- Clear status indicators for appointments and services

### Service Discovery
- Visual category browsing through intuitive icon-based navigation system
- Filterable service listings by five main categories (Home Care, Education, Creative, Health, Events)
- Service cards displaying key information including:
  - Service title and description
  - Category classification
  - Hourly rate
  - Provider username
  - Booking availability
- Detailed service view pages featuring:
  - Complete service descriptions
  - Provider information
  - Location details
  - Contact information/email (if provided by the provider)
  - Direct booking access

### Landing Page
- Welcome header with platform name
- Platform introduction explaining SkillFlow's community-focused mission
- Five main service categories showcased with icons and descriptions:
  - Home Care (maintenance and organization)
  - Education (tutoring and mentoring)
  - Creative (arts and design)
  - Health (wellness and fitness)
  - Events (planning and coordination)
- Clean, minimalist design with turquoise blue accents
- Responsive layout adapting to different screen sizes

### Service Listings and Details
- Category-based filtering through an interactive icon menu with 5 categories:
  - Home Care (fas fa-home icon)
  - Education (fas fa-book icon)
  - Creative (fas fa-paint-brush icon)
  - Health (fas fa-heart icon)
  - Events (fas fa-calendar icon)
- Service cards displaying:
  - Category label
  - Hourly rate (€/hr)
  - Service title
  - Service description
  - Provider username
  - View More and Book buttons
- Detailed service view showing:
  - Full service information
  - Provider details
  - Contact email (if provided by the service provider)
  - Service creation date
  - Booking options (if not the service provider)

### Navigation
- Category-based filtering
- Responsive design
- Dynamic user menu
- Toast notifications

### Information Pages
- About Us
- Help Center
- Legal Information
- How It Works

### User Account Management

#### User Authentication
- Sign up with username and password
- Login functionality with welcome message
- Secure logout with confirmation
- Password requirements enforcement

#### Profile Management
- Edit personal information:
  - First Name
  - Last Name
  - Email
  - Bio (with 200 character limit)
- Real-time character counting for bio
- Cancel/Save changes options
- Account deletion with double confirmation

#### Service Provider Features
- Create new service listings with:
  - Category selection
  - Title
  - Hourly rate
  - Description (with 500 character limit)
- Manage existing services:
  - Edit service details
  - Delete services
  - View all created services
- Schedule Management:
  - Add available time slots
  - Set service locations
  - Delete unbooked time slots
  - View upcoming appointments

#### Client Features
- View and book available services
- Manage appointments:
  - View pending bookings
  - Cancel bookings
  - See confirmed appointments
  - Track appointment status

#### Navigation
- Dedicated profile dropdown menu with quick access to:
  - Edit Profile
  - My Services
  - Manage Account
  - Appointments

### Site Navigation

#### Main Navigation Bar (Navbar)
- Brand link "SkillFlow" leading to home
- "About Us" quick access link
- Responsive hamburger menu for mobile devices
- Dynamic navigation based on authentication:
  - Non-authenticated users see:
    - Login button
    - Sign Up button
  - Authenticated users see:
    - Home link
    - "+New Post" for creating services
    - Profile dropdown menu
    - Logout button

#### Profile Dropdown Menu
- Edit Profile
- My Services
- Manage Account
- Appointments

#### Category Navigation
- Interactive category icons for filtering services:
  - Home Care
  - Education
  - Creative
  - Health
  - Events

#### Footer Navigation
- About Section:
  - About Us
  - How It Works
- Support Section:
  - Help Center
  - Cancellation Policy
- Legal Section:
  - Terms of Service
  - Privacy Policy
- Social Media Links:
  - Facebook
  - X (Twitter)
  - Instagram
  - LinkedIn

#### Responsive Design Features
- Collapsible hamburger menu on mobile
- Dropdown menus optimized for touch devices
- Responsive content layout
- Consistent navigation across all screen sizes

### Planned Future Features

#### Light and Dark Mode Toggle

 It’ll be super simple to switch between the two modes, depending on what we're feeling. Eventually, we might even make it auto-switch based on system settings or time of day. The idea is to make the app feel more personal and comfy to use no matter where we are. Plus, there could be some customization options in the future.

#### Enhanced User Interaction
- Rating and review system for services
  - Star ratings (1-5)
  - Written reviews with photos
  - Provider response capability
  - Rating verification system
- Direct messaging system between clients and providers
  - Real-time chat functionality
  - File sharing capabilities
  - Message notifications
  - Chat history

#### Payment Integration
- Secure payment processing
  - Multiple payment methods (credit cards, digital wallets)
  - Split payment options
  - Automatic invoicing
  - Refund management
- Service deposits and cancellation fees
- Automated payout system for providers

#### Advanced Search and Discovery
- Smart search functionality
  - Filter by price range
  - Location-based search
  - Availability-based search
  - Skill level filtering
- Advanced category system
  - Sub-categories for specialized services
  - Custom tags for better discovery
  - Related services suggestions

#### Enhanced Booking System
- Recurring appointment scheduling
- Group booking capabilities
- Waiting list functionality
- Automated reminder system
  - Email notifications
  - SMS notifications
  - Calendar integration
- Cancellation/rescheduling automation

#### Profile Enhancements
- Enhanced provider profiles
  - Qualification verification
  - Certificate uploads
  - Portfolio gallery
  - Video introductions
- Social proof integration
  - External reviews integration
  - Social media links
  - Professional certifications display

#### Analytics and Reporting
- Provider dashboard
  - Booking statistics
  - Income tracking
  - Popular time slots analysis
  - Client retention metrics
- Client dashboard
  - Spending analysis
  - Service history
  - Favorite providers
  - Booking patterns

#### Service Enhancement Features
- Package deals and bundles
- Gift card system
- Loyalty program
- Referral system with rewards
- Seasonal promotions management

#### Platform Expansion
- Mobile application development
- Multi-language support
- Accessibility enhancements
- API development for third-party integrations

## Deployment
The deployment section is structured to provide clear instructions for:

### SkillFlow Deployment
1. Environment Setup
2. Django Configuration
3. Database Migration
4. Static Files Configuration
5. Security Settings

### Cloudinary for Media
- Account Setup
- Integration Steps
- Media Management
- Performance Optimization

### Version Control Practices
- Git Workflow
- Branch Management
- Commit Conventions
- Pull Request Process

### Forking the Repository
If you'd like to contribute to the SkillFlow project or use it as a starting point for your own development:
1. Navigate to the [SkillFlow repository](https://github.com/onur-CK/SkillFlow)
2. Click the "Fork" button in the top-right corner of the page
3. Select your GitHub account as the destination for the fork
4. Wait for the forking process to complete
5. You'll now have your own copy of the repository to work with

### Cloning the Repository
To create a local copy of the repository on your machine:
1. Navigate to your forked version of the SkillFlow repository
2. Click the "Code" button and copy the repository URL
3. Open your terminal/command prompt
4. Navigate to the directory where you want to clone the repository
5. Run the command: `git clone [repository URL]`
6. Install the required dependencies using: `pip install -r requirements.txt`
7. Set up your environment variables according to the deployment instructions
8. Run the development server with: `python manage.py runserver`

## Credits and Resources

### Tutorials

The tutorials were used for the purpose of learning and improving understanding, and no use was made of the code content in the tutorials.

- Developing with Django Course by Code Institute
- Principle of Agile Development by Code Institute
- Building with Bootstrap Course by Code Institute
- Database Management Systems Course by Code Institute
- [Bootstrap 5 Crash Course by Traversy Media](https://www.youtube.com/watch?v=4sosXZsdy-s&t=670s)
- 

### Media and Assets
- [Favicon](https://favicon.io/favicon-generator/) 
- [Icons](https://fontawesome.com/icons/moon?f=classic&s=solid)
- 
- 

### Guides and Tutorials

The tutorials were used for the purpose of learning and improving understanding, and no use was made of the code content in the tutorials.

- [CRUD Mastery](https://www.youtube.com/watch?v=pqWyUAT38e0)
- [How to CRUD in Django](https://www.youtube.com/watch?v=opjyyXoqrxg)
- [Complete Django CRUD Operations](https://www.youtube.com/watch?v=N6jzspc2kds)
- [Login, Logout, Signup](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- [Code Institute Readme Tutorial by Kasia Bogucka](https://www.youtube.com/watch?v=l1DE7L-4eKQ)

### Django Documentation
- Django installation: pip install django
- Django version control: python -m django --version
- Creating the project structure: django-admin startproject skillflow .

### Bootstrap Documentation
- Bootstrap Grid System
- Bootstrap Components
- Bootstrap Utilities
- Bootstrap Form Controls

### Learning Platforms and Videos
- YouTube tutorials on Django and Bootstrap integration !!! add the links !!!!!!!!!!!!!!!!!!
- Stack Overflow discussions on booking system implementation
- CSS-Tricks articles on responsive design techniques

### Acknowledgments
We would like to extend our sincere gratitude to:
- My mentor(David Bowers) and my facilitator(Kay Welfare) for their contributions in the process of building my project.
- The Django and Bootstrap development communities for their excellent documentation.
- All contributors(students and tutors) who helped identify and fix bugs during development.

## Technologies Used

### Programming Languages
- Python 3.13.1
- JavaScript
- HTML5
- CSS3

### Frameworks
- Django 5.1.4
- Bootstrap 5.3.3
- Font Awesome 6.4.2

### Database Solutions
- SQLite (Development)

### Media Management Tools
- Cloudinary

### Supporting Libraries and Packages
- Font Awesome
- Django Forms
- Whitenoise

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Chrome DevTools

### Django Documentation
- Django installation: pip install django
- Django version control: python -m django --version
- Creating the project structure: django-admin startproject skillflow .
