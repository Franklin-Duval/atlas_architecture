# Generated by Django 3.1.2 on 2020-11-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas_architecture', '0004_auto_20201108_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='code',
            field=models.CharField(default='Type_code', max_length=10),
        ),
    ]