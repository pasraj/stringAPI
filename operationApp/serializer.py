from rest_framework import serializers
from operationApp.models import String,OperationTransaction

class StringSerializer(serializers.ModelSerializer):
    class Meta:
        model = String
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationTransaction
        fields = ['operation', 'before', 'after']