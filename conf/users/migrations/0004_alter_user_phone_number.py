# Generated by Django 3.2.25 on 2024-03-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240310_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=None, max_length=11, null=True),
        ),
    ]