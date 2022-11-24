# Woohoo Haiku

This Django project is a little poetry blog that can turn into a call-and-response game through user interaction. The main value in it lies to provide fun to those who enjoy poetry, haiku or just playing with words.

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## Table of Contents

- [Design](#design)
    - [Database Model](#database-model)
    - [Wireframes](#wireframes)
    - [Visual Design Choices](#visual-design-choices)
    - [CRUD](#crud)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [UX](#ux)
    - [Site Goals](#site-goals)
    - [User Stories](#user-stories)

- [Testing](#testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    

## Design

The overall design of the site is based on the Japanese principle of minimalism and therefore doesn't include a lot of visual variants and distractions.

The general layout, navigation and functionality is plain and intiutive, meeting a user's expectation of any standard blog site.

Features and interactivity are kept to a minimum, as to not overwhelm the user with too many options and to maintain a zen like usage of the site.

### Database Model

The first draft of the entity relationship diagram does not include all models used in the final database.

![ERD](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/ERD-with-tanka.jpg)

### Wireframes

The initial [wireframes in Figma](https://www.figma.com/file/Ajb5EOJLJedDc0v8a0wL67/Woohoo-Haiku) are an overly simplified version of the finished product and merely served the purpose of listing most of the site's essential features.

Not all features and functions are covered by these first drafts. For a full list of existing features see [Features](#features)

![home-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/home.jpg)

![read-haiku-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/read-haiku.jpg)

![browse-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/browse.jpg)

![create-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/create.jpg)

![login-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/login.jpg)

![signup-wireframe](https://res.cloudinary.com/kay-ddggxh/image/upload/v1669304695/woohoo_haiku/images/readme/wireframes_erd/signup.jpg)

### Visual Design Choices

**Colour Scheme:**

In keeping with the minimalist style, the colour scheme utilises only one colour (and variants of different opacity). It is represented throughout the site in background images, navbar and footer.
The exception are various call-to-action-buttons which follow the traditional signal colours.

**Fonts:**

Fonts were chosen to convey Asian/Japanese visuals. 
For full despcription of font names and their sources see [Media and Styling](#media-and-styling)

**Images:**

All images used depict classic Japanese artistic elements such as koi, cherry blossom and finger waves.
For full despcription of all images and their sources see [Media and Styling](#media-and-styling)

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

## Features

### Existing Features

### Possible Future Features

## UX

### Site Goals

### User Stories

## Testing

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

    The select option in the haiku form with value "Tag your haiku appropriately" is not disabled and could potentially be selected as a tag option.

    **Fix**:

    Set first select option (now has index 0) of haiku form manually to "Tag your haiku appropriately" with value "placeholder" in ``forms.py``.
    Then target option with index 0 via JavaScript in ``base.html`` and add necessary attributes ``disabled``, ``selected`` and ``hidden``.


- **Haiku update form showing html for admin**:

    When editing a haiku as an admin user, the haiku content renders html tags and attributes in the textarea of the edit form

    **Fix**:

    Remove Summernote formatting from admin Haiku and Tanka form. As for this project, the extra formatting Summernote provides is unnecessary and even upset the formatting of haiku entries made by admin users as well as the respective haiku edit form.


### Unfixed bugs

There are currently no known bugs 😀

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

*Koi-sun-wave haike tile image:* [pngegg.com](https://www.pngegg.com/en/png-vcqwe )

**Fonts:**

All fonts were taken from [DaFont](https://www.dafont.com/).

*Ninja Warrior:* [Hardiboy Design](https://www.dafont.com/profile.php?user=1278940)

*Dekiru:* [Laura Luppani](https://www.dafont.com/profile.php?user=473885)




