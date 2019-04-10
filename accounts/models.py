from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True)
    description = models.CharField(max_length=100, default='')
    student = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user.username} UserProfile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class NewsletterUser(models.Model):
        email = models.EmailField()
        date_added = models.DateTimeField(auto_now_add=True)

        def __init__(self):
                return self.email