# Generated by Django 4.2.5 on 2024-01-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_document_title_alter_document_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='contents',
            field=models.TextField(blank=True, default='Hi there! This is **markdown** 👋'),
        ),
    ]
