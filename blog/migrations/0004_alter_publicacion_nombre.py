# Generated by Django 3.2.25 on 2025-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20250617_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
