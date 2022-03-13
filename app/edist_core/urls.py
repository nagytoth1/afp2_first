from django.contrib import admin
from django.urls import path, include
import Edist_Site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Edist_Site.urls'))
    
]
