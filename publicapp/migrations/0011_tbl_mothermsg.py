# Generated by Django 2.1.4 on 2020-02-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0010_tbl_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_mothermsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=50)),
                ('mother_id', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]
