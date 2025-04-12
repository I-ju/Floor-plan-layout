# Generated by Django 5.2 on 2025-04-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
                ('width', models.FloatField(default=50)),
                ('height', models.FloatField(default=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(default='#FFF68F', max_length=20)),
            ],
        ),
    ]
