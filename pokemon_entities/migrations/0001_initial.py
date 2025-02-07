# Generated by Django 3.1.14 on 2022-07-12 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200)),
                ('title_en', models.CharField(blank=True, max_length=200)),
                ('title_jp', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evolutions', to='pokemon_entities.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('appeared_at', models.DateTimeField(default=None)),
                ('disappeared_at', models.DateTimeField(default=None)),
                ('level', models.IntegerField(default=None)),
                ('health', models.IntegerField(default=None)),
                ('strength', models.IntegerField(default=None)),
                ('defence', models.IntegerField(default=None)),
                ('stamina', models.IntegerField(default=None)),
                ('pokemon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
