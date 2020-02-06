from django.urls import path

from . import views

urlpatterns = [
    path('',views.pivo, name = 'pivo'),
    path('go',views.goodJob, name = 'go'),
    path('basis',views.basis, name = 'basis'),
]