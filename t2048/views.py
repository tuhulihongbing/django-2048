from django.shortcuts import render

# Create your views here.

def show_2048(request):
    return render(request, 'index.html')