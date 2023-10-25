# urls.py

from django.urls import path
from . import views
from views import *

urlpatterns = [
    path('powers/', views.get_powers, name='get_powers'),
    path('powers/<int:id>/', views.get_power_by_id, name='get_power_by_id'),
]
