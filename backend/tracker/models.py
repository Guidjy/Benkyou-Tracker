from django.db import models
from accounts.models import User
from django.utils import timezone
from datetime import timedelta


class Content(models.Model):
    TYPE_CHOICES = {
        'BO': 'book',
        'SH': 'show',
        'PD': 'podcast',
        'TE': 'textbook',
        'OT': 'other'
    }
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='OT')
    title = models.CharField(max_length=128)
    total_time_spent = models.DurationField(default=timedelta(0))
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    

class Activity(models.Model):
    TYPE_CHOICES = {
        'RE': 'read',
        'WA': 'watched',
        'LI': 'listened',
        'ST': 'studied',
        'OT': 'other',
    }
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='OT')
    duration = models.DurationField(default=timedelta(0))
    date_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='activities_user', on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='activities_content', on_delete=models.CASCADE, blank=True, null=True)
    

class AccountabilityPartner(models.Model):
    user1 = models.ForeignKey(User, related_name='partner_1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='partner_2', on_delete=models.CASCADE)
