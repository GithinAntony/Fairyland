# Generated by Django 2.1.4 on 2020-02-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0009_delete_tbl_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=50)),
                ('mother_id', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]
