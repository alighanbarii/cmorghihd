# Generated by Django 5.2.4 on 2025-07-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_created_at_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
