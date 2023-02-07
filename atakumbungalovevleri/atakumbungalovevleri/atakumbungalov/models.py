from django.db import models

class Hakkımda(models.Model):
    baslik = models.CharField(max_length=20)
    icerik = models.TextField()
    image = models.ImageField(upload_to="hakkımda")
    
    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"

    def __str__(self):
        return self.baslik


class Hizmetler(models.Model):
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Hizmetler"
        verbose_name_plural = "Hizmetler"

    def __str__(self):
        return self.baslik


class Galeri(models.Model):
    baslik = models.CharField(max_length=50)
    image = models.ImageField(upload_to="galeri")
    anasayfa_active = models.BooleanField(default='False')
    yayıntarih = models.DateTimeField(auto_now_add=True, verbose_name='Yayın Tarihi')

    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"
    
    def __str__(self):
        return self.baslik

class AnasayfaHizmetler(models.Model):
    baslik = models.CharField(max_length=50, verbose_name="Başlık")
    icerik = models.TextField(verbose_name='İçerik')
    image = models.ImageField(verbose_name='Resim')

    class Meta:
        verbose_name = 'Ana Sayfa Hizmetler'
        verbose_name_plural = 'Ana Sayfa Hizmetler'



