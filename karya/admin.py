from django.contrib import admin
from .models import *

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','deskripsi','pencipta','kategori','harga')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)

class BeritaAdmin(admin.ModelAdmin):
     list_display = ('nama','title','desc','tanggal','link','conten','img')
admin.site.register(Berita,BeritaAdmin)