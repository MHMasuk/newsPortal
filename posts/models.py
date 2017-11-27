from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.conf import settings

from category.models import Category
# Create your models here.
# POSTS MODELS.PY

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to='posts', null=True, blank=True, width_field='width', height_field='height')
    slug = models.SlugField(allow_unicode=True, unique=True)
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)  # Create_at is the creation date
    message = models.TextField()
    category = models.ForeignKey(Category, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
                                               'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']  # Every message is uniquely linked to the user
