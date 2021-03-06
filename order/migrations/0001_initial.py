# Generated by Django 4.0 on 2021-12-21 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_customuser_is_farmer_customuser_is_pharmacy_and_more'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy', models.IntegerField()),
                ('paymentStatus', models.BooleanField()),
                ('orderedDate', models.DateTimeField()),
                ('packedDate', models.DateTimeField()),
                ('transportedDate', models.DateTimeField()),
                ('deliveredDate', models.DateTimeField()),
                ('cancelledDate', models.DateTimeField()),
                ('deliveryPrice', models.DateTimeField()),
                ('orderStatus', models.CharField(max_length=255)),
                ('totalAmount', models.CharField(max_length=255)),
                ('totalProducts', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.addressmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
    ]
