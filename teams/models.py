from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

class Team(models.Model):
    name = models.CharField(max_length=64)
    manager = models.CharField(max_length=64)
    short_name = models.CharField(max_length=5)
    year_founded = models.DateField()
    country = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.pk)])

