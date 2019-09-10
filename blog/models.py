from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    REVIEW_CHOICES = ((1, 'E'), (2, 'D'), (3, 'C'), (4, 'B'), (5, 'A'))
    particle = models.IntegerField(null=True, choices=REVIEW_CHOICES)
    logical = models.IntegerField(null=True, choices=REVIEW_CHOICES)
    performance = models.IntegerField(null=True, choices=REVIEW_CHOICES)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()