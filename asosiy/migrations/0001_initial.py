# Generated by Django 4.0.5 on 2022-06-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('miqdor', models.IntegerField()),
                ('brend', models.CharField(max_length=50)),
                ('kelgan_narx', models.PositiveSmallIntegerField()),
                ('sotuv_narx', models.PositiveSmallIntegerField()),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ombor')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('dokon', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=50)),
                ('qarz', models.IntegerField()),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ombor')),
            ],
        ),
    ]
