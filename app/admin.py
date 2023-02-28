from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Project, Post, Ticket, Category, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Ticket)
admin.site.register(Category)

