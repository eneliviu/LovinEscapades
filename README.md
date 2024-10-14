
# ***<center><font color="red"> LovinEscapades</font>***: The Ultimate Trip Tracking Tool!</center>
## <center> A Django web app </center>

### **Table of content:**
- [Overview](#overview)
- [Application Development](#application-development)
- [Main Features](#main-features)
- [Application Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Accessibility and Design](#accessibility-and-design)
- [Usage and Screenshots](#usage-and-screenshots)
- [Online Validators](#online-validators)
- [Manual Testing](#manual-testing)
- [Unit Testing](#unit-testing)
- [Known bugs and issues](#known-bugs-and-issues)
- [Further improvements](#further-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Documentation version](#documentation-version)


## Overview

***LovinEscapades*** is a web CRUD application developed as part of Milestone Project 4 in the Full Stack Software Development program at Code Institute. This project showcases a complete full-stack Django development approach, utilizing:

- Python with the Django framework
- JavaScript with jQuery
- Custom CSS

In its present form, ***LovinEscapades*** allows registered users to:

- Log in via the `Log In` page using their username and password
- Create, update, edit, and delete information regarding their trips
- Upload and delete photos associated with a particular trip
- Share information about their trips and images with other users or unregistered site visitors
- Post testimonials (upon site admin approval) about their experiences with the site and its community

For site visitors who are not registered users, it is still possible to:

- View shared trip locations marked on a Leaflet map using georeferenced markers
- Navigate to the `Gallery` page via the links in the marker popups
- Send inquiries to the site admin from the `Contact Us` page
- Register on the site from the `Registration` page

Designed with user-friendliness in mind, ***LovinEscapades*** is an intuitive application aimed at helping users maintain focus and boost engagement. It's important to note that this app serves as a demonstration of acquired full-stack programming skills in fulfillment of the requirements of Milestone Project 4, rather than being a final product. 
The project's foundation builds upon the concepts from Milestone Project 2, where I developed a TODO list using a front-end stack.
 

The application can be accessed at [***LovinEscapades***](https://shorturl.at/f4uCn)



### Target Audience

***LovinEscapades*** targets travel enthusiasts and individuals who enjoy documenting and sharing their travel experiences. It appeals to users looking to organize their trips, connect with a community, and explore destinations through shared content. Designed with simplicity in mind, the platform suits both tech-savvy individuals and those new to online travel documentation, providing an intuitive space for managing itineraries and memories. The app is designed to accommodate a diverse user base, embracing individuals from varied geographic locales, cultures, and backgrounds globally, fostering a rich exchange of experiences and perspectives.


## Application development
The development of the ***LovinEscapades*** application followed an iterative approach, incorporating essential Agile principles. However, as I was still familiarizing myself with Agile methodologies, I found these principles challenging to follow consistently.

Much of the development process was guided by a trial-and-error approach, as I initially lacked a clear vision of the project content. Despite these challenges, I focused on implementing a select number of user stories to ensure progress.

The user stories were crafted using a custom template, structured as follows::

*<center>**Title:***</center>

*<center>**Description:***</center>
*<center>As a **[role]** I can **[capability]** so that **[received benefit]***</center>

*<center>**Acceptance Criteria:***</center>
*<center>Acceptance Criteria 1:*</center>
*<center>Acceptance Criteria 2:*</center>
*<center>Acceptance Criteria 3:*</center>

Key user stories that influenced development included:
- As a site visitor, I can register for an account or log in to an existing one, so I can access personalized features and services.
- As a registered user, I want the ability to create, edit, and delete a trip record.
- As a registered user, I can create and share my trip, allowing me to document my travel experiences and share them with others.
- As a site visitor, I want a view of shared trip locations and photos.

All the `User Stories` labeled in the `must have` category were fulfilled by the time of project submission.

![Main menu](static/docs/Kanban.webp#center)
*<center><font color="red">LovinEscapades</font>: Github Kanban baord with project User stories*.</center><br>

![Main menu](static/docs/Kanban_detail.webp#center)
*<center><font color="red">LovinEscapades</font>: Custom template for User Stories*.</center><br>

During development, I encountered numerous bugs and conducted extensive code refactoring to adhere to the DRY (Don't Repeat Yourself) principle. Frequent Git commits were made throughout the process to ensure consistent progress tracking and effective version control.


[*Back to top*](#)


## Main Features

### **User Registration and Authentication:**
- Secure user registration and login system.
- Automatically creates a User Profile instance for new registrations.
- Allows registered users to follow others, currently accessible only via the admin page.

### **Trip Management:**
- Create, update, and delete trip entries with descriptions, locations, and dates.

### **Photo Gallery:**
- Upload and manage photos linked to each trip.
- Browse a gallery of all trip-related photos.

### **Interactive Map:**
- Show trip locations on a Leaflet map with markers.
- Connect map markers to trip details and photo galleries.

### **User Testimonials:**
- Submit testimonials on site experiences, pending admin approval.

### **Contact Form:**
- Contact page for user inquiries and feedback to site admin.

### **Error Handling:**
- Provides a smooth user experience by handling errors gracefully and delivering helpful messages.

### **Responsive Design:**
- Fully responsive design for seamless use across different devices and screen sizes.

### **Cross-Platform Accessibility:**
- Usable on any device with an internet connection, including mobile, tablet, and desktop.

### **Security:**
- Secures actions for logged-in users using `@login_required`.
- Utilizes the `AllAuth` extension for safe user registration and login.
- Limits access to sensitive information to authorized users, like site admins and data owners.

These features highlight the core functionalities of ***LovinEscapades***, showcasing its capabilities for user interaction, content management, and community engagement. 
More details about the app functionality are provided in the [Usage and Screenshots](#usage-and-screenshots) section.


[*Back to top*](#)


## Project structure

### ***Lovingescapades*** project consists of four apps:

### 1. `trip`
This app features the `Dashboard` page, allowing users to:
- View updated counts of trips, uploaded photos, and testimonials awaiting approval.
- Decide if new trip information will be shared publicly or kept private. Public trips are mapped on the landing page, while private trips are visible only to the authenticated user.
- Quickly access trip details through trip card elements, which provide basic trip information (destination, start and end dates, creation date) along with options to edit/delete trips and upload/delete photos.
- Display approved user testimonials on the landing page and map the locations of shared trips.  

### 2. `user_profile`
The user profile app offers two primary sections:
- Profile update section for editing basic user information such as username, first and last name, and email address.
- Functionality for posting and deleting testimonials, which are subject to admin approval before appearing on the landing page.  

### 3. `contact`
This app provides essential functionality for site visitors to send inquiries to the site admin via a dedicated form.

### 4. `gallery`
- Hosts the photo gallery where all publicly shared photos by registered users can be viewed by any visitor.
- Users can publish photos even if they choose not to make the associated trip information public.
- Each photo in the gallery includes a like icon and basic trip details, though the feature for sending and receiving likes has not been implemented yet.


[*Back to top*](#)


## Technologies Used

### **Django Web Framework:** 
- A web framework made with Python that helps build web apps quickly and efficiently. It's great for managing databases and organizing code, making it easier to create complex features for ***LovinEscapades***.

### **JavaScript:** 
- A programming language that makes web pages interactive. It's used to add features like real-time updates and dynamic content that responds to user actions.

### **jQuery:**
- A Javascript library that makes it easier to use JavaScript. It simplifies tasks like handling mouse clicks or animations, making the site more user-friendly. The JQuery was included in the project via a Content Delivery Network (CDN) link. 

### **Bootstrap 5.3 CSS:** 
- A toolkit for building websites that look good on all devices. It comes with ready-to-use designs, which help in quickly creating a clean and modern interface for the app. Boostrap library was included in the project via CDN link. 

### **Custom CSS:** 
- Styles written specifically for ***LovinEscapades*** to personalize the look of the site, ensuring it matches the overall theme and design vision.

### **Leaflet JavaScript mapping library:** 
- A tool for creating interactive maps that work well on different devices. It helps users see trip locations and explore the map easily.

### **Geopy Python Module:** 
- A library that helps find geographic coordinates, like latitude and longitude, from place names. It’s used to show trip locations accurately on the map.

### **Django graph models:** 
- [Django Extensions](https://shorturl.at/GxkSs) is a collection of custom extensions for the Django Framework that can be used for creating ER (Entity-Relationship) diagrams for the project database. These diagrams make it easier to visualize, understand, and manage the database structure. You can view these database model relationships using the online [GraphViz generator](https://shorturl.at/AAuhy). 

### **Python modules**
The following Python modules were installed using the `pip install` command in the terminal and were listed in the `requirements.txt` file:
- asgiref==3.8.1 
- cloudinary==1.36.0 
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.16
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-extensions==3.2.3
- django-filter==24.3
- geographiclib==2.0
- geopy==2.4.1
- gunicorn==20.1.0
- oauthlib==3.2.2
- pillow==10.4.0
- psycopg2==2.9.9
- PyJWT==2.9.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- urllib3==1.26.20
- whitenoise==5.3.0

### **Javascript libraries**
- Leaflet 1.9.4 ([JavaScript library for mobile-friendly interactive maps](https://leafletjs.com/index.html))

### **Markdown**
- The Markdown formatting for README.md and HELP.md files was done according to the documentation provided at
[www.markdownguide.org](https://www.markdownguide.org/basic-syntax/).

### Cloudinary serving
- The static assets (images in our case) are served using Cloudinary's capabilities

### Cloud deployment
- The app is currently deployed on [Heroku Cloud Application Platform](https://www.heroku.com)
- For cloud deployment, the [dependency requirements file](requirements.txt) was compiled using the following command in the VSCode terminal: 
```
pip freeze --local > requirements.txt
```
 
- The processes to run on the Heroku platform are specified in the `Procfile` file. 
- Sensitive information is stored in the `env.py` file, which is listed in the `.gitignore` to prevent it from being uploaded to GitHub.
- The app can be accessed at [***LovinEscapades***](https://shorturl.at/f4uCn).

### Local deployment
- For development or deployment on a local development, the web server can be started using the terminal command:

```
python manage.py runserver
```

[*Back to top*](#)


## Accessibility and Design

### Accessibility
- Attention was given to the ARIA (Accessible Rich Internet Applications) content, ensuring that screen readers can effectively retrieve information when needed.

### Fonts
- The font 'Lato' was chosen for the logo and related statement text. It is both legible and adds a rough, gritty   texture, breaking the clean visual of the site.
- The font 'Roboto' was used for general text, both offering a clean and easily readable appearance.

### Colors and Themes
- The website’s style is minimalistic, primarily based on predefined Bootstrap 5.3 themes and touches of custom CSS. This approach ensures good contrast and a decent aesthetic, supporting accessibility and visual appeal.

### Icons
- Font Awesome were used for the Logo, social media icons in the Footer, `My profile`-page link and like buttons on share photos in the `Gallery`-page. 

[*Back to top*](#)


## Usage and Screenshots

### Responsive design
- The 
![Main menu](static/clips/Responsive_large_screen.webp#center)
*<font color="red">LovinEscapades</font>: Responsive design: large screen*.<br>


![Main menu](static/clips/Responsive_tablet_phone.webp#center)
*<font color="red">LovinEscapades</font>: Responsive design: tablet and mobile phone*.<br>


### User Registration

- The site visitor must fill in a standard registration form:

![Main menu](static/clips/User_registration_form.webp#center)
*<font color="red">LovinEscapades</font>: Responsive design: tablet and mobile phone*.<br>

- The user instroduces username, email and a strong password
![Main menu](static/clips/User_registration_form_fill.webp#center)
*<font color="red">LovinEscapades</font>: Responsive design: tablet and mobile phone*.<br>

- If the registration is successful, the user is redirect to the home page and a success message is posted.
- For logged-in users, the Registration navbar menu is not visible anymore, and the 'My profile'- page with a user icon appears on the right side of the navbar.
- Authenticated users can navigate to the Dashboard page

![Main menu](static/clips/User_registration_logged.webp#center)
*<font color="red">LovinEscapades</font>: Responsive design: tablet and mobile phone*.<br>


### User Dashboard
- The Dashboard offers CRUD fuctionality for managing trips and images

![Main menu](static/clips/Dashboard_clean.webp#center)
*<font color="red">LovinEscapades</font>: Dashboard page*.<br>

#### **Create new trip**
- On the Dashboard, the stats are null and the user can create a new trip record by clicking on the 'Add new trip' button to open an empty form in a Bootstrap modal.
- By design, all form fields are required

![Main menu](static/clips/Add_new_trip_start.webp#center)
*<font color="red">LovinEscapades</font>:Add new trip form*.<br>

- Using Javascript, the date picker entries are corroborated in real-time to the Trip status category (Completed, On-going and Planned) to avoid erroneous choices and to increase the UX. The eventual error are shown in browser alerrs, and the user can chose other entries accordingly. 
- On the backend, the date entries are checked against those form other planned trips to eliminate possible collusions. There errors are hadled by Python logic in `trip.views.py`, and a Django error message is sent if necessary.



![Main menu](static/clips/Add_trip_Completed_error.webp#center)

*<font color="red">LovinEscapades</font>: Add new trip form: date choice missmatch for COMPLETED trips*.<br>



![Main menu](static/clips/Add_trip_Planned_error.webp#center)

*<font color="red">LovinEscapades</font>: Add new trip form: date choice missmatch for PLANNED trips*.<br>

- After a new trip is created and posted as a trip card containg basic trip info  
- Django success message is sent to the user.
- The Dasboard is paginated such that it can handle a large number of trip instances 



![Main menu](static/clips/Add_new_trip_success.webp#center)

*<font color="red">LovinEscapades</font>: Add new trip form: correct date choice for ON-GOING trips*.<br>

- The created trip, if the shared choice is `YES`, it will be sent to the Leaflet map on the landing page. By clicking on the marker, trip information and a redirecting link appear in a tooltip while the map zooms in at the marker location
- The coordinates are calculated using the `geopy` Python module that uses the trip destination (Place and Country) to localize and retrieve the Longitude and the Latitude for mapping the location.
- Although the form does not show the coordinates fields when creating a new trip, these fields exist and are populated when the coordinates are saved.  
- If the location cannot be geolocated, a Django error message is sent to the user.  


![Main menu](static/clips/Add_new_trip_on_map.webp#center)

*<font color="red">LovinEscapades</font>: Add new trip form: correct date choice for ON-GOING trips*.</center><br>


![Main menu](static/clips/Add_new_trip_on_map_tooltip.webp#center)

*<font color="red">LovinEscapades</font>: Add new trip form: correct date choice for ON-GOING trips*.<br>

#### **Managing trips**
- After a  new trip is created, the dashboard stats are updated accordigly



![Main menu](static/clips/Dashboard_update_stats.webp#center)

*<font color="red">LovinEscapades</font>: Trip card with CRUD functionalitys*.<br>

- The trip cards have CRUD functionality for editing trip data and uploading photos.


![Main menu](static/clips/Trip_card.webp#center)

*<font color="red">LovinEscapades</font>: Trip card with CRUD functionalitys*.<br>

- By clicking on the `Update` button, the user is directed to a page containing two choices: 
    - `Update trip` for changing the trip info.
    - `Upload photo` for uploading trip photos.



![Main menu](static/clips/Update_trip_page.webp#center)

*<font color="red">LovinEscapades</font>: Trip card with CRUD functionalitys*.<br>

- Selecting `Update trip` opens the create trip form with all fields filled in, such that the user can modify and save the new trip information.


![Main menu](static/clips/Edit_trip_form.webp#center)

*<font color="red">LovinEscapades</font>: Edit trip page*.<br>

- Selecting `Update photo` option opens a form for loading photos.
- All form fields are mandatory and must be non-empty.
- Constraints on min and max text length are in place using Django Validators.
- After upload, a success message is sent to the user.
- If the user chooses to share it, then the photo is also sent to the `Gallery`-page.



![Main menu](static/clips/Upload_photos_form.webp#center)

*<font color="red">LovinEscapades</font>: Upload photo form*.<br>



![Main menu](static/clips/Upload_photo_success.webp#center)

*<font color="red">LovinEscapades</font>: Upload photo success*.<br>

- After image upload, the stats on the dashboard are updated accordingly


![Main menu](static/clips/Dasboard_stats_1_photo_1_trip.webp#center)

*<font color="red">LovinEscapades</font>: Updated dashboard with trip and photo added*.<br>

- The user can access the uploaded photo using the `Photos` button on the trip card to navigate to a `details<image_id>` URL that opens a masonry gallery of image cards. 



![Main menu](static/clips/User_trip_photo.webp#center)

*<font color="red">LovinEscapades</font>: Gallery page with shared photo*.<br>

- Shared photos can be seen by any site visitor on the `Gallery`-page.


![Main menu](static/clips/Gallery_shared_photo.webp#center)

*<font color="red">LovinEscapades</font>: Gallery page with shared photo*.<br>

- Each photo can be individually deleted form the  `details<image_id>`



![Main menu](static/clips/Delete_photo.webp#center)

*<font color="red">LovinEscapades</font>: Delete photo modal confirmation*.<br>

- After the photo is being deleted, the user is redirected to Dashboard and a Django success message is sent to the user.
- The stats on the Dashboard are updated accordingly



![Main menu](static/clips/Delete_photo_success.webp#center)

*<font color="red">LovinEscapades</font>: Delete photo success message and updated dashboard stats*.<br>

### Manage the user profile
- Initially, the user profile contains only the username and email address that are required 
    by the registration process, but the fields for first and last name are empty.


![Main menu](static/clips/User_profile_clean.webp#center)

*<font color="red">LovinEscapades</font>: User profile page*.<br>

- The `Update` button opens a form for updating the user information



![Main menu](static/clips/Update_user_profile.webp#center)

*<font color="red">LovinEscapades</font>: Update user profile form*.<br>

- After submitting the form, the user is redirected back to `My Profile`-page where the personalia has been updated



![Main menu](static/clips/Update_user_profile_success.webp#center)

*<font color="red">LovinEscapades</font>: Update user profile form*.<br>

- The user can post testimonials to the landing page using the 'New testimonial' button



 ![Main menu](static/clips/Testimonials_form.webp#center)

*<font color="red">LovinEscapades</font>: Post testimonial form*.<br>

- After submitting the testimonial, the user is redirected to `My Profile`-page where the post is loaded and pending approval. 



 ![Main menu](static/clips/Testimonials_success.webp#center)

*<font color="red">LovinEscapades</font>: Posted testimonial*.<br>



 ![Main menu](static/clips/Testimonial_admin.webp#center)

*<font color="red">LovinEscapades</font>: Testimonial pending approval on admin page*.<br>



 ![Main menu](static/clips/Testimonial_approved.webp#center)

*<font color="red">LovinEscapades</font>: Approved testimonial on admin page*.<br>



 ![Main menu](static/clips/Testimonial_approved_user_profile.webp#center)

*<font color="red">LovinEscapades</font>: Approved testimonial on admin page*.<br>

- The `Dashboard`-page has also been udated with a new testimonial post


 ![Main menu](static/clips/Dashboard_trip_testimonial_approved.webp#center)

*<font color="red">LovinEscapades</font>: Updated dashboard page with trip and approved testimonial*.<br>

- After approval, the testimonial is posted on the landing page


 ![Main menu](static/clips/Landing_page_with_testimonial.webp#center)

*<font color="red">LovinEscapades</font>: Updated dashboard page with trip and approved testimonial*.<br>



- Deleteing a trip will remove all the linked trip photos as well
- The dasboard stats and the landing page map are also updated  

 ![Main menu](static/clips/Example_two_trips_two_photos.webp#center)

*<font color="red">LovinEscapades</font>: Updated dashboard page with trip and approved testimonial*.<br>

 ![Main menu](static/clips/Map_two_trips.webp#center)

*<font color="red">LovinEscapades</font>: Updated map with new trip marker added*.<br>

 ![Main menu](static/clips/Delete_trip.webp#center)

*<font color="red">LovinEscapades</font>: Delete trip and associated photo*.<br>


 ![Main menu](static/clips/Delete_trip_success.webp#center)

*<font color="red">LovinEscapades</font>: Delete trip and associated photo*.<br>

 ![Main menu](static/clips/Map_one_trip_after_delete.webp#center)

*<font color="red">LovinEscapades</font>: Delete trip marker from map after trip deletion*.<br>


[*Back to top*](#)


#### **Managing site admin inquiries**

 ![Main menu](static/clips/Contact_us_form.webp#center)

*<font color="red">LovinEscapades</font>: Form for sending inquiries to site admin*.<br>


 ![Main menu](static/clips/Contact_success.webp#center)

*<font color="red">LovinEscapades</font>: Inquiry successfully sent to site admin*.<br>


 ![Main menu](static/clips/Inquiry_to_site_admin.webp#center)

*<font color="red">LovinEscapades</font>: Inquiry successfully sent to site admin*.<br>


 ![Main menu](static/clips/Inquiry_to_site_admin_read.webp#center)

*<font color="red">LovinEscapades</font>: Inquiry successfully sent to site admin*.<br>


[*Back to top*](#)

#### **Managing photo gallery page**

- The `Gallery`-page contains all the photos sahred by the user. 
- A user can choose to share a photo, but not to make the entire trip public.
- Deleting a trip will delete also the associated photos from the `Gallery`-page



 ![Main menu](static/clips/Shared_gallery.webp#center)

*<font color="red">LovinEscapades</font>: Inquiry successfully sent to site admin*.<br>


[*Back to top*](#)


## Database schema

The Entity Relationship Diagram (EDR) for the full project database shcema was produced using the 
[Graph models extention](https://shorturl.at/psHzX) and visualized using the online [GraphViz generator](https://shorturl.at/AAuhy). 



![Main menu](static/docs/graphviz_all_models.webp#center)

*<font color="red">LovinEscapades</font>: EDR project database diagram*.<br>


## Online Validators

### **PEP8**
The [Pep8 CI](https://pep8ci.herokuapp.com/) Python Linter returned no errors:

| App            | File         | CI Linter Result           |  Status |
| --- | --- | --- | --- |
| `trip`         | `forms.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `filters.py` | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `models.py`  | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `utils.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `urls.py`    | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `views.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `contact`      | `forms.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `models.py`  | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `urls.py`    | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `views.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `gallery`      | `forms.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `models.py`  | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `urls.py`    | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `views.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `user_profile` | `forms.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `models.py`  | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `urls.py`    | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
|                | `views.py`   | All clear, no errors found | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|

---

### **JSHint**
The [JSHint](https://jshint.com/) validator flagged two warnings across all JavaScript files concerning the use of Bootstrap 5.3 modals and Leaflet `L` objects.


![Main menu](static/docs/JSHint.webp#center)

*<font color="red">LovinEscapades</font>: JSHint validator results*.<br>

### **Lighthouse**
The Lighthouse validator showed very good results, with an warning related to a Leaflet internal issue. 


![Main menu](static/docs/Lighthouse_navtest.webp#center)

*<font color="red">LovinEscapades</font>: Lighthouse navigation test*.<br>


![Main menu](static/docs/Lighthouse_snapshot_test.webp#center)

*<font color="red">LovinEscapades</font>: Lighthouse snapshot test*.<br>


### Jigsaw CSS Validator

The Jigsaw CSS Validator reported no errors for the custom CSS.

![Main menu](static/docs/W3C-CSS-CustomCSS.webp#center)

*<font color="red">LovinEscapades</font>: Jigsaw CSS Validator test for custom style*.<br>

However, it identified two errors in the Leaflet CSS, both related to Leaflet specifically:

![Main menu](static/docs/W3C-CSS-Errors-URL.webp#center)

*<font color="red">LovinEscapades</font>: Jigsaw CSS Validator test errors*.<br>

Upon further investigation using [caniuse.com](https://caniuse.com), it was confirmed that `plus-lighter` is a valid value for the `mix-blend-mode` property.

![Main menu](static/docs/CANIUSE_plus-lighter.webp#center)

*<font color="red">LovinEscapades</font>: Lighthouse snapshot test*.<br>

For the second error, no relevant results were found, and I am unable to provide an explanation or a fix.

![Main menu](static/docs/CANIUSE_behaviour.webp#center)

*<font color="red">LovinEscapades</font>: Lighthouse snapshot test*.<br>


### Web Accessibility Evaluation Tool (WAVE) 

The WAVE Tool reports no errors but does issue an alert.

![Main menu](static/docs/WAVE_test.webp#center)

*<font color="red">LovinEscapades</font>: WAVE accessibility test*.<br>


Upon investigating further, it suggests that both the site logo and the "Home" navbar element have the same link pointing to the homepage. I have not addressed this alert because having multiple links leading to the home page is a common practice and does not typically impede navigation or accessibility.

![Main menu](static/docs/WAVE_test_alert.webp#center)

<font color="red">LovinEscapades</font>: WAVE accessibility test alert*.<br>

Finally, the WAVE contrast check test also passes successfully.

![Main menu](static/docs/WAVE_test_contrast.webp#center)

<font color="red">LovinEscapades</font>: WAVE contrast test*.<br>


### W3C Markup Validation Service

The W3C HTML Validator displays parsing errors because of the Django Template Language. Attempting to find alternative validators online didn't yield any viable solutions. I'm open to suggestions on how to address this issue.


![Main menu](static/docs/NU_HTML_checker.webp#center)
 
*<font color="red">LovinEscapades</font>: W3C HTML Validator partial results*.<br>


## Manual Testing

- Manual testing primarily concentrated on interacting with the forms to ensure users received appropriate feedback after submission. 
- The default `clean()` and `save()` methods of the model form class were overridden as necessary to implement specific validations.

- Emphasis was placed on real-time user feedback during form completion.
- Fields were designed to provide immediate alerts for incorrect inputs.
- Some form fields were configured with predefined choices to minimize input errors.

- Despite these measures, certain errors might still occur, such as:
    - Selecting inappropriate trip dates that don't align with the trip status, like planning a trip with past dates.
    - Overlapping dates when creating a new trip that conflict with previously created trips.   



| Feature | Expected behaviour | Test | Status |
| --- | --- | --- | --- |
| `User registration` | **New user can register**
| &nbsp;&nbsp;- *Username validation* | Accept a valid username | Non-empty string | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Username validation* | Accept a valid password | Strong password |![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Redirect to dashboard* | Innloged user redirected to user dashboard | Successful navigation (200 status code) |![warning](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success message* | Returns Django messsage for successful login | Green message box on screen |![warning](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `User login` | **User information retrieved, user can login**
| &nbsp;&nbsp;- *Username validation* | Valid username | Can login with corrent user name | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Password validation* | Valid password | Can login with correct password | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Redirect to home address* | Redirect | User redirected to home after registration |![warning](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success message* | Returns messsage for successful login/registration | Green message box on screen |![warning](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Welcome message* | Dispalys username and welcome message | Green message box on screen |![warning](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Create new trip` | **Authenticated users can create a new trip**
| &nbsp;&nbsp;- *Select time intervals* | Start date less or equal to end date | Type wrong dates combinations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Completed trips cannot be in the future | Type wrong dates combintations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Planned trips cannot be in the past | Type wrong dates combintations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Ongoing trips must contain the current date | Type wrong dates combintations | ![alert](https://via.placeholder.com/10/E54151?text=+) `alert`|
| &nbsp;&nbsp;- *Success messages* | Create/delete trips must return a message to the user | Create and delete trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Edit trip` | **Modify an existing trip**
| &nbsp;&nbsp;- *Select time intervals* | Start date less or equal to end date | Type wrong dates combinations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Completed trips cannot be in the future | Type wrong dates combintations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Planned trips cannot be in the past | Type wrong dates combintations | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Select time intervals* | Ongoing trips must contain the current date | Type wrong dates combintations | ![alert](https://via.placeholder.com/10/E54151?text=+) `alert`|
| &nbsp;&nbsp;- *Success messages* | Create/delete trips must return a message to the user | Create and delete trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Change title* |  Title non-empty, min 100 char | Enter title with different  lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Change place* | Place non-empty, min 2 char | Enter place names with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Change country* | Country non-empty, 2-56 chars | Enter country names with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | Edit trips must return a message to the user | Edit trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Map the shared trips * | Shared trips must be mapped | Create trips with/without sharing rights | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Delete trip` | **Modify an existing trip**
| &nbsp;&nbsp;- *Remove trip and associated phots* | Deleting a trip must remove all associated photos | Create/delete trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Remove trip and map markers* | Deleting a trip must remove all associated map markers | Create/delete trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | Removing trips must return a message to the user | Remove trips | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Upload/Delete photos` | **An image can be uploaded to the site**
| &nbsp;&nbsp;- *File type* | Only valid image files can be uploaded | Upload wrong file types | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Title length* | Title between 2-50 chars | Enter photo titles with different lengths  | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Description length* | Photo description 2-500 chars | Enter photos descriptions with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Upload shared photos ti gallery* | Shared photos must be uploaded to Gallery | Upload photos with/withoud sharing rights | ![alert](https://via.placeholder.com/10/E54151?text=+) `alert`|
| &nbsp;&nbsp;- *Delete photo* | Upload/delete photos must return a message to the user | Uploade/delete photos | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | Upload/delete photos must return a message to the user | Uploade/delete photos | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Post testimonials` | **An authenticated user can be post a testimonial**
| &nbsp;&nbsp;- *Create testimonial* | A post should contain vaild text 2-50 chars | Enter posts with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Testimonial on the landing page* | Approved testimonials should be posted on the lading page | Create and approve posts | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Delete testimonial* | Users can delete their own testimonials | Add and delete testimonials | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | Add/delete testimonials must return a message to the user | Uploade/delete testimonials | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Send inquiries` | **A site visitor can send an email to site admin**
| &nbsp;&nbsp;- *Valid sender name* | Sender name of 2-100 chars | Enter sender names with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Valid message* | A message text of 50-500 chars | Enter messages with different lengths | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Admin can receive message* | The messages are visible on the admin page | Send inquiries | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Admin can approve message* | The admin can approve a message on admin page | Send inquiries | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | Sent inquries must return a message to the user | Send inquiries | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Create user profile` | **A profile table shoukd be created when a user registers to the site**
| &nbsp;&nbsp;- *User Profile in the admin page* | Profile can be accessed by the admin | Create new users and check the admin page | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *User Profile can be deleted* | Deleting users removes the profile from admin | Delete User from the admin | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *A users can follow other users* | Can select one or mores users to follow from the admin page| Follow/unfollow users | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Edite user profile` | **A user can edit his profile data**
| &nbsp;&nbsp;- *User can change/remove name* | User can chose what personal data to display | Add and remove user names | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *User can modify email address* | User can change email address, but a valid email is mandatory have | Edit email address | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Success messages* | User receives a meaasge after editing the profile | Edit profile items | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| `Leaflet map` | **A user map shared trips and; the map has basic filtering options**
| &nbsp;&nbsp;- *Shared trip location is mapped correctly* | User can find the correct trip destination on the map | Add many destinations | ![alert](https://via.placeholder.com/10/E54151?text=+) `alert`|
| &nbsp;&nbsp;- *Filter trips* | User and site visitors can filter trips | Use different entries for place, country, category and trip status  | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Filter success* | The filter retrieves the correct trips | The right trips are mapped | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|
| &nbsp;&nbsp;- *Error messages* | User receives an error messasge if no match is found | Use different entries for place, country, category and trip status | ![pass](https://via.placeholder.com/10/00FF00?text=+) `pass`|


---

### Unit Testing 

I  run automatic testing for the simplest case - i.e. the ContactForm `contact` app with the command

```
python3 manage.py test contact
```

and I got the following error:
`django.db.utils.OperationalError: near "None": syntax error`

The error occured when running unit testing with all apps, and I have tried to redo the database migrations, but it didn't work. 
For the time being, I am open for suggestions.


### Additional testing

#### Devices and browsers
Additional testing was performed by calling the application from my private devices operating on Windows 11 (desktop and laptop), as well as
on my smartphone (Samsung Galaxy S21) operating on Android OS, using the following web browsers:
- Google Chrome: Version 129.0.6668.100 (Official Build) (64-bit)
- Brave: version 1.70.126 Chromium: 125.0.6422.112 (Official Build) (64-bit)
- Microsoft Edge: Version 129.0.2792.89 (Official build) (64-bit)


[*Back to top*](#)

## <font color="red">Known bugs and issues</font>
- There is a **Javascript error** that occurs when creating trips with the `Ongoing` status. I don't know if it is a logical error or a coding error, but I suspect that the inclusion of the javascript tags onto the Django templates may not be quite right.
- Mapping remote, exotic or uncharted locations can fail sometimes due to the limitations of the gelocation services
- The geolocator cannot deal with places having similar names, so a more sophisticated logic must be implemented for selecting the right one. 

If you encounter other bugs, please create an issue by clicking [here](https://github.com/eneliviu/LovePlanningCLI/issues).


[*Back to top*](#)


## Further improvements
- Refactor the Javascript functions 
- Refactor the delete functions since there is quite a bit of overlap between them.
- Functionality to reply to user inquiries send through the form on the Contact Us page
- Filter and sort options to organize and view the trips and photos according to more detailed criteria.
    - Add a day-time picker to improve the map filter
    - Add separate filter for the image gallery page
    - Add separate filter for dashboard page
- Reminders
    - Set due dates with automatic reminder to receive timely notifications for upcoming trips and deadlines.
- Social Sharing:
    - Share trip experiences and images with other users and visitors.
    - Comment and interact on shared trip entries.


[*Back to top*](#)


## Contributing

### To contribute to the ***LovinPlans*** project:
- Fork the repository on GitHub to create your own copy.
- Clone the forked repository to your local machine.
- To fork the project:
    - Click the "Fork" button on the top-right corner of the repository page
    - Clone Your Fork by running the following command in the terminal or command prompt:
        `git clone https://github.com/your-username/repository-name.git`
- Make your desired changes, whether it's fixing a bug, adding a feature, or updating documentation.
- Commit your changes with clear messages.
- Push your commits to your forked repository on GitHub.
- Submit a pull request detailing your changes and their benefits.

[*Back to top*](#)

## License
### Open Source
As an open-source project, ***LovinEscapades*** promotes transparency and community involvement. The code is accessible on GitHub, allowing developers to view, fork, and contribute to the project as they desire.


[*Back to top*](#)


## Acknowledgements
- Further details on the usage of Leaflet JS were obtained from https://leafletjs.com/
- [`BugBytes` Youtube channel](https://www.youtube.com/watch?v=qzrE7cfc_3Q) for using Django Graphs and great short examples of using extensions
- [`BugBytes` Youtube channel](https://www.youtube.com/watch?v=E2bhoCOMlsA&t=44s) for the Django - Leaflet integration idea  
- [Pagination with Django](https://djangocentral.com/adding-pagination-with-django/#adding-pagination-using-function-based-views)
- [On handling multiple forms on the same template](https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django)
- [Codemy Youtube channel](https://www.youtube.com/watch?v=H8MmNqDyra8&list=PLCC34OHNcOtoQCR6K4RgBWNi3-7yGgg7b&index=3) for automatically creating profile pages
- `ChatGPT` was utilized to generate sensible input for text content, assist in crafting the README file, and perform language proof-checking.

    
[*Back to top*](#)


## Documentation version

Last updated: Oct 14, 2024

[*Back to top*](#)