from django.urls import path
from . import views

urlpatterns = [
    path('pelanggan',views.pelanggan, name='pelanggan'),
    path('createdatapelanggan',views.createdatapelanggan, name='createdatapelanggan'),
    path('update/<str:id>',views.updatedatapelanggan, name='updatedatapelanggan'),
    path('delete/<str:id>',views.deletedatapelanggan, name='deletedatapelanggan'),
    path('baju',views.baju, name='baju'),
    path('createdatabaju',views.createdatabaju, name='createdatabaju'),
    path('updatebaju/<str:id>',views.updatedatabaju, name='updatedatabaju'),
    path('deletebaju/<str:id>',views.deletedatabaju, name='deletedatabaju'),
    path('tambahan',views.tambahan, name='tambahan'),
    path('createdatatambahan',views.createdatatambahan, name='createdatatambahan'),
    path('updatetambahan/<str:id>',views.updatedatatambahan, name='updatedatatambahan'),
    path('deletetambahan/<str:id>',views.deletedatatambahan, name='deletedatatambahan'),
    path('pemesanan',views.pemesanan, name='pemesanan'),
    path('createdatapemesanan',views.createdatapemesanan, name='createdatapemesanan'),
    path('updatepemesanan/<str:id>',views.updatedatapemesanan, name='updatedatapemesanan'),
    path('deletepemesanan/<str:id>',views.deletedatapemesanan, name='deletedatapemesanan'),
]