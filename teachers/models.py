from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'
