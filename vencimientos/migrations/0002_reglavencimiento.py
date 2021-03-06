# Generated by Django 4.0.2 on 2022-02-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_impuesto_ini_venc'),
        ('vencimientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReglaVencimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit_d', models.IntegerField(default=0)),
                ('cuit_h', models.IntegerField(default=9)),
                ('dia', models.IntegerField()),
                ('impuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.impuesto')),
            ],
        ),
    ]
