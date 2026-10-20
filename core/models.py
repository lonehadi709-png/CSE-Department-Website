
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    photo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    venue = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.title
