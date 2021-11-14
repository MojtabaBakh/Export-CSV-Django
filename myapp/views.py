from django.shortcuts import render
from . models import Student
from django.http import HttpResponse
import datetime
import csv
import xlwt
from django.template.loader import get_template
from xhtml2pdf import pisa




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



def export_excel(response):
    response=HttpResponse(content_type="apllication/ms-excel")
    response["content-Disposition"]='attachment ; filename=students'+str(datetime.datetime.now())+'.xls'
    
    workbook=xlwt.Workbook(encoding='utf-8')
    worksheet=workbook.add_sheet("students")
    columns=['id' , 'Name' , 'Last Name' , 'Student Code']
    rownumber=0
    
    for col in range(len(columns)):
        worksheet.write(rownumber , col , columns[col])
        
    students=Student.objects.all().values_list('id' , 'Name' , 'Family' , 'Code')
    
    for std in students:
        rownumber+=1
        
        for col in range(len(std)):
            worksheet.write(rownumber , col , std[col])
    
    
    workbook.save(response)
    return response


def export_pdf(request):
    response=HttpResponse(content_type="apllication/pdf")
    response["content-Disposition"]='attachment ; filename=students'+str(datetime.datetime.now())+'.pdf'
    
    template_path="myapp/studentspdf.html"
    template=get_template(template_path)
    students=Student.objects.all()
    context={"students": students}
    html=template.render(context)
    pisa.CreatePDF( html , dest=response  )
    return response
