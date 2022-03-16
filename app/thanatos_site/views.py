from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Subject
from django.core.exceptions import ObjectDoesNotExist

def mainPage(request):
    subjects = Subject.objects.all() # összes adatot lekérjük (Select *)
    
    queryparam_subject = request.GET.get('s')
    
    #ha még nincs megadva subject query-paraméterként (s nincs beállítva vagy üres), akkor a főoldalt dobja ki
    if queryparam_subject is None or queryparam_subject == '':
        return render(request, 'main.html',{'subjects_names':subjects})
    #ha be van állítva az s értéke, akkor tudjuk, hogy melyik tárgyat kell lekérni
    else:
        try:
            subject_data:Subject = Subject.objects.get(pk=queryparam_subject)
        #ha nem létezik, pl. s=32 van beállítva, akkor kivételkezelés, dobjon vissza a főoldalra
        except ObjectDoesNotExist: 
            return redirect('home')
        return HttpResponse(f'<h1>{subject_data.subject_name}</h1>')