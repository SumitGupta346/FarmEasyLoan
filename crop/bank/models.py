from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=40)
    password= models.CharField(max_length=20)
    type= models.CharField(max_length=20)

class bank(models.Model):
    bankid=models.CharField(max_length=20)
    bank_name = models.CharField(max_length=40)
    branch_name= models.CharField(max_length=40)
    city= models.CharField(max_length=40)

class aadhar_details(models.Model):
    aadhar_no=models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    gender= models.CharField(max_length=40)
    dob= models.CharField(max_length=40)
    address= models.CharField(max_length=40)
    utar_no = models.CharField(max_length=40)

class crop_loan_status(models.Model):
    loanid=models.CharField(max_length=20)
    verify_status= models.CharField(max_length=30)
    request_status= models.CharField(max_length=30)
    appln_status= models.CharField(max_length=30)
    reason= models.CharField(max_length=40)


class crop_loan(models.Model):
    cid=models.CharField(max_length=20)
    loan_id= models.CharField(max_length=20)
    rateof_intrest= models.CharField(max_length=20)
    min_acre= models.CharField(max_length=20)
    Acre_of_land= models.CharField(max_length=20)
    Loan_amount = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=15)
    utara= models.CharField(max_length=20)
    photo = models.FileField(upload_to='documents/')
    appln_contact= models.CharField(max_length=20)


class govt_schemes(models.Model):
    gsid=models.CharField(max_length=20)
    schme_type= models.CharField(max_length=40)
    doc_reqrd= models.CharField(max_length=80)
    loan_rate= models.CharField(max_length=20)
    eligible= models.CharField(max_length=40)
    description = models.CharField(max_length=100)

class farmer_reg(models.Model):
    farmer_name=models.CharField(max_length=40)
    lname= models.CharField(max_length=40)
    age= models.CharField(max_length=10)
    gender= models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    aadhar_no = models.CharField(max_length=15)
    utar_no= models.CharField(max_length=20)


class meeting_details(models.Model):
    loan_id=models.CharField(max_length=40)
    bank_id= models.CharField(max_length=40)
    gsid= models.CharField(max_length=10)
    date= models.CharField(max_length=20)
    time= models.CharField(max_length=20)


class upload_document(models.Model):
    loan_id=models.CharField(max_length=40)
    bank_id= models.CharField(max_length=40)
    gsid= models.CharField(max_length=10)
    aadhar_no=models.CharField(max_length=15)
    document_name= models.CharField(max_length=20)
    location= models.FileField(upload_to='documents/')
