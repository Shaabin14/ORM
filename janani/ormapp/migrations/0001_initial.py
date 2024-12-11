# Generated by Django 5.1.4 on 2024-12-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('customer_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=100)),
                ('loan_no', models.IntegerField()),
                ('loan_amount', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
