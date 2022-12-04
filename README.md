# Woohoo Haiku

This Django project is a little poetry blog that can turn into a call-and-response game through user interaction. The main value in it lies to provide fun to those who enjoy poetry, haiku or just playing with words.
Much like a regular blog site, a registered user can submit posts, like and comment on other users' posts. However, the posts and comments are meant to follow the [Haiku/Tanka format](https://poetry4kids.com/lessons/how-to-write-a-tanka-poem/). Thus, the original post will be a haiku. Other users can then add two more lines to extend it into a tanka, whilst trying to capture and maintain the feel of the original post and understand the authors subject and intent.

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## Table of Contents

- [UI/UX](#uiux)
    - [Wireframes](#wireframes)
    - [Visual Design Choices](#visual-design-choices)
    - [Site Goals](#site-goals)
    - [User Stories](#user-stories)
    
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

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    

## UI/UX

The overall design of the site is based on the Japanese principle of minimalism and therefore doesn't include a lot of visual variants and distractions.

The general layout, navigation and functionality is plain and intiutive, meeting a user's expectation of any standard blog site.

Features and interactivity are kept to a minimum, as to not overwhelm the user with too many options and to maintain a zen like usage of the site.


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


### Visual Design Choices

**Colour Scheme:**

In keeping with the minimalist style, the colour scheme utilises only one colour (#E91C32). It is represented throughout the site in background images, navbar and footer. This color (see CSS custom property ``--primary-color``) originates from the "Koi-sun-wave haiku tile image" and was determined by using the Chrome extension color picker [ColorZilla](https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp).

![Primary colour](https://res.cloudinary.com/kay-ddggxh/image/upload/v1670070285/woohoo_haiku/images/readme/primary-color.png)

To set a background for the navbar and footer, an opacity of 0.6 was added to the primary color (see CSS custom property ``--p-color-opaque``).
The exception are various call-to-action-buttons which follow the traditional signal colours.

**Fonts:**

Fonts were chosen to convey Asian/Japanese visuals. 
For full despcription of font names and their sources see [Media and Styling](#media-and-styling)

**Images:**

All images used depict classic Japanese artistic elements such as koi, cherry blossom and finger waves.
For full despcription of all images and their sources see [Media and Styling](#media-and-styling)

### Site Goals

### User Stories

## Features

### Existing Features

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

### Browser Testing

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

    Include ``{% if forloop.first %}`` statement to insure message is only displayed after the first iteration of the for loop ([Reference](https://stackoverflow.com/a/46927971)).


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

## Development

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/ie/) tutorials "Hello Django" and "I Think Therefore I Blog".
For further guidance on syntax and implementation of features I also referred to [Codemy Django tutorials](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com) and [Very Academy tutorials](https://www.youtube.com/c/veryacademy/playlists)

**CreateHaiku View**:

The view that enables an authenticated user to add and save their own haiku was created using Django's [CreateView method](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)

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




