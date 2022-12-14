from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tag(models.Model):
    """
    Defines tag (category) object
    """
    tagname = models.CharField(max_length=80)

    def __str__(self):
        return self.tagname


# Source: https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/blog/models.py#:~:text=class%20Post(,.count() # noqa
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
    tag = models.ForeignKey(
        Tag, on_delete=models.PROTECT, default=1, related_name="tag")

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        helper method to return total num of likes on post
        """
        return self.likes.count()

    def approved_tankas(self):
        """
        helper method to return number of approved tankas only
        """
        return self.tankas.filter(approved=True)

    def save(self, *args, **kwargs):
        """
        helper method to generate slug for haikus submitted
        by non-admin users
        """
        self.slug = slugify(self.title)
        super(Haiku, self).save(*args, **kwargs)


# Source: https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/blog/models.py#:~:text=class%20Comment(,name%7D%22  # noqa
class Tanka(models.Model):
    """
    Defines Tanka object
    """
    post = models.ForeignKey(
        Haiku, on_delete=models.CASCADE, related_name='tankas')
    name = models.CharField(max_length=60)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f"{self.name} made this into a tanka: {self.body}"
