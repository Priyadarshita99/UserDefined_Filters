from django.shortcuts import render

# Create your views here.
def userfilters(request):
    d={'data':'Hey there! How Are You'}
    return render(request,'userfilters.html',d)