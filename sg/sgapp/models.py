from django.db import models


class Fri(models.Model):
    user_name = models.CharField(max_length=200)
    Q1 = models.CharField(max_length=200)
    Q2 = models.CharField(max_length=200)
    Q3 = models.CharField(max_length=200)
    Q4 = models.CharField(max_length=200)
    Q5 = models.CharField(max_length=200)
    Q6 = models.CharField(max_length=200)
    Q7 = models.CharField(max_length=200)
    Q8 = models.CharField(max_length=200)
    Q9 = models.CharField(max_length=200)
    Q10 = models.CharField(max_length=200)
class Per(models.Model):
    user_namep = models.CharField(max_length=200)
    Q1p = models.CharField(max_length=200)
    Q2p = models.CharField(max_length=200)
    Q3p = models.CharField(max_length=200)
    Q4p = models.CharField(max_length=200)
    Q5p = models.CharField(max_length=200)
    Q6p = models.CharField(max_length=200)
    Q7p = models.CharField(max_length=200)
    Q8p = models.CharField(max_length=200)
    Q9p = models.CharField(max_length=200)