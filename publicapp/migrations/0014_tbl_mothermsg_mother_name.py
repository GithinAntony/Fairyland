# Generated by Django 2.1.4 on 2020-02-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0013_tbl_mothermsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_mothermsg',
            name='mother_name',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
