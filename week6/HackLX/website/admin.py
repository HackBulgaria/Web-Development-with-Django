from django.contrib import admin

from .models import Offer, Category


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'author', 'image')
    search_fields = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
