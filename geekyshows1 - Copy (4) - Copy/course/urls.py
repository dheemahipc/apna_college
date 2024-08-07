from django.urls import path
from .views import import_excel

urlpatterns = [
    path('', import_excel, name='import_excel'),
]
