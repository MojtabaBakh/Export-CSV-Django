from django.shortcuts import render
from . models import Student
from django.http import HttpResponse
import datetime
import csv



def student_list(request):
    students=Student.objects.all()
    
    return render(request , 'myapp/studentlist.html' , {'students':students})



def student_details( request , pk) :
    student=Student.objects.get(id = pk)
    return render(request , 'myapp/studentdetails.html' , {'student':student})



def Export_students(request):
    response=HttpResponse(content_type="text/csv")
    response["content-Disposition"]='attachment ; filename=students'+str(datetime.datetime.now())+'.csv'
    writer=csv.writer(response)
    writer.writerow(['id' , 'Name' , 'Last Name' , 'Student Code'])
    students=Student.objects.all()
    for student in students :
        writer.writerow([student.id , student.Name , student.Family , student.Code])
    return response
    
    
