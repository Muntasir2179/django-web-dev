from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name} - ({self.code})"
    
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.city} - {self.street} - ({self.postal_code})"
    

    # This class is used to add special behavior to the model
    class Meta:
        verbose_name_plural = "Address Entries"   # replaces the plural name of the model by assigned name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1, message="Rating cannot be less then 1"),
            MaxValueValidator(limit_value=5, message="Rating cannot be greater then 5")
        ]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")   # models.PROTECT, models.SET_NULL
    published_countries = models.ManyToManyField(Country)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)  # Harry Porter 1 => harry-porter-1

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    # this method constructs the url that can be used to navigate the data
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # # overriding save method for automatically populate slug field
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    