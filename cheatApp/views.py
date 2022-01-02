from django.shortcuts import render

# Create your views here.


def home_view(request):


    return render(request, 'base.html' )



def mySheets(request):

    return render(request, 'MySheets\sheets.html')
