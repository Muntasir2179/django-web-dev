from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1, message="Rating cannot be less then 1"),
            MaxValueValidator(limit_value=5, message="Rating cannot be greater then 5")
        ]
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)  # Harry Porter 1 => harry-porter-1

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    # this method constructs the url that can be used to navigate the data
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # overriding save method for automatically populate slug field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    