from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        log = request.POST.get("l")
        par = request.POST.get("p")
        user = authenticate(request, username=log, password=par)
        if user is None:
            return redirect("login")
        login(request, user)
        return redirect("bolim")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

