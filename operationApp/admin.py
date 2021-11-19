from django.contrib import admin
from operationApp.models import String,OperationTransaction

# Register your models here.

admin.site.register([String, OperationTransaction])
