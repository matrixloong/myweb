from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('pub_date',)

    def __unicode__(self):
        return self.title
# Create your models here.


class Essay(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    creation_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('creation_time',)

    def __unicode__(self):
            return self.title


