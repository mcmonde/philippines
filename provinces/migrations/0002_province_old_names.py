# Generated by Django 4.2.11 on 2024-04-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='old_names',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
