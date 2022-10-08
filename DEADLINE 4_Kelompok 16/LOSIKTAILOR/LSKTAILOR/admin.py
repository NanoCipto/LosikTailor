from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.pelanggan)
admin.site.register(models.baju)
admin.site.register(models.tambahan)
admin.site.register(models.pemesanan)
admin.site.register(models.detailpesanan)
admin.site.register(models.detailtambahan)