# Generated by Django 3.0.4 on 2020-03-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200325_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='heading',
            field=models.CharField(default='Blog Post', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='article',
            field=models.CharField(max_length=4000),
        ),
    ]
