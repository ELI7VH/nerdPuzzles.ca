# Generated by Django 2.0.1 on 2018-01-24 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_challenge_challenge_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='id',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='week_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]