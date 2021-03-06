# Generated by Django 3.2.7 on 2021-10-18 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_alter_plant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_watered', models.DateTimeField()),
                ('note', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='plant-pics/updates')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
        ),
    ]
