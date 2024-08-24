from django.db import models

class WorldMap(models.Model):
    name = models.CharField(verbose_name="Nome do País", max_length=100)
    capital = models.CharField(verbose_name="Capital do País", max_length=100, blank=True, null= True)
    subregion = models.CharField(verbose_name="Continente em que está localizado", max_length=100, blank=True, null= True)
    population = models.CharField(verbose_name="População do País", max_length=100, blank=True, null= True)
    region = models.CharField(verbose_name="Região", max_length=100, blank=True, null= True)
   
    def __str__(self) -> str:
       return f"{self.name} - {self.region}"
