# Generated by Django 2.1.4 on 2020-02-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0005_tbl_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_contact',
            name='name',
            field=models.CharField(default='public', max_length=100),
        ),
    ]
