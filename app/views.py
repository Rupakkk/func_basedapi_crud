from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

@api_view('GET','POST','PUT','DELETE')
def student_api(request)

