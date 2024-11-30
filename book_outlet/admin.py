from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author")
    list_display = ("title", "author")
    list_display_links = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address")
    list_display_links = ("first_name", "last_name", "address")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "postal_code")
    list_display_links = ("city",)


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    list_display_links = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
