# Generated by Django 3.1.3 on 2021-03-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jebouloapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='number_of_publication_announce',
            field=models.IntegerField(default=2, verbose_name='number publication'),
        ),
    ]
