import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone

from .models import Pokemon, PokemonEntity


timezone.localtime()


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_map = PokemonEntity.objects.filter(
        disappeared_at__gt=timezone.now(),
        appeared_at__lt=timezone.now()
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons_on_map:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            image_url=request.build_absolute_uri(pokemon.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
        })
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons_on_map = PokemonEntity.objects.filter(
        pokemon__id=pokemon_id,
        disappeared_at__gt=timezone.now(),
        appeared_at__lt=timezone.now()
    )
    if pokemons_on_map:
        previous_pokemon_evolution = pokemons_on_map[0].pokemon.evolutions.all()
        next_pokemon_evolution = pokemons_on_map[0].pokemon.evolution
        pokemon = {
            'img_url': pokemons_on_map[0].pokemon.image.url,
            'title_ru': pokemons_on_map[0].pokemon.title_ru,
            'title_en': pokemons_on_map[0].pokemon.title_en,
            'title_jp': pokemons_on_map[0].pokemon.title_jp,
            'description': pokemons_on_map[0].pokemon.description,
        }
        if next_pokemon_evolution:
            pokemon['next_evolution'] = {
                'title_ru': next_pokemon_evolution.title_ru,
                'pokemon_id': next_pokemon_evolution.id,
                'img_url': next_pokemon_evolution.image.url
            }
        if previous_pokemon_evolution:
            pokemon['previous_evolution'] = {
                'title_ru': previous_pokemon_evolution[0].title_ru,
                'pokemon_id': previous_pokemon_evolution[0].id,
                'img_url': previous_pokemon_evolution[0].image.url
            }
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_on_map:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            image_url=request.build_absolute_uri(
                pokemon_entity.pokemon.image.url
            )
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon,
    })
