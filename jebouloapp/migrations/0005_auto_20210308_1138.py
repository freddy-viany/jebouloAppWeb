# Generated by Django 3.1.3 on 2021-03-08 10:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jebouloapp', '0004_auto_20210306_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcemodel',
            name='customermodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermodel', to='jebouloapp.customermodel'),
        ),
        migrations.AlterField(
            model_name='announcemodel',
            name='mobile_phone',
            field=models.CharField(max_length=27, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(237)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='number_of_publication_announce',
            field=models.IntegerField(default=1, verbose_name='number publication'),
        ),
    ]
