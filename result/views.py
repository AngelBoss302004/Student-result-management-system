from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentResultView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        name = form_data.get("name")
        mark1 = form_data.get("mark1")
        mark2 = form_data.get("mark2")
        mark3 = form_data.get("mark3")

        total = mark1 + mark2 + mark3
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Failed"

        result = {
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        return JsonResponse(result)