from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='signup', null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Personaldetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=50, default='fullname')
    email = models.EmailField(default='default@example.com')
    mobile = models.IntegerField(default=0)
    dob = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=50, default='gender')
    address = models.CharField(max_length=100, default='address')
    pincode = models.IntegerField(default=0)


class Educationaldetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=50, default='degree')
    specialization = models.CharField(max_length=50, default='specification')
    cgpa = models.CharField(max_length=50, default='cgpa')
    college = models.CharField(max_length=50, default='college')
    passoutyear = models.IntegerField(default=0)


class Financialdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    income_item1 = models.CharField(max_length=50, default='iitem1')
    income_amount1 = models.IntegerField(default=0)
    expense_item1 = models.CharField(max_length=50, default='eitem1')
    expense_amount1 = models.IntegerField(default=0)


class Professionaldetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    aadhaar = models.IntegerField(default=0)
    account = models.IntegerField(default=0)
    pancard = models.CharField(max_length=50, default='pan')
    electionid = models.CharField(max_length=50, default='election')
    drivinglicense = models.CharField(max_length=50, default='license')
    passport = models.CharField(max_length=50, default='passport')


class Medicaldetails(models.Model):

    BP_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    CHOLESTROL_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    DIABETICS_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    THYROID_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    ALLERGY_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    ASTHMA_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    HEART_CHOICES = [('Yes', 'Yes'), ('No', 'No')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bloodpressure = models.CharField(max_length=6, choices=BP_CHOICES, default='no')
    cholestrol = models.CharField(max_length=6, choices=CHOLESTROL_CHOICES, default='no')
    diabetics = models.CharField(max_length=6, choices=DIABETICS_CHOICES, default='no')
    thyroid = models.CharField(max_length=6, choices=THYROID_CHOICES, default='no')
    asthma = models.CharField(max_length=6, choices=ASTHMA_CHOICES, default='no')
    allergy = models.CharField(max_length=6, choices=ALLERGY_CHOICES, default='no')
    heartdisease = models.CharField(max_length=6, choices=HEART_CHOICES, default='no')

# Create your models here.
