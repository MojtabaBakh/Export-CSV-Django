from django.db import models
from django.urls import reverse



class Student(models.Model):
    Name=models.CharField(max_length=100)
    Family=models.CharField(max_length=100)
    Code=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return super().__str__()
    
    
    def get_absolute_url(self):
        return reverse("studentdetails", args=[self.id])
    
