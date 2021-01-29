from django.db import models

class Pilot(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name
