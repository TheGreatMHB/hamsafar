# Generated by Django 4.2 on 2023-04-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVP', '0002_destination_name_destination_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='type',
            field=models.CharField(choices=[('Food', 'Food'), ('Exciting', 'Exciting'), ('Sport', 'Sport'), ('Relaxtion', 'Relaxtion')], max_length=100),
        ),
    ]