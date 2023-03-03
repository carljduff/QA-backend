from django.contrib import admin
from .models import Project, Post, Ticket, Category, UserData
# Register your models here.

admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(UserData)

