from django.db import models
from _datetime import date

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    transportation = models.BooleanField()
    weatherSensetion = models.BooleanField()
    status = models.BooleanField()
    date = models.DateField()
    counter = models.IntegerField()

    def __str__(self):
        return self.name

    def deleteRest(self, deleteId):
        self.objects.filter(id=deleteId).delete()

    def updateStatus(self, newStatus, updateId):
        self.objects.get(id=updateId).update(status = newStatus)



