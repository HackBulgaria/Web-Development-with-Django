from django.contrib import admin

from users.models import Author, Buyer, BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'age', 'interests')


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'customer_id', 'came_from', )
