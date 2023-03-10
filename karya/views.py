from django.shortcuts import render, redirect
from multiprocessing import context
from .models import Artikel, Kategori, Berita
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

def is_seniman(user):
    if user.groups.filter(name='Seniman').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Seniman').exists():
        request.session['is_seniman'] = 'seniman'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)

def berita(request):
    template_name = "back/tabel_berita.html"
    berita = Berita.objects.all()
    # print(artikel)
    context = {
        'title' : 'dashboard',
        'berita': berita,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_seniman)
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    #for a in artikel:
     #   print(a.nama,'-',a.jadwal,'-',a.kategori)
    context = {
        'title' : 'DATA',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    print(kategori)
    if request.method == "POST":
        nama = request.POST.get('nama')
        deskripsi = request.POST.get('deskripsi')
        pencipta = request.POST.get('pencipta')
        kategori = request.POST.get('kategori')
        harga = request.POST.get('harga')
        
        # memanggil kategori
        kat = Kategori.objects.get(nama=kategori)
        
        Artikel.objects.create(
            nama = nama,
            deskripsi = deskripsi,
            pencipta = pencipta,
            kategori = kat,
            harga = harga,
        ) 
        return redirect(artikel)
    
    context = {
        'title' : 'Tambah Data',
        'kategori' : kategori,
    }   
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'Lihat Informasi Jadwal',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

# edit artikel
@login_required
def edit_artikel(request, id):
    template_name = "back/edit_artikel.html"
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get('nama')
        deskripsi = request.POST.get("deskripsi")
        harga = request.POST.get("harga")
        print(nama, deskripsi, harga)
        # save data
        a.nama = nama
        a.deskripsi = deskripsi
        a.harga = harga
        a.save()
        return redirect(artikel)
    
    
    context = {
        'title' : 'Edit Informasi',
        'artikel': a,
        
    }
    return render(request, template_name, context)
# edit artikel
@login_required
def hapus_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

@login_required
@user_passes_test(is_seniman)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'Dashboard tabel_users',
        'list_user' : list_user
    }
    return render(request, template_name, context)

def sinkron_berita(request):
	url = "https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=3d511487debd4bbdb9cbdf6c824eae35"
	data = requests.get(url).json()
	for d in data['articles']:
		cek_berita = Berita.objects.filter(nama=d['author'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.nama=d['author']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Berita.objects.create(
				nama = d['author'],
				title = d['title'],
				desc = d['description'],
				tanggal = d['publishedAt'],
				link = d['url'],
                conten = d['content'],
				img = d['urlToImage'],
			)
	return redirect(berita)
