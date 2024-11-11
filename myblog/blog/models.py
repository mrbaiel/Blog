from django.utils import timezone

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title[:30]
