# Generated by Django 4.0 on 2021-12-15 09:48

from django.db import migrations, models
import plant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.jpg', upload_to=plant.models.upload_to, verbose_name='Image')),
            ],
        ),
    ]
