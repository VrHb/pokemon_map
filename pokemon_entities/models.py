from django.db import models



class Pokemon(models.Model):
    """Вид покемона"""
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True) 
    description = models.TextField(blank=True) 
    evolution = models.ForeignKey(
        "self",
        verbose_name="Эволюция покемона", 
        related_name="evolutions",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    """Рокемон на карте"""
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name="Вид покемона",
        on_delete=models.CASCADE, 
        blank=True
    )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(default=None)
    health = models.IntegerField(default=None)
    strength = models.IntegerField(default=None)
    defence = models.IntegerField(default=None)
    stamina = models.IntegerField(default=None)

