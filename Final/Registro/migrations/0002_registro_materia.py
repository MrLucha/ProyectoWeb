# Generated by Django 3.0.3 on 2020-02-18 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Materia', '0001_initial'),
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='Materia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Materia.Materia'),
        ),
    ]
