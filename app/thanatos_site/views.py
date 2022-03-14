from django.shortcuts import redirect, render
from . models import Subject

def mainPage(request):
    subjects = Subject.objects.all() # összes adatot lekérjük (Select *)
    
    return render(request, 'main.html',{'subjects_names':subjects})