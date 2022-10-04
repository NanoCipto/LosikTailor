from django.shortcuts import render,redirect
from . import models

# Create your views here.

# Ambil data pelanggan

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

        newpemesanan = models.pemesanan(
            IDpelanggan = pelangganobj,
            tanggalpemesanan = tanggalpemesanan
        ).save()
        return redirect('pemesanan')

def updatedatapemesanan(request,id):
    pemesananobj = models.pemesanan.objects.get(IDpemesanan = id)
    if request.method == "GET":
        return render(request, "updatedatapemesanan.html",{
            'pemesanan' : pemesananobj
        })
    else :
        pemesananobj.IDpelanggan = request.POST['IDpelanggan']
        pemesananobj.tanggalpemesanan = request.POST['tanggalpemesanan']
        pemesananobj.save()
        return redirect('pemesanan')

def deletedatapemesanan(request,id):
    pemesananobj = models.pemesanan.objects.get(IDpemesanan = id)
    pemesananobj.delete()
    return redirect('pemesanan')

def detailpesanan(request):
    detailpesananall = models.detailpesanan.objects.all()

    return render(request, 'detailpesanan.html',{
        "detailpesananall" : detailpesananall,
    })

def createdatadetailpesanan (request):
    if request.method == "GET":
        return render(request, 'createdatadetailpesanan.html')
    else :
        IDpemesanan = request.POST['IDpemesanan']
        IDbaju = request.POST['IDbaju']
        Jeniskain = request.POST['Jeniskain']
        Ukuranbaju = request.POST['Ukuranbaju']
        Jumlahitempesanan = request.POST['Jumlahitempesanan']

        newdetailpesanan = models.detailpesanan(
            IDpemesanan = IDpemesanan,
            IDbaju = IDbaju,
            Jeniskain = Jeniskain,
            Ukuranbaju = Ukuranbaju,
            Jumlahitempesanan = Jumlahitempesanan
        ).save()
        return redirect('detailpesanan')

def updatedetailpesanan(request,id):
    detailpesananobj = models.detailpesanan.objects.get(IDdetailpesanan = id)
    if request.method == "GET":
        return render(request, "updatedatadetailpesanan.html",{
            'detailpesanan' : detailpesananobj
        })
    else :
        detailpesananobj.IDpemesanan = request.POST['IDpemesanan']
        detailpesananobj.IDbaju = request.POST['IDbaju']
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
    detailtambahanall = models.detailtambahan.objects.all()

    return render(request, 'detailtambahan.html',{
        "detailtambahanall" : detailtambahanall,
    })

def createdatadetailtambahan (request):
    if request.method == "GET":
        return render(request, 'createdatadetailtambahan.html')
    else :
        IDdetailtambahan = request.POST['IDdetailtambahan']
        IDpemesanan = request.POST['IDpemesanan']
        IDtambahan = request.POST['IDtambahan']
        Jumlahitemtambahan = request.POST['Jumlahitemtambahan']

        newdetailtambahan = models.detailtambahan(
            IDdetailtambahan = IDdetailtambahan,
            IDpemesanan = IDpemesanan,
            IDtambahan = IDtambahan,
            Jumlahitemtambahan = Jumlahitemtambahan,
        ).save()
        return redirect('detailtambahan')

def updatedetailtambahan(request,id):
    detailtambahanobj = models.detailtambahan.objects.get(IDdetailtambahan = id)
    if request.method == "GET":
        return render(request, "updatedatadetailtambahan.html",{
            'detailtambahan' : detailtambahanobj
        })
    else :
        detailtambahanobj.IDdetailtambahan = request.POST['IDdetailtambahan']
        detailtambahanobj.IDpemesanan = request.POST['IDpemesanan']
        detailtambahanobj.Jumlahitemtambahan = request.POST['Jumlahitemtambahan']
        detailtambahanobj.save()
        return redirect('detailtambahan')

def deletedatadetailtambahan(request,id):
    detailtambahanobj = models.detailtambahan.objects.get(IDdetailtambahan = id)
    detailtambahanobj.delete()
    return redirect('detailtambahan')

