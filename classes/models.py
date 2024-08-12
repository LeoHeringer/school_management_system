from django.db import models
from students.models import Student
from teachers.models import Teacher

class Class(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    students = models.ManyToManyField(Student, related_name='classes')
    
    def __str__(self):
        return f'{self.name} - {self.year}'
