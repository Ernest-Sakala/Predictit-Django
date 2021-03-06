# Generated by Django 4.0 on 2021-12-21 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drug', '0003_drugmodel_image'),
        ('user', '0002_customuser_is_farmer_customuser_is_pharmacy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drugmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
    ]
