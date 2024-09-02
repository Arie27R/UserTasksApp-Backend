# TaskApp/views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from TaskApp.models import Tasks
from TaskApp.serializers import TaskSerializer

@csrf_exempt
def taskApi(request, id=0):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        tasks_serializer = TaskSerializer(data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)  # Retorna un diccionario
        return JsonResponse({"message": "Failed to Add.", "errors": tasks_serializer.errors}, status=400)  # Retorna un diccionario
    
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        try:
            task = Tasks.objects.get(TaskId=task_data['TaskId'])
        except Tasks.DoesNotExist:
            return JsonResponse({"message": "Task not found."}, status=404)
        
        tasks_serializer = TaskSerializer(task, data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse({"message": "Updated Successfully"}, status=200)
        return JsonResponse({"message": "Failed to Update.", "errors": tasks_serializer.errors}, status=400)
    
    elif request.method == 'DELETE':
        try:
            task = Tasks.objects.get(TaskId=id)
        except Tasks.DoesNotExist:
            return JsonResponse({"message": "Task not found."}, status=404)
        
        task.delete()
        return JsonResponse({"message": "Deleted Successfully"}, status=200)

