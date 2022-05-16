"""sariroti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('index/', index, name='index'),
    path('data-sales/', sales, name='data-sales'),
    path('data-toko/', toko, name='data-toko'),
    path('data-distribusi/', distribusi, name='data-distribusi'),
    path('data-roti/', roti, name='data-roti'),
    path('data-jadwal/', jadwal, name='data-jadwal-kunjungan'),
    path('tambah-sales/', tambahsales, name='tambah-sales'),
    path('data-sales/ubah/<int:id_sales>', updatesales, name='update-sales'),
    path('data-toko/ubah/<int:id_toko>', updatetoko, name='update-toko'),
    path('data-sales/hapus/<int:id_sales>', hapus_sales, name='hapus-sales'),
    path('data-toko/hapus/<int:id_toko>', hapus_toko, name='hapus-toko'),
    path('tambah-jadwal/', tambahjadwal, name='tambah-jadwal'),
    path('data-jadwal/ubah/<int:id_jadwal>', updatejadwal, name='update-jadwal'),
    path('data-jadwal/hapus/<int:id_jadwal>', hapus_jadwal, name='hapus-jadwal'),
    path('tambah-roti/', tambahroti, name='tambah-roti'),
    path('data-roti/ubah/<int:id_roti>', updateroti, name='update-roti'),
    path('data-roti/hapus/<int:id_roti>', hapus_roti, name='hapus-roti'),
    
]