# Generated by Django 5.0.3 on 2024-03-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
