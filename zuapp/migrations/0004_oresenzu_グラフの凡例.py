# Generated by Django 3.1.5 on 2021-05-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuapp', '0003_oresenzu'),
    ]

    operations = [
        migrations.AddField(
            model_name='oresenzu',
            name='グラフの凡例',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
