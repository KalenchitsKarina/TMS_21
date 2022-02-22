from django.urls import path

from .views import use_form

urlpatterns = [
    path('', use_form),
    path('show/', use_form),
    path('save/', use_form),
]