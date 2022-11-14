from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    tasks_organization = models.CharField(max_length=200, blank=True)
    tasks_full_name = models.CharField(max_length=200, blank=True)
    tasks_tel_number  = models.CharField(max_length=200, blank=True)
    tasks_email = models.EmailField(blank=True)
    tasks_source = models.CharField(max_length=200)
    tasks_theme_letters = models.CharField(max_length=200, blank=True)
    tasks_stages = models.CharField(max_length=200)
    tasks_requested_equipment = models.CharField(max_length=200)
    tasks_more_info = models.TextField(null=True, blank=True)
    tasks_name_offer = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tasks_organization