from django.db import models

# Create your models here.

class pelanggan (models.Model):
    IDpelanggan = models.AutoField(primary_key=True)
    Nama = models.CharField(max_length=100)
    noHP = models.IntegerField()

    def __str__(self):
        return str(self.IDpelanggan)

class baju (models.Model):
    IDbaju = models.AutoField(primary_key=True)
    jenisbaju = models.CharField(max_length=30)
    hargabaju = models.FloatField()

    def __str__(self):
        return str(self.IDbaju)

class tambahan (models.Model):
    IDtambahan = models.AutoField(primary_key=True)
    jenistambahan = models.CharField(max_length=20)
    hargatambahan = models.FloatField()

    def __str__(self):
        return str(self.IDtambahan)

class pemesanan (models.Model):
    IDpemesanan = models.AutoField(primary_key=True)
    IDpelanggan = models.ForeignKey(pelanggan,on_delete=models.CASCADE)
    tanggalpemesanan = models.DateField()
    tanggalselesai = models.DateField()

    def __str__(self):
        return str(self.IDpemesanan)

class detailpesanan (models.Model):
    IDdetailpesanan = models.AutoField(primary_key=True)
    IDpemesanan = models.ForeignKey(pemesanan,on_delete=models.CASCADE)
    IDbaju = models.ForeignKey(baju,on_delete=models.CASCADE)
    Jeniskain = models.CharField(max_length=30)
    Ukuranbaju = models.CharField(max_length=100)
    Jumlahitempesanan = models.IntegerField()

    def __str__(self):
        return str(self.IDdetailpesanan)

class detailtambahan (models.Model):
    IDdetailtambahan = models.AutoField(primary_key=True)
    IDpemesanan = models.ForeignKey(pemesanan,on_delete=models.CASCADE)
    IDtambahan = models.ForeignKey(tambahan,on_delete= models.CASCADE)
    Jumlahitemtambahan = models.IntegerField()

    def __str__(self):
        return str(self.IDdetailtambahan)

