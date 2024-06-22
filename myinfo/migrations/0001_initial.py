# Generated by Django 5.0.3 on 2024-06-17 15:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Educationaldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default='degree', max_length=50)),
                ('specialization', models.CharField(default='specification', max_length=50)),
                ('cgpa', models.CharField(default='cgpa', max_length=50)),
                ('college', models.CharField(default='college', max_length=50)),
                ('passoutyear', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Financialdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_item1', models.CharField(default='iitem1', max_length=50)),
                ('income_amount1', models.IntegerField(default=0)),
                ('expense_item1', models.CharField(default='eitem1', max_length=50)),
                ('expense_amount1', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicaldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodpressure', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('cholestrol', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('diabetics', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('thyroid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('asthma', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('allergy', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('heartdisease', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='no', max_length=6)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personaldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='fullname', max_length=50)),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('dob', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(default='gender', max_length=50)),
                ('address', models.CharField(default='address', max_length=100)),
                ('pincode', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professionaldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.IntegerField(default=0)),
                ('account', models.IntegerField(default=0)),
                ('pancard', models.CharField(default='pan', max_length=50)),
                ('electionid', models.CharField(default='election', max_length=50)),
                ('drivinglicense', models.CharField(default='license', max_length=50)),
                ('passport', models.CharField(default='passport', max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signup', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
