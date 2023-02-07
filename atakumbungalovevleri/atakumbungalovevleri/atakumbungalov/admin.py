from django.contrib import admin
from .models import Hakkımda,Hizmetler,Galeri,AnasayfaHizmetler



admin.site.register(Hizmetler)


class HakkımdaAdmin(admin.ModelAdmin):
    list_display = ['baslik','tarih']
    
    class Meta:
        model = Hakkımda
admin.site.register(Hakkımda)

class GaleriAdmin(admin.ModelAdmin):
    list_display = ['image','yayıntarih']
    class Meta:
        model = Galeri
admin.site.register(Galeri, GaleriAdmin)

class AnasayfaHizmetlerAdmin(admin.ModelAdmin):
    list_display = ["baslik"]
    class Meta:
        model = AnasayfaHizmetler
admin.site.register(AnasayfaHizmetler, AnasayfaHizmetlerAdmin)


