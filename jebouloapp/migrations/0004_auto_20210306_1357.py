# Generated by Django 3.1.3 on 2021-03-06 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jebouloapp', '0003_auto_20210306_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customermodel',
            old_name='number_of_publication_competence',
            new_name='number_of_publication_announce',
        ),
    ]
