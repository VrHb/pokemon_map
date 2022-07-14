from django.db import models


class Pokemon(models.Model):
    """Вид покемона"""
    title_ru = models.CharField(
        max_length=200,
        verbose_name="Название на русском"
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Название на английском"
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Название на японском"
    )
    image = models.ImageField(
        null=True,
        verbose_name="Картинка"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание покемона"
    )
    next_evolution = models.ForeignKey(
        "self",
        verbose_name="В кого эволюционирует",
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
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень развития', blank=True)
    health = models.IntegerField(verbose_name='Здоровье', blank=True)
    strength = models.IntegerField(verbose_name='Сила', blank=True)
    defence = models.IntegerField(verbose_name='Защита', blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True)

    class Meta:
        verbose_name = "Покемон на карте"
        verbose_name_plural = "Покемоны на карте"

    def __str__(self):
        return f"{self.pokemon.title_ru}"
