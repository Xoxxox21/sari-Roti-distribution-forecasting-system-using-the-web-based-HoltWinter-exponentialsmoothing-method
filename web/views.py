from operator import le
from django.shortcuts import redirect, render
from web.models import *
from web.form import *
from django.contrib import messages
def index(request):
    data_sales = datasales.objects.all()
    data_toko = datatoko.objects.all()
    data_distribusi = datadistribusi.objects.all()
    data_jadwal = jadwal_kunjungan.objects.all()
    data_roti = dataroti.objects.all()
    total_sales = len(data_sales)
    total_toko = len(data_toko)
    total_roti = len(data_roti)
    konteks={
        'data_sales' : data_sales,
        'data_toko' : data_toko,
        'data_distribusi' : data_distribusi,
        'data_jadwal' : data_jadwal,
        'data_roti' : data_roti,
        'total_sales' : total_sales,
        'total_toko' : total_toko,
        'total_roti' : total_roti,
    }
    return render(request, 'index.html', konteks)

def sales(request):
    data_sales = datasales.objects.all()
    konteks={
        'data_sales' : data_sales,
    }
    return render(request, 'datasales.html', konteks)

def toko(request):
    data_toko = datatoko.objects.all()
    konteks={
        'data_toko' : data_toko,
    }
    return render(request, 'datatoko.html', konteks)

def distribusi(request):
    data_distribusi = datadistribusi.objects.all()
    konteks={
        'data_distribusi' : data_distribusi,
    }
    return render(request, 'distribusi.html', konteks)

def tambahsales(request):
    if request.POST:
        form = FormtambahSales(request.POST)
        if form.is_valid():
            form.save()
            pesan="Data berhasil ditambahkan"
        else:
            pesan="Data yang dimasukkan tidak valid"
        form=FormtambahSales()    
        konteks={
                'form': form,
                'pesan': pesan,
            }
        return render(request, 'tambahsales.html', konteks)
    else:
        form=FormtambahSales()
        konteks={
                'form': form,
        }
        return render(request, 'tambahsales.html', konteks)

def updatesales(request, id_sales):
    Sales = datasales.objects.get(id=id_sales)
    template = 'updatesales.html'
    if request.POST:
        form = FormtambahSales(request.POST, instance=Sales)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('update-sales', id_sales=id_sales)             
    else:
        form = FormtambahSales(instance=Sales)
        konteks = {
            'form' : form,
            'sales' : Sales,
        }
    return render(request,template,konteks)

def updatetoko(request, id_toko):
    Toko = datatoko.objects.get(id=id_toko)
    template = 'updatetoko.html'
    if request.POST:
        form = Formtoko(request.POST, instance=Toko)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('update-toko', id_toko=id_toko)             
    else:
        form = Formtoko(instance=Toko)
        konteks = {
            'form' : form,
            'toko' : Toko,
        }
    return render(request,template,konteks)

def hapus_sales(request, id_sales):
    Sales = datasales.objects.filter(id=id_sales)
    Sales.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('data-sales')

def hapus_toko(request, id_toko):
    Toko = datatoko.objects.filter(id=id_toko)
    Toko.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('data-toko')

def jadwal(request):
    data_jadwal = jadwal_kunjungan.objects.all()
    konteks={
        'data_jadwal' : data_jadwal
    }
    return render(request, 'jadwal.html',konteks)

def tambahjadwal(request):
    if request.POST:
        form = form_jadwal_kunjungan(request.POST)
        if form.is_valid():
            form.save()
            pesan="Data berhasil ditambahkan"
        else:
            pesan="Data yang dimasukkan tidak valid"
        form=form_jadwal_kunjungan()    
        konteks={
                'form': form,
                'pesan': pesan,
            }
        return render(request, 'tambahjadwal.html', konteks)
    else:
        form=form_jadwal_kunjungan()
        konteks={
                'form': form,
        }
        return render(request, 'tambahjadwal.html', konteks)

def updatejadwal(request, id_jadwal):
    Jadwal = jadwal_kunjungan.objects.get(id=id_jadwal)
    template = 'updatejadwal.html'
    if request.POST:
        form = form_jadwal_kunjungan(request.POST, instance=Jadwal)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('update-jadwal', id_jadwal=id_jadwal)             
    else:
        form = form_jadwal_kunjungan(instance=Jadwal)
        konteks = {
            'form' : form,
            'jadwal' : Jadwal,
        }
    return render(request,template,konteks)

def hapus_jadwal(request, id_jadwal):
    Jadwal = jadwal_kunjungan.objects.filter(id=id_jadwal)
    Jadwal.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('data-jadwal-kunjungan')

def roti(request):
    data_roti = dataroti.objects.all()
    konteks={
        'data_roti' : data_roti
    }
    return render(request, 'dataroti.html',konteks)

def tambahroti(request):
    if request.POST:
        form = form_roti(request.POST)
        if form.is_valid():
            form.save()
            pesan="Data berhasil ditambahkan"
        else:
            pesan="Data yang dimasukkan tidak valid"
        form=form_roti()    
        konteks={
                'form': form,
                'pesan': pesan,
            }
        return render(request, 'tambahroti.html', konteks)
    else:
        form=form_roti()
        konteks={
                'form': form,
        }
        return render(request, 'tambahroti.html', konteks)

def updateroti(request, id_roti):
    roti = dataroti.objects.get(id=id_roti)
    template = 'updateroti.html'
    if request.POST:
        form = form_roti(request.POST, instance=roti)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('update-roti', id_roti=id_roti)             
    else:
        form = form_roti(instance=roti)
        konteks = {
            'form' : form,
            'roti' : roti,
        }
    return render(request,template,konteks)

def hapus_roti(request, id_roti):
    roti = dataroti.objects.filter(id=id_roti)
    roti.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('data-roti')