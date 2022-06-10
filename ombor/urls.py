from django.contrib import admin
from django.urls import path, include
from userapp.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="login"),
    path('user/', include("userapp.urls")),
    path('asosiy/', include("asosiy.urls")),
    path('mahsulot_edit/', include("asosiy.urls")),

]
