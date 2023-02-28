from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='portfolio/images/')
    jira = models.URLField(blank=True)
    mockup = models.URLField(blank=True)
    confluence = models.URLField(blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creators', default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    date = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.title

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
        
    class Meta:
        verbose_name_plural = 'Categories'

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(blank=False)
    reference = models.URLField(blank=True)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"