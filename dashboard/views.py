from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from . import forms as dashboard_forms
from .models import Student, Score, Class
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from . import helpers

def index(request):
    obj = Student.objects.all()
    return render(request, "dashboard/index.html", {"obj": obj})


@csrf_exempt
def detail(request, id=None):

    obj = get_object_or_404(Student, pk=id)
    year_form = dashboard_forms.YearForm(request.POST or None)

    if request.method == 'POST':
        year = request.POST.get('year')
        if year == 'All':
            classes = obj.classes.all()
        else:
            classes = obj.classes.filter(year__year=str(year))
    else:
        classes = obj.classes.all()

    context = {'object': obj, 'classes': classes, "form": year_form}
    return render(request, 'dashboard/detail.html', context)


def grades_pdf(request, id):
        
    if request.method == 'POST':
        # year = request.POST.get('year')

        student_id = id
        obj = get_object_or_404(Student, pk=student_id)
        classes = request.POST.getlist('courses[]')
        print(classes)

        pdf = helpers.drawPDF(classes, obj)
        # Save the PDF

    return pdf


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            error_message = "Username or Password is incorrect!"
            return render(request, "home/login.html", {"error_message": error_message})

    return render(request, "home/login.html")


def logout(request):
    return redirect("login")


def dashboard(request):
    return redirect("login")
