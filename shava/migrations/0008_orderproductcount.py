# Generated by Django 3.0.6 on 2020-05-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shava', '0007_auto_20200525_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProductCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shava.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shava.Product')),
            ],
        ),
    ]
