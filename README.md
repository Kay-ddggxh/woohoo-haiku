# Woohoo Haiku

This Django project is a little poetry blog that can turn into a call-and-response game through user interaction. The main value in it lies to provide fun to those who enjoy poetry, haiku or just playing with words.
Much like a regular blog site, a registered user can submit posts, like and comment on other users' posts. However, the posts and comments are meant to follow the [Haiku/Tanka format](https://poetry4kids.com/lessons/how-to-write-a-tanka-poem/). Thus, the original post will be a haiku. Other users can then add two more lines to extend it into a tanka, whilst trying to capture and maintain the feel of the original post and understand the authors subject and intent.

![responsive mockup](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670925613/woohoo_haiku/images/readme/mockup.png)

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## Table of Contents

- [UI/UX](#uiux)
    - [Agile](#agile)
    - [Wireframes](#wireframes)
    - [Site Goals](#site-goals)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)
    
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)
   
- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [CRUD](#crud)

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [External Libraries](#external-libraries-and-applications)
    - [Database](#database) 

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    

## UI/UX

The overall design of the site is based on the Japanese principle of minimalism and therefore doesn't include a lot of visual variants and distractions.

The general layout, navigation and functionality is plain and intiutive, meeting a user's expectation of any standard blog site.

Features and interactivity are kept to a minimum, as to not overwhelm the user with too many options and to maintain a zen like usage of the site.


### Agile

This project was designed and built using the agile approach. Right from the initial planning through to final development. To help visualise the process I created a [GitHub project](https://github.com/users/Kathrin-ddggxh/projects/6) and utilised the provided Kanban board method to split project elements into user stories and manageable tasks.

To view all user stories including their required acceptance criterias and tasks, refer the project linked to above.
Each story also has been tagged with a label to signify how crucial a particular feature is to the overall workings and acceptability of the site.

### Wireframes

The initial [wireframes in Figma](https://www.figma.com/file/Ajb5EOJLJedDc0v8a0wL67/Woohoo-Haiku) are an overly simplified version of the finished product and merely served the purpose of listing most of the site's essential features.

Not all features and functions are covered by these first drafts. For a full list of existing features see [Features](#features)

<details>
    <summary>
        Wireframe images
    </summary>
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/home.jpg" alt="home-wireframe">
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/read-haiku.jpg" alt="haiku-wireframe">
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/browse.jpg" alt="browse-wireframe">
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/create.jpg" alt="create-wireframe">
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/login.jpg" alt="login-wireframe">
    <img src="https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/signup.jpg" alt="signup-wireframe">
</details>

### Site Goals

The goal of this site is to provide the user with a very simple haiku sharing platform. User actions are delibertately limited. For example, the commenting is restricted (by admin approval) to only submit a tanka as extension of the original haiku post. This way it eliminates grounds for discussion and animosity - there are plenty of other sites out there to fulfill those needs. By the same token, there a no options to share on social media or links to any commercial sites encouraging consumerism.
The online world also provides enough sensory overload as it is. Therefore the site does not make use of audio or too many varying images. However, both those could be considered during future development, provided it's in keeping with the site's sense of simplicity (see [Future Features](#possible-future-features)).
To conlcude, the site is intended to foster calm and focus by letting the user get creative with words - nothing else.

### 5 Planes of UX

#### Strategy

Addresses user's needs and product objectives.
For this project, it was more a case of *un-addressing* the needs the rest of the web tries to meet - no buying-selling, no social media, no discussions and no excessive visual feed.
The objective lies in creating a calm, creative space. Browsable content is kept on one simplistic level.

#### Scope

Addresses what functions and features are within the scope of the project.
Minimal functionality was key to this project. This means that most features included are a basic requirement. Features like user sign up and login had to be implemented, as well as basic CRUD funtionality for authenticated users. For detailed explanation of all existing features see [Existing Features](#existing-features).
Futures discussed under [Future Features](#possible-future-features), while still within the possible scope of this project, were deemed unnecessary at this point in time.

#### Structure

Defines how users can navigate the site and utilise all existing features.
The structure of the site is modelled on a very basic blog site. Most simple blog pages online follow a similar template as this site.
The structure allows users to visit the site, browse haikus and tanka extenstions and filter haikus by tagname. In order to contribute to the site in any way however, user authentication is required for which an account must be created.

#### Skeleton

Puts features defined in structure into navigational elements.
For a first outline of the project skeleton see [Wireframes](#wireframes).
To guarantee intuitive navigation of the site, both the navbar and the main content follow a standard layout pattern that should be familiar to most users.
The navbar provides links to the main features and functions of the site, varying based on whether a user is authenticated or not. On small to medium screen sizes drop-down burger menu takes the place of the full navbar. A second-option home button is in place as a small logo, opposite all other nav links. According to research, this is also common practice.
The main content is presented in a list view of haiku panels which link to the details and other functions of each haiku.
Buttons and links are appropriately named. Clear and simple instructions as to how to use the page can be found in the relevant sections.
A footer with social media links (currently merely serve as placeholders) completes the "framing" effect of the site.

#### Surface

Addresses visual design and how to convey desired emotions and achieve desired effects.
For more detail on the planning of the surface plane, see [Visual Design Choices](#visual-design-choices).


### Visual Design Choices

**Colour Scheme:**

In keeping with the minimalist style, the colour scheme utilises only one colour (#E91C32). It is represented throughout the site in background images, navbar and footer. This color (see CSS custom property ``--primary-color``) originates from the "Koi-sun-wave haiku tile image" and was determined by using the Chrome extension color picker [ColorZilla](https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp).

![Primary colour](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670070285/woohoo_haiku/images/readme/primary-color.png)

To set a background for the navbar and footer, an opacity of 0.6 was added to the primary color (see CSS custom property ``--p-color-opaque``).
The exception are various call-to-action-buttons which follow the traditional signal colours.

**Fonts:**

Fonts were chosen to convey Asian/Japanese visuals. 
For full despcription of font names and their sources see [Media and Styling](#media-and-styling)

**Images and Icons:**

All images and icons used depict classic Japanese artistic elements such as koi, cherry blossom and finger waves.
The icons for the like-btn and the tanka counter were deliberately picked as something other than the classic heart and speech bubble icon to add originality to the design. 
For full despcription of all images and their sources see [Media and Styling](#media-and-styling).


## Features

### Existing Features

#### Navigation

- Navbar with icon and nav links
- Different links visible for authenticated and unauthenticated users
- Active link rendered black instead of default white
- Collapsible burger menu with drop-down on small to medium screens

![navbar](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/nav-unauth.png)

![navbar logged in](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/navbar.png)

![burger menu](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/nav-burger.png)

#### Site introduction

- Introductory paragraph at top of home page
- Explains to user what site is about and how use and navigate it
- Links "Sign Up" and "Create Page" inside paragraph are clickable depending on user authentication

![site intro](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/site-intro.png)

#### Haiku list

- Paginated list view of haikus on home page
- Haiku panels serve as links to haiku details
- Panel shows title, author, tagname, number of likes and number of added tankas

![haiku-list](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/haiku-list-view.png)

#### Filter buttons

- Button group on homepage listing all available tagnames
- "All haikus" button acts as delete filters

![filter button group](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/filter-btns.png)

#### Filtered haikus

- List view of all haikus with the same tagname
- Default message displays if no haikus with selected tag exist

![filtered haikus](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/filter-result.png)

![no filter result message](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/no-tags.png)

#### My haikus

- Renders list of haikus only submitted by currently authenticated user
- Default message displays if user has not submitted any haikus yet

![user haikus](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/user-haikus.png)

![no user haikus message](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/no-user-haikus.png)

#### Haiku details

- Renders body of individual haiku on seperate page
- Displays title, tagname, author, content, number of likes and number of tankas
- If user is authenticated, "Edit" and "Delete" buttons are rendered below haiku

![haiku details](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/haiku-detail.png)

#### Create haiku

- Form to write and submit haiku renders on seperate page
- Form contains fields for title (textfield), tag (select drop-down) and content (textfield)
- All fields are required and submission will not succeed unless form is completed
- Includes instructions on how to write haiku above input fields

![haiku instructions](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/haiku-instructions.png)

![haiku form](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/haiku-form.png)

#### Tankas

- Displays list of all admin approved tanka extenstions below haiku details
- If no tankas have been added yet, default message displays

![added tankas](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/tankas.png)

![no tankas](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/no-tankas.png)

#### Tanka form

- Only visible to authenticated users
- Includes instructions on how to extend haiku into tanka
- Located below haiku detail and existing tanka extensions
- Submission requires admin approval and will not be displayed until approved

![tanka form](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691699/woohoo_haiku/images/readme/features/tanka-form.png)

#### Edit haiku

- Only accessible by authenticated user who is author of selected haiku
- Form prepopulated by selected haiku content
- All fields are required and submission will not succeed unless form is completed

![edit form](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/edit-form.png)

#### Delete haiku

- Only accessible by authenticated user who is author of selected haiku
- Renders seperate page that prompts user to confirm action to delete haiku

![delete page](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/delete-page.png)

#### Sign Up

- Allows user to create account
- Fields include Username, Email (optional), Password and Password confirmation

![sign up page](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/login.png)

#### Login

- Login form asking for username and password of signed up user
- Includes "Remember me" checkbox option

![login page](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/login.png)

#### Logout

- Seperate page prompts user to confirm action to sign out.

![sign out page](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691698/woohoo_haiku/images/readme/features/logout.png)

#### Footer

- Footer with social medial icon links
- Links open in seperate tabs

![footer](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670691697/woohoo_haiku/images/readme/features/footer.png)

### Possible Future Features

**Image upload for user**

Add file upload option to haiku form. Allow user to upload image that matches theme of created haiku. Set image as suttle background for haiku detail panel.

**Music toggle**

Include background music toggle switch. Music will be non-vocal and conducive to deep focus and creativity, i. e. chillstep, psy-ambient, futur garage.

**Likes for tankas**

Include like functionality for tanka extension. Allows users to rate which extensions work best for submitted haikus.

**Syllable checker**

Write JS function that validates haiku format upon submission. Function will count syllables before each linebreak and insure submitted haiku matches the 5-7-5 pattern. This function could also be extended to confirm the 7-7 pattern for tankas.

## Database Design

### Database Model

The database model diagram was designed using [Lucidchart](https://lucid.app/lucidchart/88f8fdd7-6949-48b7-a9a0-6e707d5e895c/edit?beaconFlowId=331535FA3078AF35&invitationId=inv_3c9d46e5-845a-48bf-85b4-52635aa019e8&page=0_0#).
The first draft of the entity relationship diagram does not include all models used in the final database.

![ERD](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/ERD-with-tanka.jpg)

### CRUD

The CRUD principle was the heart of the design process for this project. For a detailed description of all CRUD features see [Features](#features)

**Create:**
An authenticated user can create and save a haiku entry.

**Read:**
A user can browse and read their own and other users' haiku entries.

**Update:**
An authenticated user can edit and update their own saved entries.

**Delete:**
An authenticated user can delete their own saved entries.

## Technologies Used

### Work Environments and Hosting

- [Figma](https://www.figma.com/) (Wireframes)
- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [Cloudinary](https://cloudinary.com/) (Serving static media files)

### Python Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)

### External Libraries and Applications

- [Whitenoise](https://whitenoise.evans.io/en/latest/) (Serving static non-media files)
- [Summernote](https://summernote.org/) (WYSIWYG editor - currently not utilised but installed for possible future use)

### Database

- [ElephantSQL](https://www.elephantsql.com/) (PostgreSQL database hosting)

## Testing

### Test Guide

For extensive instructions on how to manually test this site and it's user stories, please refer to these [testing instructions](TESTING.md)

### Validator Testing

#### HTML [W3C validator](https://validator.w3.org/)

As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Jinja templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.

**Home page**

No errors or warnings to show.

**My Haikus page**

No errors or warnings to show.

**Create page**

No errors or warnings to show.

**Tag selection page**

No errors or warnings to show.

**Haiku details page**

1 info, 1 warning, 6 errors.

![haiku details html validation result](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670930603/woohoo_haiku/images/readme/validation_imgs/create-haiku-html-errors.png)

*Fix:*

- Remove trailing slash from ``<br />``.
- Change ``<article>`` element into ``<div>`` element as "article" did not contribute much to semantics and accessibility. 
- Render form in template using ``{{ tanka_form | crispy }}`` instead of ``{{ tanka_form | safe }}`` as this caused Django to insert table elements. CSS adjustments were needed to re-style tanka form.

**Edit Haiku page**

No errors or warnings to show.

**Delete Haiku page**

No errors or warnings to show.

**Sign Up page**

No errors or warnings to show.

**Login page**

No errors or warnings to show.

**Sign Out page**

No errors or warnings to show.

#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No error found.

![jigsaw result](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670932703/woohoo_haiku/images/readme/validation_imgs/css-jigsaw-result.png)

#### JavaScript [JSHint](https://jshint.com/) 

1 undefined variable: bootstrap. 
Referring to line 122 in base.html ``let alert = new bootstrap.Alert(msg)``

*Fix:*

No action required as this is a custom bootstrap variable and did not need to be defined inside the script.

#### Python [CI Python Linter](https://pep8ci.herokuapp.com/)

Only files with custom written python code have been verified with the above validator.

**admin.py**

All clear, no errors found

**forms.py**

All clear, no errors found

**models.py**

All clear, no errors found

**haikus/urls.py**

All clear, no errors found

**views.py**

All clear, no errors found

**settings.py**

All clear, no errors found

**woohoo_haiku/urls.py**

All clear, no errors found

### Browser Testing

**Layout:** Testing layout and appearance of site for consistency throughout browsers.

**Functionality:** 
- Testing complete functionality of the site. This includes:
    - Sign Up
    - Login
    - Logout
    - External social media links
    - Navigation
    - Browse entries
    - Filter entries by tag name
    - Create new entry
    - Like/unlike entries
    - Comment/extend entries
    - Delete and edit entries
    - Admin user functions
    
- Ensuring all links, navigation and form submit functions as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| Safari      | ✔          | ✔             |
| IE          |deprecated by Microsoft, not tested|

### Fixed bugs

- **Slug for user haiku**:

    For a haiku submitted by a non-admin user the slug won't auto-generate.

    **Fix**: 
    
    Include helper method ```save``` in ```Haiku``` model ([Reference](https://stackoverflow.com/questions/68897050/slug-not-auto-generate-after-add-page-in-django)).


- **Nav link of current page not highlighted**:

    Due to Django's templating nature, the navbar HTML only occurs once, in the base template. This prevents manual adding of an "active" class to the link currently on.

    **Fix**: 
    
    Wrap all ```<li>``` items in nav list in ```{% with url_name=request.resolver_match.url_name %}```. Then run ```{% if ... %}``` check on each list item to see if URL name matches URL patch and if so, append "active" class ([Reference](https://stackoverflow.com/questions/39639264/django-highlight-current-page-in-navbar)).


- **Repeat of message for zero user haikus**

    In template ``user_haikus``, if the user has not yet submitted any haikus, a message should display, informing the user of this. Initially the message repeated for the length of the for loop (number of all haiku objects) instead of only displaying once.

    **Fix**:

    Move conditional statement that compares user ID to haiku author ID to view level. Initially this was done with an if statement inside the forloop in the template. However, this seemed to prevent the ``{% empty %}`` option of a Django forloop from working. By moving the conidition test into a method ``def get_queryset(self)`` inside the ``UserHaikus`` view, ``{% empty %}`` can now be used in the template forloop to check if the list of objects is empty.
    ([Reference](https://www.geeksforgeeks.org/for-empty-loop-django-template-tags/))


- **Tanka count on homepage**:

    The tanka counter of each haiku entry on the homepage displays the number of all submitted tankas when it should only count approved submits.

    **Fix**:

    Add helper method ``approved_tankas`` to ``Haiku`` model which filters tankas by approval status ``True``. This method can then be referenced in index.html template. ([Reference](https://github.com/DjangoGirls/tutorial-extensions/issues/39#issuecomment-276360075)).


- **Select option in Haiku form not disabled**:

    The select option in the haiku form with value "Tag your haiku" is not disabled and could potentially be selected as a tag option.

    **Fix**:

    Target option with text value "Tag your haiku" via JavaScript in ``base.html`` and add necessary attributes ``disabled``, ``selected`` and ``hidden``.


- **Placeholder tag shows as link on homepage**:

    The placeholder tag with text value "Tag your haiku" shows as a link in the tag button group on the homepage but shouldn't.

    **Fix**:

    Use JavaScript to loop through all elements with class of ``tag-link``, select the one with ``innerText`` value of "Tag your haiku" and change style to ``display: none``. 


- **Haiku update form showing html for admin**:

    When editing a haiku as an admin user, the haiku content renders html tags and attributes in the textarea of the edit form

    **Fix**:

    Remove Summernote formatting from admin Haiku and Tanka form. As for this project, the extra formatting Summernote provides is unnecessary and even upset the formatting of haiku entries made by admin users as well as the respective haiku edit form.


### Unfixed bugs

There are currently no known bugs 😀

## Deployment

This project was deployed using [Heroku](https://heroku.com/), [Cloudinary](https://cloudinary.com/), [ElephantSQL](https://www.elephantsql.com/) and [Whitenoise](https://whitenoise.evans.io/en/latest/). For a full list libraries refer to [Technologies Used](#technologies-used).

#### Installing libraries

The following steps outline all libraries needed for successful deployment on Heroku. All necessary requirements and settings updates will not be discussed in this section as they are assumed as logical follow-up steps to installments. For full explanation on how to install these libraries, refer to the links provided in [Technologies Used](#technologies-used).

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-cloudinary-storage``
- Install **Whitenoise** (prevent issues with Heroku not rendering custom stylesheet): ``pip3 install whitenoise``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but be more inventive about the key string!)

#### Update Settings

- Add the following code at the top of ``settings.py`` to connect Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to new database, replace provided **DATABASE** variable with 
    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made

#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")

#### Connect to Cloudinary

- In Cloudinary dashboard, copy **API Environment variable**
- In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"`` and remove ``CLOUDINARY_URL=`` from the variable string
- Add same variable value as new Heroku config var named **CLOUDINARY_URL**
- In ``settings.py``, in ``INSTALLED_APPS`` list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
- To define Cloudinary as static file storage add the following to settings.py
    ````
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

#### Allow Heroku as host

- In ``settings.py`` add
    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
    ````

## Development

The following options are available to work with this code or run in a local environment.

### Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on repository to download ([woohoo-haiku](https://github.com/Kathrin-ddggxh/woohoo-haiku))
- Click the **Fork** buttonin the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed

### Clone

Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repostitory (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change current directory to target location for cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

### Download as ZIP

- Log into GitHub and click on repository to download ([woohoo-haiku](https://github.com/Kathrin-ddggxh/woohoo-haiku))
- Select **Code** and click "Download Zip" file
- Once download is completed, extract ZIP file and use in your local environment

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/ie/) tutorials "Hello Django" and "I Think Therefore I Blog".
For further guidance on syntax and implementation of features I also referred to [Codemy Django tutorials](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com) and [Very Academy tutorials](https://www.youtube.com/c/veryacademy/playlists)

**CreateHaiku View**:

The view that enables an authenticated user to add and save their own haiku was created using Django's [CreateView method](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)

**Form submit feedback**:

To display a self-closing feedback message to the user after submitting a form, I used the this [StackOverflow article](https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post) as reference.

**Form Customisation**:

Form customisation was achieved using [Django Widgets](https://docs.djangoproject.com/en/dev/ref/forms/widgets/). 

The syntax for adding a form select field was inspired by a [Codemy tutorial](https://www.youtube.com/watch?v=_ph8GF84fX4&ab_channel=Codemy.com) 

**Haiku categories and filter option**:

The option to filter haikus by tagname was implemented following this [Codemy tutorial](https://www.youtube.com/watch?v=2MkULPXXXLk&ab_channel=Codemy.com). The UI for this functionality was altered to display in the form of a button group rather than nav links.

**Main page pagination**

The code to add conditional pagination to the ``index`` template, including page navigation links was taken as Django and Bootstrap boilerplate from [Code Institute source code](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/06_creating_our_first_view/templates/index.html). Styling was customised. 

### Media and Styling

**Images:**

*Koi nav icon:* [Hani Suwaryo | dreamstime.com](https://www.dreamstime.com/koi-logo-japan-fish-japanese-symbol-background-illustration-vector-stock-koi-logo-japan-fish-japanese-koi-fishes-logo-luck-image114846444 )

*Cherry blossom background image:* [Alofipo | cleanpng.com](https://www.cleanpng.com/png-plum-blossom-red-plum-411432/download-png.html)

*Koi-sun-wave haiku tile image:* [pngegg.com](https://www.pngegg.com/en/png-vcqwe )

**Fonts:**

All fonts were taken from [DaFont](https://www.dafont.com/).

*Ninja Warrior:* [Hardiboy Design](https://www.dafont.com/profile.php?user=1278940)

*Dekiru:* [Laura Luppani](https://www.dafont.com/profile.php?user=473885)




