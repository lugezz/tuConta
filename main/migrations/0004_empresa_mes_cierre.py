# Generated by Django 4.0.2 on 2022-02-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_empresa_options_alter_feriado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='mes_cierre',
            field=models.IntegerField(default=12),
        ),
    ]
