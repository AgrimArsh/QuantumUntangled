from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user}'

# Create Profile when creating user (https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#disqus_thread)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when creating User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Tag(models.Model):
    db_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.display_name}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} by {self.author.username}'