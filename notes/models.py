from django.db import models
from students.models import Student
from classes.models import Class

class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='notes')
    subject = models.CharField(max_length=100)  
    content = models.TextField()  
    date_created = models.DateField(auto_now_add=True)  
    last_updated = models.DateField(auto_now=True) 

    def __str__(self):
        return f'Note for {self.student} - {self.subject}'

    class Meta:
        ordering = ['student', 'class_name', 'subject']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
