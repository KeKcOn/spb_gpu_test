# Generated by Django 3.2.25 on 2024-03-10 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_organizaton', to='api.organization', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=None, max_length=11),
        ),
    ]