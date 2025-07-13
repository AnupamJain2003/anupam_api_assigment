from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()
    status = models.CharField(default='Saved', max_length=50)

class BogieChecksheet(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()
    status = models.CharField(default='Saved', max_length=50)
