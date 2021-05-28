from django.db import models


class Salary(models.Model):
    salary = models.CharField(max_length=100)


class Upload(models.Model):
    upload_file = models.FileField()
