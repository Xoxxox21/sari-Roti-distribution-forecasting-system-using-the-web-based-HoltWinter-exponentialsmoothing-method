from django.db import models
from django.forms import NumberInput

class datatoko (models.Model):
    PnD= 'P&D'
    WARUNG_REorNOO = 'WARUNG RE/NOO'
    MTI_REorNOO = 'MTI RE/NOO'
    toko = [
        (PnD,'P&D'),
        (WARUNG_REorNOO,'WARUNG RE/NOO'),
        (MTI_REorNOO,'MTI RE/NOO'),
    ]
    kode = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)
    pemilik = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=13)
    Email = models.CharField(max_length=50)
    alamat = models.TextField()
    Jenis_toko = models.CharField(max_length=13, choices=toko, default=PnD)
    bank_name = models.CharField(max_length=50)
    bank_akun_name = models.CharField(max_length=50)
    npwp_no = models.CharField(max_length=15)
    name_npwp = models.CharField(max_length=50)
    provinsi = models.CharField(max_length=50)
    kabupaten_kota = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    def __str__(self):
        return self.nama

class datasales (models.Model):
    LAKILAKI = 'laki-laki'
    perempuan = 'perempuan'
    MENIKAH='menikah'
    BELUMMENIKAH='belum menikah'
    ML = 'ML'
    MR = 'MR'
    jk = [
        (LAKILAKI,'laki-laki'),
        (perempuan,'perempuan'),
    ]
    status = [
        (MENIKAH,'menikah'),
        (BELUMMENIKAH,'belum menikah'),
    ]
    sales_type = [
        (ML,'MOBIL'),
        (MR,'MOTOR')    
    ]
    nik = models.CharField(max_length=16)
    nama = models.CharField(max_length=50)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=13)
    Email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=jk,
        default=LAKILAKI
    )
    pilih_status = models.CharField(
        max_length=13,
        choices=status,
        default=MENIKAH
    )
    pilih_sales_type = models.CharField(
        max_length=10,
        choices=sales_type,
        default=ML
    )
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    def __str__(self):
        return self.nama
    

class dataroti (models.Model):
    kode = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    def __str__(self):
        return self.nama

class datadistribusi (models.Model):
    tanggal = models.CharField(max_length=100)
    Store = models.CharField(max_length=100)
    Store_Type = models.CharField(max_length=100)
    Disc = models.CharField(max_length=100)
    roti_id = models.ForeignKey(
        dataroti,
        on_delete=models.CASCADE
    )

class jadwal_kunjungan(models.Model):
    sales_id = models.ForeignKey(
        datasales,
        on_delete=models.CASCADE
    )
    toko_id = models.ForeignKey(
        datatoko,
        on_delete=models.CASCADE
    )
    hari = models.CharField(max_length=100)
    def __str__(self):
        return self.sales_id