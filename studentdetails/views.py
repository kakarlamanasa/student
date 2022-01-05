from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .form import StudentForm
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            email=request.POST.get('email')
            password=request.POST.get('password')
            User=authenticate(request,email=email,password=password)
            if User is not None:
                login(request,user)
                return redirect('/')
            context={}
            return render(request,'app/studentlogin.html',context)
def logoutpage(request):
    logout(request)
    return redirect('/')

def student_list(request):
    students = Student.objects.all()
    paginator= paginator(students,1)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)
    context = {
        "students":paged_students
    }
    return render(request,"studentdetails/student_list.html",context)
def single_student(request,student_id):
    single_student = get_objects_or_404(Student,pk=student_id)
    context ={
        "single_student":single_student
    }
    return render(request,"studentdetails/student_details.html",context)
def student_regi(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        context = {
            "forms": forms
        }
        if form.is_valid():
            form.save()
            messages.sucess(request,"Student registration successfully completed!")
            return redirect("student_list")
        else:
            forms=StudentForm()

    return render(request,"studentdetails/registration.html",context)
def edit_student(request,pk):
    student_edit = Student.objects.get(id=pk)
    edit_form = StudentForm(instance=student_edit)
    if request.method=="POST":
        edit_form.save()
        messages.success (request,"edit student info sucessfully!" )
        return redirect("student_list")
    context={
        "edit_form":edit_form
    }
    return render(request,"studentdetails/edit_student.html",context)
def delete_student(request,student_id):
    student_delete=Student.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request,"delete student info successfully!")
    return redirect("student_list")