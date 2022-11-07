# Woohoo Haiku

[Link to live site](https://woohoo-haiku.herokuapp.com/) 

## References/Documentation/Tutorials

### Django Documentation

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.

**CreateHaiku View**:

The view that enables an authenticated user to add and save their own haiku was created using Django's [CreateView method](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)

**Form Customisation**:

To add placeholder text to the HaikuForm input fields I used [Django Widgets](https://docs.djangoproject.com/en/dev/ref/forms/widgets/) inside the constructor method. It was achieved taking input from [this tutorial](https://www.youtube.com/watch?v=C_tb3AOj2qg&ab_channel=VeryAcademy) and a [Stackoverflow article](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django)