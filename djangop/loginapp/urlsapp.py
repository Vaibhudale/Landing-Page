from django.urls import path
from .import views
urlpatterns=[
    path('', views.index, name="login"),
    path('send_details/',views.send_details,name="car")
]
