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

    # if the request method is POST and send by save & continue button, exacute ...
    if request.method == 'POST' and 'save-go' in request.POST:
        year = request.POST.get('year')
        if year == 'All':
            classes = obj.classes.all()
        else:
            classes = obj.classes.filter(year__year=str(year))

        # Get the selected courses and save them in a session so that they can be kept selected until they are send to 
        # drawPDF function.
        selected_values = request.POST.getlist('courses')

        if not 'selected_values' in request.session or not request.session['selected_values']:
            request.session['selected_values'] = [int(i) for i in selected_values] 
        else:
            saved_list = request.session['selected_values']
            for value in selected_values:
                if value not in saved_list:
                    saved_list.append(int(value))
            request.session['selected_values'] = saved_list

        selected_courses = request.session['selected_values']
        print(selected_courses)

    # if the request methof is POST and send by generate pdf button, create the pdf file and download it.
    elif request.method == 'POST' and 'generate-pdf' in request.POST:
        classes = request.POST.getlist('courses')
        pdf = helpers.drawPDF(classes, obj)
        return pdf
    
    # if the request method is GET, get all classes and clear the selected courses
    else:
        classes = obj.classes.all()
        selected_values = request.session.get('courses', [])
        saved_list = []
        request.session['selected_values'] = []
        selected_courses = []

    
    context = {'object': obj, 'classes': classes, "form": year_form, 'selected_courses': selected_courses}
    return render(request, 'dashboard/detail.html', context)


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
