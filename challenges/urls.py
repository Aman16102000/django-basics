from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge_text, name="month-challenge-url"),
    path("", views.all_months_list),
]
