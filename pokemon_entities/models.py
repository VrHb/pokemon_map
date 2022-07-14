from django.db import models



class Pokemon(models.Model):
    """Вид покемона"""
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True) 
    description = models.TextField(blank=True) 
    next_evolution = models.ForeignKey(
        "self",
        verbose_name="Эволюция покемона", 
        related_name="previous_evolution",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    class Meta:
        verbose_name = "Покемон"
        verbose_name_plural = "Покемоны"
    
    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    """Покемоны на карте"""
    pokemon = models.ForeignKey(
    Pokemon,
    verbose_name="Вид покемона",
    related_name="pokemons",
    on_delete=models.CASCADE,
    )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
    
    class Meta:
        verbose_name = "Покемон на карте"
        verbose_name_plural = "Покемоны на карте"
    
    def __str__(self):
        return f"{self.pokemon.title_ru} {self.pokemon.id}"

