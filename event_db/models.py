from django.db import models


class EventModel(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=400)
    repertoire = models.TextField()
    collaborative_musicians = models.TextField()
    tickets_link = models.CharField(max_length=200)
    objects = models.Manager()
