from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from . import forms as dashboard_forms
<<<<<<< HEAD
from .models import Student, Score
=======
from .models import Student, Score, Class
>>>>>>> 48a3010 (fix generate pdf functionality)
from django.http import HttpResponse
from reportlab.pdfgen import canvas


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

<<<<<<< HEAD
def grades_pdf(request):
=======
def grades_pdf(request, id):
        
    if request.method == 'POST':
        
>>>>>>> 48a3010 (fix generate pdf functionality)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="grades_report.pdf"'

        p = canvas.Canvas(response)

<<<<<<< HEAD
        year = request.POST.get('year')

        student_id = request.POST.get('id')
        obj = get_object_or_404(Student, pk=student_id)

        if year == 'All':
            classes = obj.classes.all()
        else:
            classes = obj.classes.filter(year__year=str(year))

        for class_obj in classes:
            scores = Score.objects.filter(studentid=obj, classes_taken=class_obj)
            p.drawString(100, 100, f"Class: {class_obj.classname}")
=======
        # year = request.POST.get('year')

        student_id = id
        obj = get_object_or_404(Student, pk=student_id)
        classes = request.POST.getlist('courses[]')
        print(classes)

        for class_obj in classes:
            scores = Score.objects.filter(studentid=obj, classes_taken=class_obj)
            class_name = Class.objects.get(classid=class_obj).classname

            print(class_obj)

            p.drawString(100, 100, f"Class: {class_name}")
>>>>>>> 48a3010 (fix generate pdf functionality)
            p.drawString(100, 120, "Scores:")
            y_position = 140

            for score in scores:
<<<<<<< HEAD
                p.drawString(120, y_position, f"Subject: {Score.classes_taken.classname}")
=======
                p.drawString(120, y_position, f"Subject: {Score.classes_taken}")
>>>>>>> 48a3010 (fix generate pdf functionality)
                p.drawString(120, y_position + 20, f"Score: {Score.score}")
                y_position += 40

            #p.showPage()

        # Save the PDF
        p.save()

        return response


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
