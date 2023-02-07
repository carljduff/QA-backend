from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='portfolio/images/')
    jira = models.URLField(blank=True)
    mockup = models.URLField(blank=True)
    confluence = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    date = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        
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