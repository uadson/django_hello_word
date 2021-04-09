from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    # mysite/
    path('', views.index, name='index'),
    # mysite/nome
    path('<nome>/', views.nome, name='nome'),
    # mysite/soma/10/20
    path('soma/<int:num1>/<int:num2>/', views.soma, name='soma'),
    # mysite/sub/20/10
    path('sub/<int:num1>/<int:num2>/', views.sub, name='sub'),
    # mysite/mult/10/20
    path('mult/<int:num1>/<int:num2>/', views.mult, name='mult'),
    # mysite/dividir/20/10
    path('dividir/<int:num1>/<int:num2>/', views.dividir, name='dividir'),
    
]