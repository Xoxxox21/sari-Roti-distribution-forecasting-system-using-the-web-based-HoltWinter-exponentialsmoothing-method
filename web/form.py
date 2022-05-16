from dataclasses import field
from django import forms
from django.forms import ModelForm
from web.models import *

class FormtambahSales(ModelForm):
    class Meta:
        model = datasales
        fields = '__all__'
        LAKILAKI = 'L'
        perempuan = 'p'
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
        widget = {
            'nik' : forms.TextInput(),
            'nama' : forms.TextInput(),
            'alamat' : forms.Textarea(),
            'no_hp' : forms.TextInput(),
            'Email' : forms.TextInput(),
            'username' : forms.TextInput(),
            'jenis_kelamin' : forms.ChoiceField(choices=jk),
            'status' : forms.ChoiceField(choices=status),
            'sales_type' : forms.ChoiceField(choices=sales_type),
            'tanggal_mulai' : forms.DateField(input_formats="%d-%m-%Y"),
            'tanggal_berakhir' : forms.DateField(input_formats='%d-%m-%Y')
        }

class Formtoko(ModelForm):
    class Meta:
        model = datatoko
        fields = '__all__'
        PnD= 'P&D'
        WARUNG_REorNOO = 'WARUNG RE/NOO'
        MTI_REorNOO = 'MTI RE/NOO'
        toko = [
            (PnD,'P&D'),
            (WARUNG_REorNOO,'WARUNG RE/NOO'),
            (MTI_REorNOO,'MTI RE/NOO'),
        ]
        widget = {
            'kode' : forms.TextInput(),
            'nama' : forms.TextInput(),
            'pemilik' : forms.TextInput(),
            'no_hp' : forms.TextInput(),
            'Email' : forms.TextInput(),
            'alamat' : forms.Textarea(),
            'Jenis_toko' : forms.ChoiceField(choices=toko),
            'bank_name' : forms.TextInput(),
            'bank_akun_name' : forms.TextInput(),
            'npwp_no' : forms.TextInput(),
            'name_npwp' : forms.TextInput(),
            'provinsi' : forms.TextInput(),
            'kabupaten_kota' : forms.TextInput(),
            'kecamatan' : forms.TextInput(),
            'village' : forms.TextInput(),
            'latitude' : forms.TextInput(),
            'longtitude' : forms.TextInput(),
        }
        
class form_jadwal_kunjungan(ModelForm):
    class Meta:
        model = jadwal_kunjungan
        fields = '__all__'
        sales_id = models.ForeignKey(
            datasales,
            on_delete=models.CASCADE
        )
        toko_id = models.ForeignKey(
                datatoko,
                on_delete=models.CASCADE
        )
        hari = models.CharField(max_length=100)
        
class form_roti(ModelForm):
    class Meta:
        model = dataroti
        fields = '__all__'
        widget = {
            'kode' : forms.TextInput(),
            'nama' : forms.TextInput(),
            'harga' : forms.TextInput(),
        }