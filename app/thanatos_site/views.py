from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Subject

def mainPage(request):
    subjects = Subject.objects.all() # összes adatot lekérjük (Select *)
    
    queryparam_subject = request.GET.get('subject')
    
    if queryparam_subject is None or queryparam_subject == '':
        return render(request, 'main.html',{'subjects_names':subjects})
    else:
        subject_data:Subject = Subject.objects.get(pk=queryparam_subject)
        return HttpResponse(f'<h1>{subject_data.subject_name}</h1>')