# Woohoo Haiku

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## References/Documentation/Tutorials

### Django Practices and Syntax

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


## Bugs

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


### Unfixed bugs

- **Tanka count on homepage**:

    The tanka counter of each haiku entry on the homepage displays the number off all submitted tankas when it should only count approved submits

- **Select option in Haiku form not disabled**:

    The select option in the haiku form with value "Tag your haiku" is not disabled and could potentially be selected as a tag option.

- **Haiku update form showing html for admin**:

    When editing a haiku as an admin user, the haiku content renders html tags and attributes in the textarea of the edit form
