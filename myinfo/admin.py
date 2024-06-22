
from django.contrib import admin
from myinfo.models import Personaldetails, Educationaldetails,  Financialdetails, Professionaldetails, Medicaldetails

admin.site.register(Personaldetails)
admin.site.register(Financialdetails)
admin.site.register(Educationaldetails)
admin.site.register(Professionaldetails)
admin.site.register(Medicaldetails)

# Register your models here.
