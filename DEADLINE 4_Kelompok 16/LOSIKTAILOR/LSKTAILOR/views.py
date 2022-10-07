from datetime import datetime
from pyexpat import model
from django.shortcuts import render, redirect
from . import models

# Create your views here.

def homepage(request):
    aktivitaspelanggan = models.pelanggan.objects.all()
    aktivitaspemesanan = models.pemesanan.objects.all()

    return render(request, 'homepage.html', {
        'aktivitaspelanggan' : aktivitaspelanggan,
        'aktivitaspemesanan' : aktivitaspemesanan
    })

def pelanggan(request):
    pelangganall = models.pelanggan.objects.all()

    return render(request, 'pelanggan.html',{
        'pelangganall' : pelangganall,
    })

def createdatapelanggan(request):
    if request.method == "GET":
        return render(request, 'createdatapelanggan.html')
    else :
        Nama = request.POST['Nama']
        noHP = request.POST['noHP']

        newpelanggan = models.pelanggan(
            Nama = Nama,
            noHP = noHP
        ).save()
        return redirect('pelanggan')

def updatedatapelanggan(request,id):
    pelangganobj = models.pelanggan.objects.get(IDpelanggan = id)
    if request.method == "GET":
        return render(request, "updatedatapelanggan.html",{
            'pelanggan' : pelangganobj
        })
    else :
        pelangganobj.Nama = request.POST['Nama']
        pelangganobj.noHP = request.POST['noHP']
        pelangganobj.save()
        return redirect('pelanggan')

def deletedatapelanggan(request,id):
    pelangganobj = models.pelanggan.objects.get(IDpelanggan = id)
    pelangganobj.delete()
    return redirect('pelanggan')

def baju(request):
    bajuall = models.baju.objects.all()

    return render(request, 'baju.html',{
        "bajuall" : bajuall,
    })

def createdatabaju (request):
    if request.method == "GET":
        return render(request, 'createdatabaju.html')
    else :
        jenisbaju = request.POST['jenisbaju']
        hargabaju = request.POST['hargabaju']

        newbaju = models.baju(
            jenisbaju = jenisbaju,
            hargabaju = hargabaju
        ).save()
        return redirect('baju')

def updatedatabaju(request,id):
    bajuobj = models.baju.objects.get(IDbaju = id)
    if request.method == "GET":
        return render(request, "updatedatabaju.html",{
            'baju' : bajuobj
        })
    else :
        bajuobj.jenisbaju = request.POST['jenisbaju']
        bajuobj.hargabaju = request.POST['hargabaju']
        bajuobj.save()
        return redirect('baju')

def deletedatabaju(request,id):
    bajuobj = models.baju.objects.get(IDbaju = id)
    bajuobj.delete()
    return redirect('baju')

def tambahan(request):
    tambahanall = models.tambahan.objects.all()

    return render(request, 'tambahan.html',{
        "tambahanall" : tambahanall,
    })

def createdatatambahan (request):
    if request.method == "GET":
        return render(request, 'createdatatambahan.html')
    else :
        jenistambahan = request.POST['jenistambahan']
        hargatambahan = request.POST['hargatambahan']

        newtambahan = models.tambahan(
            jenistambahan = jenistambahan,
            hargatambahan = hargatambahan
        ).save()
        return redirect('tambahan')

def updatedatatambahan(request,id):
    tambahanobj = models.tambahan.objects.get(IDtambahan = id)
    if request.method == "GET":
        return render(request, "updatedatatambahan.html",{
            'tambahan' : tambahanobj
        })
    else :
        tambahanobj.jenistambahan = request.POST['jenistambahan']
        tambahanobj.hargatambahan = request.POST['hargatambahan']
        tambahanobj.save()
        return redirect('tambahan')

def deletedatatambahan(request,id):
    tambahanobj = models.tambahan.objects.get(IDtambahan = id)
    tambahanobj.delete()
    return redirect('tambahan')



def pemesanan(request):
    data =[]
    pemesananall = models.pemesanan.objects.all()
    for item in pemesananall:
        dummy =[]
        IDpemesanan = item.IDpemesanan
        detailpesanan = models.detailpesanan.objects.filter(IDpemesanan = IDpemesanan)
        dummy.append(item)
        dummy.append(detailpesanan)
        data.append(dummy)
    return render(request, 'pemesanan.html',{
        'pemesananall' : pemesananall
    })

def createdatapemesanan (request):
    pelangganall = models.pelanggan.objects.all()
    if request.method == "GET":
        return render(request, 'createdatapemesanan.html', {
            'pelangganall' : pelangganall
        })
    else :
        IDpelanggan = request.POST['IDpelanggan']
        pelangganget = models.pelanggan.objects.get(IDpelanggan = IDpelanggan)
        pelangganobj = pelangganget
        tanggalpemesanan = request.POST['tanggalpemesanan']
        tanggalselesai = request.POST['tanggalselesai']

        newpemesanan = models.pemesanan(
            IDpelanggan = pelangganobj,
            tanggalpemesanan = tanggalpemesanan,
            tanggalselesai = tanggalselesai
        ).save()
        return redirect('pemesanan')

def updatedatapemesanan(request,id):
    pemesananobj = models.pemesanan.objects.get(IDpemesanan = id)
    pelangganall = models.pelanggan.objects.all()
    tanggalpemesanan = datetime.strftime(pemesananobj.tanggalpemesanan, '%Y-%m-%d')
    tanggalselesai = datetime.strftime(pemesananobj.tanggalselesai, '%Y-%m-%d')
    if request.method == "GET":
        return render(request, "updatedatapemesanan.html",{
            'pemesanan' : pemesananobj,
            'pelangganall' : pelangganall,
            'tanggalpemesanan' : tanggalpemesanan,
            'tanggalselesai' : tanggalselesai
        })
    else :
        pemesananobj.pelanggan = request.POST['IDpelanggan']
        pelangganbaru = models.pelanggan.objects.get(IDpelanggan = request.POST['IDpelanggan'])
        pemesananobj.IDpelanggan = pelangganbaru
        pemesananobj.tanggalpemesanan = request.POST['tanggalpemesanan']
        pemesananobj.tanggalselesai = request.POST['tanggalselesai']
        pemesananobj.save()
        return redirect('pemesanan')

def deletedatapemesanan(request,id):
    pemesananobj = models.pemesanan.objects.get(IDpemesanan = id)
    pemesananobj.delete()
    return redirect('pemesanan')

def detailpesanan(request):
    data =[]
    detailpesananall = models.detailpesanan.objects.all()    
    for item in detailpesananall:
        dummy =[]
        detailpesanan = item.IDdetailpesanan
        pemesanan = models.pemesanan.objects.filter(detailpesanan = detailpesanan)
        dummy.append(item)
        dummy.append(pemesanan)
        data.append(dummy)
    
    return render(request, 'detailpesanan.html',{
        "detailpesananall" : detailpesananall,
    })

def createdatadetailpesanan (request):
    pemesananall = models.pemesanan.objects.all()
    bajuall = models.baju.objects.all()
    if request.method == "GET":
        return render(request, 'createdatadetailpesanan.html', {
            'pemesananall' : pemesananall,
            'bajuall' : bajuall
        })
    else :
        IDpemesanan = request.POST['IDpemesanan']
        pemesananget = models.pemesanan.objects.get(IDpemesanan = IDpemesanan)
        pemesananobj = pemesananget
        IDbaju = request.POST['IDbaju']
        bajuget = models.baju.objects.get(IDbaju = IDbaju)
        bajuobj = bajuget
        Jeniskain = request.POST['Jeniskain']
        Ukuranbaju = request.POST['Ukuranbaju']
        Jumlahitempesanan = request.POST['Jumlahitempesanan']

        newdetailpesanan = models.detailpesanan(
            IDpemesanan = pemesananobj,
            IDbaju = bajuobj,
            Jeniskain = Jeniskain,
            Ukuranbaju = Ukuranbaju,
            Jumlahitempesanan = Jumlahitempesanan
        ).save()
        return redirect('detailpesanan')

def updatedatadetailpesanan(request,id):
    detailpesananobj = models.detailpesanan.objects.get(IDdetailpesanan = id)
    pemesananall = models.pemesanan.objects.all()
    bajuall = models.baju.objects.all()
    if request.method == "GET":
        return render(request, "updatedatadetailpesanan.html",{
            'detailpesanan' : detailpesananobj,
            'pemesananall' : pemesananall,
            'bajuall' : bajuall
        })
    else :
        detailpesananobj.pemesanan = request.POST['IDpemesanan']
        pemesananbaru = models.pemesanan.objects.get(IDpemesanan = request.POST['IDpemesanan'])
        detailpesananobj.IDpemesanan = pemesananbaru
        detailpesananobj.baju = request.POST['IDbaju']
        bajubaru = models.baju.objects.get(IDbaju = request.POST['IDbaju'])
        detailpesananobj.IDbaju = bajubaru
        detailpesananobj.Jeniskain = request.POST['Jeniskain']
        detailpesananobj.Ukuranbaju = request.POST['Ukuranbaju']
        detailpesananobj.Jumlahitempesanan = request.POST['Jumlahitempesanan']
        detailpesananobj.save()
        return redirect('detailpesanan')

def deletedatadetailpesanan(request,id):
    detailpesananobj = models.detailpesanan.objects.get(IDdetailpesanan = id)
    detailpesananobj.delete()
    return redirect('detailpesanan')

def detailtambahan(request):
    data =[]
    detailtambahanall = models.detailtambahan.objects.all()    
    for item in detailtambahanall:
        dummy =[]
        detailtambahan = item.IDdetailtambahan
        tambahan = models.tambahan.objects.filter(detailtambahan = detailtambahan)
        dummy.append(item)
        dummy.append(tambahan)
        data.append(dummy)
    return render(request, 'detailtambahan.html',{
        "detailtambahanall" : detailtambahanall,
    })

def createdatadetailtambahan (request):
    pemesananall = models.pemesanan.objects.all()
    tambahanall = models.tambahan.objects.all()
    if request.method == "GET":
        return render(request, 'createdatadetailtambahan.html', {
            'pemesananall' : pemesananall,
            'tambahanall' : tambahanall
        })
    else :
        IDpemesanan = request.POST['IDpemesanan']
        pemesananget = models.pemesanan.objects.get(IDpemesanan = IDpemesanan)
        pemesananobj = pemesananget
        IDtambahan = request.POST['IDtambahan']
        tambahanget = models.tambahan.objects.get(IDtambahan = IDtambahan)
        tambahanobj = tambahanget
        Jumlahitemtambahan = request.POST['Jumlahitemtambahan']

        newdetailtambahan = models.detailtambahan(
            IDpemesanan = pemesananobj,
            IDtambahan = tambahanobj,
            Jumlahitemtambahan = Jumlahitemtambahan,
        ).save()
        return redirect('detailtambahan')

def updatedatadetailtambahan(request,id):
    detailtambahanobj = models.detailtambahan.objects.get(IDdetailtambahan = id)
    pemesananall = models.pemesanan.objects.all()
    tambahanall = models.tambahan.objects.all()
    if request.method == "GET":
        return render(request, "updatedatadetailtambahan.html",{
            'detailtambahan' : detailtambahanobj,
            'pemesananall' : pemesananall,
            'tambahanall' : tambahanall
        })
    else :
        detailtambahanobj.pemesanan = request.POST['IDpemesanan']
        pemesananbaru = models.pemesanan.objects.get(IDpemesanan = request.POST['IDpemesanan'])
        detailtambahanobj.IDpemesanan = pemesananbaru
        detailtambahanobj.tambahan = request.POST['IDtambahan']
        tambahanbaru = models.tambahan.objects.get(IDtambahan = request.POST['IDtambahan'])
        detailtambahanobj.IDtambahan = tambahanbaru
        detailtambahanobj.Jumlahitemtambahan = request.POST['Jumlahitemtambahan']
        detailtambahanobj.save()
        return redirect('detailtambahan')

def deletedatadetailtambahan(request,id):
    detailtambahanobj = models.detailtambahan.objects.get(IDdetailtambahan = id)
    detailtambahanobj.delete()
    return redirect('detailtambahan')