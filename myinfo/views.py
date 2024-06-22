
from django.shortcuts import render, redirect, get_object_or_404
from .models import Signup, Personaldetails, Educationaldetails, Financialdetails, Professionaldetails, Medicaldetails
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages


def index(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]

        # Check if the username already exists
        if User.objects.filter(username=a).exists():
            messages.error(request, "Username already exists.")
            return render(request, "sign-up.html")

        try:
            # Create the user
            user = User.objects.create_user(username=a, password=b)
            user.save()

            # Create the Signup entry
            e = Signup(username=a, password=b, user=user)
            e.save()

            # Log the user in and redirect to success page
            login(request, user)
            return redirect("signup_success")
        except IntegrityError:
            messages.error(request, "An error occurred. Please try again.")
            return render(request, "sign-up.html")

    return render(request, "sign-up.html")


def signup_success(request):
    return render(request, 'signup-success.html')


def form_success(request):
    return render(request, 'form-success.html')


def delete_success(request):
    return render(request, 'delete-success.html')


def edit_success(request):
    return render(request, 'edit-success.html')


@login_required
def form(request):
    return render(request, 'form.html')


def signin(request):
    if request.method == 'POST':
        a = request.POST['name1']
        b = request.POST['name2']
        user = authenticate(username=a, password=b)
        if user is not None:
            login(request, user)
            return redirect('form')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, "sign-in.html")


def lout(request):
    logout(request)
    return redirect('signin')


@login_required
def personal(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        Personaldetails.objects.create(
            user=request.user, fullname=a, email=b, mobile=c, dob=d, gender=e, address=f, pincode=g)
        return redirect("form_success")
    return render(request, "signup_personal.html")


@login_required
def educational(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        Educationaldetails.objects.create(
            user=request.user, degree=a, specialization=b, cgpa=c, college=d, passoutyear=e)
        return redirect("form_success")
    return render(request, "signup_educational.html")


@login_required
def financial(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        Financialdetails.objects.create(
            user=request.user, income_item1=a, income_amount1=b, expense_item1=c, expense_amount1=d)
        return redirect("form_success")
    return render(request, "signup_financial.html")


@login_required
def professional(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        Professionaldetails.objects.create(
            user=request.user, aadhaar=a, account=b, pancard=c, electionid=d, drivinglicense=e, passport=f)
        return redirect("form_success")
    return render(request, "signup_professional.html")


@login_required
def medical(request):
    if request.method == 'POST':
        a = request.POST.get('name1')
        b = request.POST.get('name2')
        c = request.POST.get('name3')
        d = request.POST.get('name4')
        e = request.POST.get('name5')
        f = request.POST.get('name6')
        g = request.POST.get('name7')
        Medicaldetails.objects.create(
            user=request.user, bloodpressure=a, cholestrol=b, diabetics=c,
            thyroid=d, asthma=e, allergy=f, heartdisease=g)
        return redirect('form_success')
    return render(request, 'signup_medical.html')


@login_required
def data(request):

    personal_data = Personaldetails.objects.filter(user=request.user)
    educational_data = Educationaldetails.objects.filter(user=request.user)
    financial_data = Financialdetails.objects.filter(user=request.user)
    professional_data = Professionaldetails.objects.filter(user=request.user)
    medical_data = Medicaldetails.objects.filter(user=request.user)

    context = {
        'personal_data': personal_data,
        'educational_data': educational_data,
        'financial_data': financial_data,
        'professional_data': professional_data,
        'medical_data': medical_data
    }
    return render(request, 'data.html', context)


@login_required
def edit_personal(request, id):
    z = get_object_or_404(Personaldetails, id=id, user=request.user)
    if request.method == "POST":
        z.fullname = request.POST["name1"]
        z.email = request.POST["name2"]
        z.mobile = request.POST["name3"]
        z.dob = request.POST["name4"]
        z.gender = request.POST["name5"]
        z.address = request.POST["name6"]
        z.pincode = request.POST["name7"]
        z.save()
        return redirect("edit_success")
    return render(request, "edit_personal.html", {"personal_detail": z})


@login_required
def delete_personal(request, id):
    personal_detail = get_object_or_404(Personaldetails, id=id, user=request.user)
    personal_detail.delete()
    return redirect("delete_success")


@login_required
def edit_educational(request, id):
    z = get_object_or_404(Educationaldetails, id=id, user=request.user)
    if request.method == 'POST':
        z.degree = request.POST['name1']
        z.specialization = request.POST['name2']
        z.cgpa = request.POST['name3']
        z.college = request.POST['name4']
        z.passoutyear = request.POST['name5']
        z.save()
        return redirect('edit_success')
    return render(request, 'edit_educational.html', {'educational_detail': z})


@login_required
def delete_educational(request, id):
    educational_detail = get_object_or_404(Educationaldetails, id=id, user=request.user)
    educational_detail.delete()
    return redirect("delete_success")


@login_required
def edit_financial(request, id):
    z = get_object_or_404(Financialdetails, id=id, user=request.user)
    if request.method == "POST":
        z.income_item1 = request.POST["name1"]
        z.income_amount1 = request.POST["name2"]
        z.expense_item1 = request.POST["name3"]
        z.expense_amount1 = request.POST["name4"]
        z.save()
        return redirect("edit_success")
    return render(request, "edit_financial.html", {"financial_detail": z})


@login_required
def delete_financial(request, id):
    financial_detail = get_object_or_404(Financialdetails, id=id, user=request.user)
    financial_detail.delete()
    return redirect("delete_success")


@login_required
def edit_professional(request, id):
    z = get_object_or_404(Professionaldetails, id=id, user=request.user)
    if request.method == 'POST':
        z.aadhaar = request.POST['name1']
        z.account = request.POST['name2']
        z.pancard = request.POST['name3']
        z.electionid = request.POST['name4']
        z.drivinglicense = request.POST['name5']
        z.passport = request.POST['name6']
        z.save()
        return redirect('edit_success')
    return render(request, 'edit_professional.html', {'professional_detail': z})


@login_required
def delete_professional(request, id):
    professional_detail = get_object_or_404(Professionaldetails, id=id, user=request.user)
    professional_detail.delete()
    return redirect("delete_success")


@login_required
def edit_medical(request, id):
    z = get_object_or_404(Medicaldetails, id=id, user=request.user)
    if request.method == "POST":
        z.bloodpressure = request.POST.get('bloodpressure', z.bloodpressure)
        z.cholestrol = request.POST.get('cholestrol', z.cholestrol)
        z.diabetics = request.POST.get('diabetics', z.diabetics)
        z.thyroid = request.POST.get('thyroid', z.thyroid)
        z.asthma = request.POST.get('asthma', z.asthma)
        z.allergy = request.POST.get('allergy', z.allergy)
        z.heartdisease = request.POST.get('heartdisease', z.heartdisease)
        z.save()
        return redirect('edit_success')
    return render(request, 'edit_medical.html', {'medical_detail': z})


@login_required
def delete_medical(request, id):
    medical_detail = get_object_or_404(Medicaldetails, id=id, user=request.user)
    medical_detail.delete()
    return redirect("delete_success")

# Create your views here.
