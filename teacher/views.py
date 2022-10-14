from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'login.html')


def bGrid(request):
    return render (request,'new.html')


def bbootstrap(request):
    return render (request,'bootstrapgrid.html')


def new(request):
    return render (request,'teacher/new.html')


def baabtra(request):
    return render (requet,'teacher/baabtra.html')

    