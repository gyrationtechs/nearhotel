from django.db import models
import datetime


class Booking(models.Model):
    name = models.CharField(max_length=255)
    room_num = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    check_in = models.DateTimeField(default=datetime.datetime.now)
    latitude = models.DecimalField(decimal_places=10, max_digits=10000)
    latitude = models.DecimalField(decimal_places=10, max_digits=10000)

    def __str__(self):
        return self.name

