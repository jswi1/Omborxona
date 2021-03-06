from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor

class MahsulotView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            m = Mahsulot.objects.filter(ombor=o)
            return render(request, "products.html", {"products":m})
        return redirect("login")

    def post(selfself, request):
        o = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom = request.POST.get("n"),
            brend = request.POST.get("b"),
            miqdor = request.POST.get("m"),
            kelgan_narx = request.POST.get("kn"),
            sotuv_narx = request.POST.get("sn"),
            ombor = o
        )
        return redirect("mahsulotlar")


class MahsulotEdit(View):
    def get(self, request, pk):
        m = Mahsulot.objects.get(id=pk)
        return render(request, "product_update.html", {"product":m})

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            miqdor=request.POST.get("m"),
            kelgan_naex=request.POST.get("kn"),
            sotuv_narx=request.POST.get("sn"),
        )
        return redirect("mahsulotlar")


class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            m = Mahsulot.objects.filter(ombor=o)
            return render(request, "client.html", {"clients":m})
        return redirect("login")

    def post(selfself, request):
        o = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            ism = request.POST.get("i"),
            dokon = request.POST.get("d"),
            tel=request.POST.get("t"),
            manzil = request.POST.get("m"),
            qarz = request.POST.get("q"),
            ombor = o
        )
        return redirect("clientlar")


class ClientEdit(View):
    def get(self, request, az):
        c = Client.objects.get(id=az)
        return render(request, "client_update.html", {"client":c})

    def post(self, request, az):
        Mahsulot.objects.filter(id=az).update(
            miqdor=request.POST.get("m"),
            kelgan_naex=request.POST.get("kn"),
            sotuv_narx=request.POST.get("sn"),
        )
        return redirect("clientlar")

class BolimView(View):
    def get(self, request):
        return render(request, "bulimlar.html")