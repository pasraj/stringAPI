from django.urls import path
from operationApp.views import *

urlpatterns = [
    path("string/", putString, name="put"),
    path("operation/",operation, name="operation"),
    path("operation_info/",get_operation, name="get_operation" )
]
