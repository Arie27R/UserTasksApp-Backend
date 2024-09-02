from rest_framework import serializers 
from TaskApp.models import Tasks

class TaskSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tasks
        fields = '__all__'
