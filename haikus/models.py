from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Haiku(models.Model):
    """
    Defines Haiku object
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="haiku_entries")
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='haiku_like', blank=True)
    tag = models.CharField(max_length=80, default="Tag your haiku")
    # bg_image = CloudinaryField('image', default='placeholder')
    # possibly user uploaded image

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        # helper method to return total num of likes on post
        return self.likes.count()

    def save(self, *args, **kwargs):
        # helper method to generate slug for haikus submitted
        # by non-admin users
        self.slug = slugify(self.title)
        super(Haiku, self).save(*args, **kwargs)


class Tanka(models.Model):
    """
    Defines Tanka object
    """
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


class Tag(models.Model):
    """
    Defines tag (category) object
    """
    tagname = models.CharField(max_length=80)

    def __str__(self):
        return self.tagname
