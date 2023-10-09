from django.db import models


class Stock(models.Model):
    robot_serial = models.CharField(
        max_length=5,
        blank=False,
        null=False,
    )
    amount = models.PositiveSmallIntegerField()
