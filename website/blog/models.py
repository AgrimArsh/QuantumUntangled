from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__():
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} by {self.author.username}'