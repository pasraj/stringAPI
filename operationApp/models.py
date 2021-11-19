from django.db import models

OPERATION_CHOICES = [
    ("REVERSE", "REVERSE"),
    ("REVERSE WORD", "REVERSE WORD"),
    ("FLIP BREAK", "FLIP BREAK"),
    ("SORT CHARACTERS", "SORT CHARACTERS")

]

class String(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OperationTransaction(models.Model):
    string = models.ForeignKey(String, on_delete=models.CASCADE)
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    before = models.CharField(max_length=100, null=True)
    after = models.CharField(max_length=100, null=True)

    def __str__(self):
        result = self.string.name + " " + self.operation
        return result
    
