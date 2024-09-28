from django.urls import path
from . import views


urlpatterns = [
    path('ba',views.base),
    path('',views.watch),


]