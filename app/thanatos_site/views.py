from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Subject
from . models import Task
from django.core.exceptions import ObjectDoesNotExist

def mainPage(request):
    subjects = Subject.objects.all() # összes adatot lekérjük (Select *)
    subject_tasks = Task.objects.all() #az összes feladat lekérése későbbi szűrésre
    queryparam_subject = request.GET.get('id')
    
    #ha még nincs megadva subject query-paraméterként (s nincs beállítva vagy üres), akkor a főoldalt dobja ki
    if queryparam_subject is None or queryparam_subject == '':
        return render(request, 'main.html',{'subjects_names':subjects})
    #ha be van állítva az s értéke, akkor tudjuk, hogy melyik tárgyat kell lekérni
    else:
        curr_subject = subjects.filter(id__exact=queryparam_subject) #lekérem id alapján a kiválasztott tárgyat
        filtered_tasks = subject_tasks.filter(subject__exact=curr_subject.first()) # a first()-el megkapom a tárgy nevét stringként és arra szűrök
        
        try:
            subject_data:Subject = Subject.objects.get(pk=queryparam_subject)
        #ha nem létezik, pl. s=32 van beállítva, akkor kivételkezelés, dobjon vissza a főoldalra
        except ObjectDoesNotExist: 
            return redirect('home')
        return render(request, 'tasks.html', {'tasks':filtered_tasks})