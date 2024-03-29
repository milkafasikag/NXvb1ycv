# Generated by Django 4.2.4 on 2023-10-30 21:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_useraccess_referer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unique_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True)),
                ('url', models.URLField(null=True)),
                ('access_count', models.PositiveIntegerField(default=0)),
                ('prodact', models.BooleanField(default=False)),
            ],
        ),
    ]
