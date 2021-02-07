from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=25)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'cities'
