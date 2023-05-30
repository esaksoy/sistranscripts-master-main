from .models import Student, Score, Class
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def drawPDF(classes, student_id):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="grades_report.pdf"'
    p = canvas.Canvas(response)

    for class_obj in classes:
        scores = Score.objects.filter(studentid=student_id, classes_taken=class_obj)
        class_name = Class.objects.get(classid=class_obj).classname

        print(class_obj)

        p.drawString(100, 100, f"Class: {class_name}")
        p.drawString(100, 120, "Scores:")
        y_position = 140

        for score in scores:
            p.drawString(120, y_position, f"Subject: {Score.classes_taken}")
            p.drawString(120, y_position + 20, f"Score: {Score.score}")
            y_position += 40

        # p.showPage()
    p.save()

    return response