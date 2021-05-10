from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

'''#model object - Single data 
def get_student_detail(request, ip):
    stu = Student.objects.get(id = ip)
    serializer = StudentSerializer(stu)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

#QuerySet - All data
def get_student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def post_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg' : 'Data Saved Successfully!'}
            #json_response = JSONRenderer().render(json_response)
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)'''

@csrf_exempt
def api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            data = Student.objects.get(id = id)
            serializer = StudentSerializer(data)
            return JsonResponse(serializer.data, safe=False)
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg' : 'Data Saved Successfully!'}
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id =  python_data.get('id')
        data = Student.objects.get(id = id)
        serializer = StudentSerializer(data, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg' : 'Data Updated Successfully!'}
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id =  python_data.get('id')
        data = Student.objects.get(id = id)
        data.delete()
        response_msg = {'msg' : 'Data Deleted Successfully!'}
        return JsonResponse(response_msg, safe=True)

