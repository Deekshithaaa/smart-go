from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('vacation/',views.vacation,name='vacation'),
    path('fri/',views.fri,name='fri'),
    path('fam/',views.fam,name='fam'),
    path('per/',views.per,name='per'),
    path('sin/',views.sin,name='sin'),
    path('fam2/',views.fam2,name='fam2'),
    path('part1/',views.part1,name='part1'),
    path('vacdet/',views.vacdet,name='vacdet'),
    path('hhh/',views.hhh,name='hhh'),
    ]
