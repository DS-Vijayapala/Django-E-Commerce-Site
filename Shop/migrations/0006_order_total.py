# Generated by Django 5.1.7 on 2025-03-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=2000),
            preserve_default=False,
        ),
    ]
