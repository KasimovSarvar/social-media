# Generated by Django 5.1.4 on 2024-12-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='admin', max_length=128),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='adminov', max_length=128),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
