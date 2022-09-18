# Generated by Django 4.1 on 2022-09-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='downvote',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='upvote',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
