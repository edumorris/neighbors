# Generated by Django 3.0.8 on 2020-08-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0002_auto_20200819_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='neighborhoob_name',
            new_name='neighborhood_name',
        ),
    ]