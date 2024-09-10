# Generated by Django 3.2.4 on 2021-06-12 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupomDesconto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('desconto', models.FloatField()),
                ('usos', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 12, 2, 58, 1, 151396)),
        ),
    ]