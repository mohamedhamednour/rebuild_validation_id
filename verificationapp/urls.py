from django.urls import path
from . import views

urlpatterns = [

    path('valid_id/', views.ValidationView.as_view(), name='valid_id'),
]