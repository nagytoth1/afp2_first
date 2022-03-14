from django.db.models.base import Model
from django.db import models

class Subject(Model): # CREATE TABLE Tárgy
    subject_name = models.CharField(max_length=200) #question_text varchar(200)
    def __str__(self):
        return self.subject_name

class Task(Model):
    description = models.TextField() # feladat leírása
    subject = models.ForeignKey(Subject, default=None, on_delete=models.DO_NOTHING, related_name='subject')
    difficulty = models.SmallIntegerField() #1-2-3-nehézségek

    def __str__(self) -> str:
        return f"{self.subject} \t {self.description} \t Nehézség: {self.difficulty}"