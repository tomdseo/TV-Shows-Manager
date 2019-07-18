from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    releaseDate = models.DateField()
    description = models.TextField()

