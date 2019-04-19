from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


def validate_negative(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s can not be negative'),
            params={'value': value},
        )


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0, validators=[validate_negative])
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        if self.views < 0:
            self.views = 0
        super(Category, self).save(*args, **kwargs)

    # For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Page(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        current_time = now()
        if self.first_visit is not None:
            if self.first_visit > current_time:
                self.first_visit = current_time
        if self.last_visit is not None:
            if self.last_visit > current_time:
                self.last_visit = current_time
        super(Page, self).save(*args, **kwargs)

    # For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
