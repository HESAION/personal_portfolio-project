# Generated by Django 3.2.9 on 2021-12-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_myblog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='date',
            field=models.DateField(),
        ),
    ]