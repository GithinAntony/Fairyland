# Generated by Django 2.1.4 on 2020-02-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0006_auto_20200218_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_contact',
            name='user',
            field=models.CharField(default='public', max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]