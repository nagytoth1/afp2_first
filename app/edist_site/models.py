import datetime

from django.db.models.base import Model
from django.db import models
from django.utils import timezone

class Subject(Model): # CREATE TABLE Tárgy
    subject_name = models.CharField(max_length=200) #question_text varchar(200)
    def __str__(self):
        return self.subject_name

