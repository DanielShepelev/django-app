# Generated by Django 4.2.7 on 2023-12-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_logic', '0002_userprofile_delete_foodiprefrence'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodiPrefrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodType', models.CharField(max_length=80)),
                ('Restrictions', models.CharField(max_length=1000)),
                ('City', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
