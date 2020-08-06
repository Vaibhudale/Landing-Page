from django.shortcuts import render
from django.http import HttpResponse
from .models import Carorder

def index(request):
    return render(request, "signin.html")
def send_details(request):
    name = request.POST["name"]
    email = request.POST["email"]
    address = request.POST["address"]
    carmodel = request.POST["carmodel"]
    timeslot = request.POST["timeslot"]

    car_order_obj = Carorder(name=name, email=email, address=address, carmodel=carmodel, timeslot=timeslot)
    car_order_obj.save()
    return render(request, 'newfile.html')