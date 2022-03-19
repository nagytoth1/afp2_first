from django.db.models.base import Model
from django.db import models

class Subject(Model): # CREATE TABLE Tárgy
    subject_name = models.CharField(max_length=200) #question_text varchar(200)
    def __str__(self):
        return self.subject_name

class Type(Model):
    type_name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.type_name

class Task(Model):
    description = models.TextField() # feladat leírása
    difficulty = models.SmallIntegerField() #1-2-3-nehézségek
    subject = models.ForeignKey(Subject, default=None, on_delete=models.DO_NOTHING, related_name='subject')
    type = models.ForeignKey(Type, default=None, on_delete=models.DO_NOTHING, related_name='type')

    def __str__(self) -> str:
        return f"{self.subject} \t {self.description} \t Nehézség: {self.difficulty}"