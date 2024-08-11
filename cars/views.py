from django.shortcuts import render
import cars



def cars_view(request):
    return render(request,'cars.html')
