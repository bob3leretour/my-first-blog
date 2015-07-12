from django.db import models
from django.utils import timezone
from django.core.mail import send_mail

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        send_mail('HELLO', 'BLABLA', 'benjamin.chomel@hotmail.com', ['benjamin.chomel@hotmail.com'])
        self.save()

    def __str__(self):
        return self.title