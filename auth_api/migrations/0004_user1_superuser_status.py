# Generated by Django 3.2.7 on 2021-09-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0003_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='superuser_status',
            field=models.BooleanField(default=False),
        ),
    ]