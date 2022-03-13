from django.shortcuts import redirect, render

def mainPage(request):
    return render(request, 'main.html')