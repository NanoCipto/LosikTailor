# Generated by Django 4.1.1 on 2022-09-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baju',
            fields=[
                ('IDbaju', models.AutoField(primary_key=True, serialize=False)),
                ('jenisbaju', models.CharField(max_length=30)),
                ('hargabaju', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='pelanggan',
            fields=[
                ('IDpelanggan', models.AutoField(primary_key=True, serialize=False)),
                ('Nama', models.CharField(max_length=100)),
                ('noHP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tambahan',
            fields=[
                ('IDtambahan', models.AutoField(primary_key=True, serialize=False)),
                ('jenistambahan', models.CharField(max_length=20)),
                ('hargatambahan', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='pemesanan',
            fields=[
                ('IDpemesanan', models.AutoField(primary_key=True, serialize=False)),
                ('tanggalpemesanan', models.DateField()),
                ('IDpelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LSKTAILOR.pelanggan')),
            ],
        ),
        migrations.CreateModel(
            name='detailtambahan',
            fields=[
                ('IDdetailtambahan', models.AutoField(primary_key=True, serialize=False)),
                ('Jumlahitemtambahan', models.IntegerField()),
                ('IDpemesanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LSKTAILOR.pemesanan')),
            ],
        ),
        migrations.CreateModel(
            name='detailpesanan',
            fields=[
                ('IDdetailpesanan', models.AutoField(primary_key=True, serialize=False)),
                ('Jeniskain', models.CharField(max_length=30)),
                ('Ukuranbaju', models.CharField(max_length=100)),
                ('Jumlahitempesanan', models.IntegerField()),
                ('IDjenisbaju', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LSKTAILOR.baju')),
                ('IDpemesanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LSKTAILOR.pemesanan')),
            ],
        ),
    ]