# Generated by Django 3.1.2 on 2020-11-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0006_auto_20201115_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracksheet',
            name='track_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
