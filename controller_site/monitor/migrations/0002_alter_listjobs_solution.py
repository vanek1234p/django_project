# Generated by Django 5.0.6 on 2024-05-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listjobs',
            name='solution',
            field=models.CharField(choices=[('waiting for the controller', 'waiting for the controller'), ('accepted', 'accepted'), ('not accepted', 'not accepted'), ('defective', 'defective')], max_length=200),
        ),
    ]
