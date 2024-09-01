from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,'index.html')
def buses(request):
    return render(request,'buses.html')
def drivers(request):
    return render(request,'drivers.html')
def routes(request):
    return render(request,'routes.html')
def staff(request):
    return render(request,'staff.html')




