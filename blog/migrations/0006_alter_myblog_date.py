# Generated by Django 3.2.9 on 2021-12-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_myblog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]