# Generated by Django 2.2.24 on 2021-06-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0008_pythonpackagecontent_unique_sha256'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythondistribution',
            name='allow_uploads',
            field=models.BooleanField(default=True),
        ),
    ]
