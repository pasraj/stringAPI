from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from operationApp.serializer import StringSerializer, OperationSerializer
from operationApp.models import String,OperationTransaction

import json
from django.http import StreamingHttpResponse

def get_string_obj(id):
    try:
        return String.objects.get(id=id)
    except:
        return "String Does not exist"

def reverseString(string):
    return string[::-1]

def reverse_word(string):
	string = string.split(" ")
	string = " ".join(reversed(string))
	return string

def flipBreak(string):
	n = len(string)
	half = n//2
	result = ""
	for i in range(half,n):
		result+=string[i]
	for i in range(0,half):
		result+=string[i]
	return result

def sortstring(string):
	string = "".join(sorted(string))
	return string


@api_view(["POST","GET"])
def putString(request):
    if request.method=="GET":
        string = String.objects.all()
        serializer =StringSerializer(string, many=True)
        return Response(serializer.data)


    if request.method == "POST":
        serializer = StringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.get('id'), status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(["POST", "GET"])
def operation(request):
    if request.method=="POST":
        data_string = json.dumps(request.data)
        json_data = json.loads(data_string)
        operation = json_data.get("operation")
        id = json_data.get("id")
        print(operation)
        string_obj = get_string_obj(id)
        string = string_obj.name
        result = ""
        if operation=="reverse":
            result = reverseString(string)
            string_obj.name = result
            trans = OperationTransaction(string=string_obj,operation="REVERSE",before=string, after=result)
            trans.save()
            string_obj.save()
        elif operation=="reverse_word":
            result = reverse_word(string)
            string_obj.name = result
            trans = OperationTransaction(string=string_obj, operation="REVERSE WORD",before=string, after=result)
            trans.save()
            string_obj.save()
            print(result + " resvese")
        elif operation=="flip_break":
            result = flipBreak(string)
            string_obj.name = result
            trans = OperationTransaction(string= string_obj, operation="FLIP BREAK",before=string, after=result)
            string_obj.save()
            trans.save()
        elif operation=="sort_char":
            result = sortstring(string)
            trans = OperationTransaction(string= string_obj, operation="SORT CHARACTERS",before=string, after=result)
            string_obj.name = result
            string_obj.save()
            trans.save()
        else:
            return Response("Enter correct operation")
        return Response(id)
    
    if request.method=="GET":
        return Response('send operation and id in json format ::  operations => reverse, reverse_word, flip_break, sort_char ')


@api_view(["POST"])
def get_operation(request):
    obj = get_string_obj(request.data.get("id"))
    trans = OperationTransaction.objects.filter(string=obj)
    print(trans)
    serializer = OperationSerializer(trans ,many=True)
    return Response(serializer.data)