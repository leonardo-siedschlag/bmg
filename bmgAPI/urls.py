from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validaçãoToken/<str:numeroSolicitado>/', views.validatorTokenView, name='validatorTokenView'),
]