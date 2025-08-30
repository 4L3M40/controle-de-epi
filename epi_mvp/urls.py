from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("colaboradores/", include("colaboradores.urls", namespace="colaboradores")),
    path("", lambda r: HttpResponseRedirect("/colaboradores/")),
]
