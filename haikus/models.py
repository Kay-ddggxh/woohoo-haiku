from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Haiku(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="haiku_entries")
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='haiku_likes', blank=True)
    # tag = models.TextChoices() => many to many?
    # bg_image = CloudinaryField('image', default='placeholder')
    # possibly user uploaded image

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title


class Tanka(models.Model):

    post = models.ForeignKey(
        Haiku, on_delete=models.CASCADE, related_name='tankas')
    name = models.CharField(max_length=60)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)   # user approved

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f"{self.name} made this into a tanka: {self.body}"
