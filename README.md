# Woohoo Haiku

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## References/Documentation/Tutorials

### Django Documentation

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.

**CreateHaiku View**:

The view that enables an authenticated user to add and save their own haiku was created using Django's [CreateView method](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)

**Form Customisation**:

Form customisation was achieved using [Django Widgets](https://docs.djangoproject.com/en/dev/ref/forms/widgets/). 

The syntax for adding a form select field was inspired by a [Codemy tutorial](https://www.youtube.com/watch?v=_ph8GF84fX4&ab_channel=Codemy.com) 


## Bugs

### Fixed bugs

- **Slug for user haiku**:

    For a haiku submitted by a non-admin user the slug won't auto-generate.

    **Fix**: Include helper method ```save``` in ```Haiku``` model ([Reference](https://stackoverflow.com/questions/68897050/slug-not-auto-generate-after-add-page-in-django))


### Unfixed bugs

- **Tanka count on homepage**:

    The tanka counter of each haiku entry on the homepage displays the number off all submitted tankas when it should only count approved submits

- **Select option in Haiku form not disabled**:

    The select option in the haiku form with value "Tag your haiku" is not disabled and could potentially be selected as a tag option.