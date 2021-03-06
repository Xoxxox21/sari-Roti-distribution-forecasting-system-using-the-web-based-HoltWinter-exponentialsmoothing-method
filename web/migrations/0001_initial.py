# Generated by Django 4.0.4 on 2022-05-13 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataroti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_roti', models.CharField(max_length=100)),
                ('nama_roti', models.CharField(max_length=100)),
                ('harga_roti', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='datasales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16)),
                ('nama', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('no_hp', models.CharField(max_length=13)),
                ('Email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'laki-laki'), ('p', 'perempuan')], default='L', max_length=10)),
                ('pilih_status', models.CharField(choices=[('menikah', 'menikah'), ('belum menikah', 'belum menikah')], default='menikah', max_length=13)),
                ('pilih_sales_type', models.CharField(choices=[('ML', 'MOBIL'), ('MR', 'MOTOR')], default='ML', max_length=10)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_berakhir', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='datatoko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=5)),
                ('nama', models.CharField(max_length=50)),
                ('pemilik', models.CharField(max_length=50)),
                ('no_hp', models.CharField(max_length=13)),
                ('Email', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_akun_name', models.CharField(max_length=50)),
                ('npwp_no', models.CharField(max_length=15)),
                ('name_npwp', models.CharField(max_length=50)),
                ('provinsi', models.CharField(max_length=20)),
                ('kabupaten_kota', models.CharField(max_length=20)),
                ('kecamatan', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(decimal_places=20, max_digits=20)),
                ('longtitude', models.DecimalField(decimal_places=20, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='jadwal_kunjungan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=100)),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.datasales')),
                ('toko_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.datatoko')),
            ],
        ),
        migrations.CreateModel(
            name='datadistribusi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.CharField(max_length=100)),
                ('Store', models.CharField(max_length=100)),
                ('Store_Type', models.CharField(max_length=100)),
                ('Disc', models.CharField(max_length=100)),
                ('roti_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.dataroti')),
            ],
        ),
    ]
