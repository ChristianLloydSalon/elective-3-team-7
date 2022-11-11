from django.shortcuts import render, redirect
from turtle import pos
from .models import *
from django.contrib import messages 

def home(request):
    emp_data = Employee.objects.filter()
    on_leave = emp_data.filter(on_leave=True)
    d = {'total_employee':emp_data.count(), 'on_leave':on_leave.count()}
    return render(request, 'admin_dashboard.html',d)

def createEmployeee(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        region = request.POST['region']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        position = request.POST['position']
        emp_obj = Employee.objects.create(name=name,dob=dob,doj=doj,address=address,city=city,region=region,zipcode=zipcode,country=country,department=department,position=position)
        messages.success(request, "Employee created successfully")
        return redirect('employee_list')
    return render(request, 'create_employeee.html')

def employee_list(request):
    emp_data = Employee.objects.filter()
    d = {'employee':emp_data}
    return render(request, 'employee_list.html',d)

def edit_employee(request, pid):
    emp_data =Employee.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        city = request.POST['city']
        region = request.POST['region']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        position = request.POST['position']
        emp_obj = Employee.objects.filter(id=pid).update(name=name,dob=dob,doj=doj,address=address,city=city,region=region,zipcode=zipcode,country=country,department=department,position=position)
        messages.success(request, "Employee Updated successfully")
        return redirect('employee_list')
    return render(request, 'edit_employeee.html', {'emp_data':emp_data})

def delete_employee(request, pid):
    data = Employee.objects.get(id=pid)
    data.delete()
    messages.success(request, "Employee Deleted successfully")
    return redirect('employee_list')

def leave_status(request, pid):
    data = Employee.objects.get(id=pid)
    if data.on_leave:
        data.on_leave = False
    else:
        data.leave_count = data.leave_count + 1
        data.on_leave = True
    data.save()
    messages.success(request, "Employee leave status Changed successfully.")
    return redirect('employee_list')
