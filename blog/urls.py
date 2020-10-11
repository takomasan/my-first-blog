from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # post_list という名前のでビューをルートURLに割り当て 
]