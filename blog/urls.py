from django.urls import path
from . import views

urlpatterns = [
    path('lista_de_posts', views.post_list, name='post_list'),
]