from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CarModel
from bson import ObjectId
from .forms import CarForm
from bson import ObjectId
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")

def car_list_view(request):
    car_model = CarModel()
    cars = car_model.get_all_cars()
    
    # Rename '_id' field to 'id' for template access
    for car in cars:
        car['id'] = str(car['_id'])  # Convert ObjectId to string
    
    return render(request, 'car_list.html', {'cars': cars})

def car_detail_view(request, car_id):
    car_model = CarModel()
    car = car_model.get_car_by_id(ObjectId(car_id))
    
    # Rename '_id' field to 'id' for template access
    car['id'] = str(car['_id'])  # Convert ObjectId to string
    
    return render(request, 'car_detail.html', {'car': car})

def add_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # Insert the new car data
            car_model = CarModel()
            car_model.insert_car(form.cleaned_data)
            return redirect('car-list')
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})

def delete_car_view(request, car_id):
    car_model = CarModel()
    car_model.collection.delete_one({'_id': ObjectId(car_id)})
    return redirect('car-list')