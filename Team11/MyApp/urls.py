from django.urls import path
from . import views
urlpatterns = [
    path('',views.Counter_Status,name = "home_page")
]