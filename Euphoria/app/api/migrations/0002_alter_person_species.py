# Generated by Django 4.0 on 2022-01-14 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.species'),
        ),
    ]
