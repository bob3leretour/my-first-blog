from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.core.files import File

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d', default='default.jpg')

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title