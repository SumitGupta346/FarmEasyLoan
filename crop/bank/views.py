import django.shortcuts

from django.urls import reverse

from django.core.files.storage import FileSystemStorage
import os
from crop.settings import BASE_DIR

# Create your views here.

from bank.models import farmer_reg,login,crop_loan_status,govt_schemes,bank,crop_loan,meeting_details,aadhar_details,upload_document


def reginsert(request):
    if request.method == "POST":
        fname = request.POST.get('t1', '')
        lastname = request.POST.get('t2', '')
        age = request.POST.get('t3', '')
        gender = request.POST.get('r1', '')
        phone = request.POST.get('t4', '')
        email = request.POST.get('t5', '')
        aadharno = request.POST.get('t6', '')
        uttar = request.POST.get('t7', '')


        farmer_reg.objects.create(farmer_name=fname, lname=lastname, age=age,gender=gender,phone=phone,email=email,aadhar_no=aadharno,utar_no=uttar)
        login.objects.create(username=email,password=phone,type='farmer')
    return django.shortcuts.render(request, "index.html")



def insertcroploan(request,pk):
    if request.method == "POST" and request.FILES['myfile']:
        cid = request.POST.get('t1', '')
        loan_id = request.POST.get('t2', '')
        rateof_intrest= request.POST.get('t3', '')
        min_acre= request.POST.get('t4', '')
        Acre_of_land = request.POST.get('t5', '')
        Loan_amount= request.POST.get('t6', '')
        aadhar  = request.POST.get('t7', '')
        utara = request.POST.get('t8', '')
        myfile = request.FILES['myfile']
        appln_contact= request.POST.get('t10', '')

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)


        crop_loan.objects.create(cid=cid, loan_id=loan_id, rateof_intrest=rateof_intrest,min_acre=min_acre,Acre_of_land=Acre_of_land,Loan_amount=Loan_amount,aadhar=aadhar,utara=utara,photo=myfile,appln_contact=appln_contact)
    id = pk
    checklogin = govt_schemes.objects.filter(id=id).values()
    for a in checklogin:
        ncid = a['gsid']
        rateof= a['loan_rate']
    return django.shortcuts.render(request, "crop_loan.html", {"cid":ncid, "rateof":rateof})



def insetuploaddocument(request):
    if request.method == "POST" and request.FILES['myfile']:
        loan_id = request.POST.get('t1', '')
        Bank_id= request.POST.get('t2', '')
        gsid= request.POST.get('t3', '')
        aadhar_no= request.POST.get('t4', '')
        document_name= request.POST.get('t5', '')
        myfile = request.FILES['myfile']


        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)


        upload_document.objects.create(loan_id=loan_id,bank_id=Bank_id,gsid=gsid,aadhar_no=aadhar_no,document_name=document_name,location=myfile)

    return django.shortcuts.render(request, "upload_document.html")




def insertcroploanstatus(request):
    if request.method == "POST":
        loanid= request.POST.get('t1', '')
        verify_status= request.POST.get('t2', '')
        request_status= request.POST.get('t3', '')
        appln_status= request.POST.get('t4', '')
        reason= request.POST.get('t5', '')



        crop_loan_status.objects.create(loanid=loanid, verify_status=verify_status,request_status=request_status,appln_status=appln_status,reason=reason)

    return django.shortcuts.render(request, "crop_loan_status.html")


def viewcroploan(request):
    userdict = crop_loan.objects.all()
    return django.shortcuts.render(request, 'viewcroploan.html', {'userdict': userdict})

def viewcroploanbank(request):
    userdict = crop_loan.objects.all()
    return django.shortcuts.render(request, 'viewcroploanbank.html', {'userdict': userdict})

def newbankcrop(request):
    userdict = crop_loan.objects.all()
    return django.shortcuts.render(request,'bankloan.html', {'userdict': userdict})


def changepass(request):
    if request.method == 'POST':
        uname = request.session['username']
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = login.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    login.objects.filter(username=uname).update(password=newpass)
                    base_url = reverse('logcheck')
                    msg = 'password has been changed successfully'
                    return django.shortcuts.redirect(base_url, msg=msg)
                else:
                    return django.shortcuts.render(request, 'changepassword.html', {'msg': 'both the usename and password are incorrect'})
            else:
                return django.shortcuts.render(request, 'changepassword.html', {'msg': 'invalid username'})
    return django.shortcuts.render(request, 'changepassword.html')


def farmerreginsert(request):

    if request.method == "POST":
        fname = request.POST.get('t1', '')
        lastname = request.POST.get('t2', '')
        age = request.POST.get('t3', '')
        gender = request.POST.get('r1', '')
        phone = request.POST.get('t4', '')
        email = request.POST.get('t5', '')
        aadharno = request.POST.get('t6', '')
        uttar = request.POST.get('t7', '')


        farmer_reg.objects.create(farmer_name=fname, lname=lastname, age=age,gender=gender,phone=phone,email=email,aadhar_no=aadharno,utar_no=uttar)
        login.objects.create(username=email,password=phone,type='farmer')
    return django.shortcuts.render(request, "reg.html")

def insertgovtschemes(request):
    if request.method == "POST":
        gsid = request.POST.get('t1', '')
        schme_type= request.POST.get('t2', '')
        doc_reqrd= request.POST.get('t3', '')

        loan_rate = request.POST.get('t4', '')
        eligible = request.POST.get('t5', '')
        description  = request.POST.get('t6', '')
        govt_schemes.objects.create(gsid=gsid, schme_type=schme_type, doc_reqrd=doc_reqrd,loan_rate=loan_rate,eligible=eligible,description =description )

    p = govt_schemes.objects.all().order_by('id').last()
    sid = int(p.gsid) + 1
    return django.shortcuts.render(request, "govtschemes.html", {'sid':sid})






def insertaadhardetails(request):
    if request.method == "POST":
        aadhar_no= request.POST.get('t1', '')
        name= request.POST.get('t2', '')
        gender= request.POST.get('t3', '')

        dob = request.POST.get('t4', '')
        address= request.POST.get('t5', '')
        utar_no= request.POST.get('t6', '')



        aadhar_details.objects.create(aadhar_no=aadhar_no,name=name, gender=gender,dob=dob,address=address,utar_no=utar_no)

    return django.shortcuts.render(request, "aadhar_details.html")

def viewmeetingdetails(request):
    userdict = meeting_details.objects.all()
    return django.shortcuts.render(request, 'viewmeeting.html', {'userdict': userdict})

def viewmeetingdetailsfarmer(request):
    uname = request.session['username']
    aanum = farmer_reg.objects.filter(email=uname).values()
    for a in aanum:
        aadharnum=a['aadhar_no']

    getlid =crop_loan.objects.filter(aadhar=aadharnum).values()
    for b in getlid:
      lid = b['loan_id']

    userdict = meeting_details.objects.filter(loan_id=lid).values()
    return django.shortcuts.render(request, 'viewmeetingfarmer.html', {'userdict': userdict})


def insertmeetingdetails(request):
    if request.method == "POST":
        loan_id= request.POST.get('t1', '')
        bank_id= request.POST.get('t2', '')
        gsid= request.POST.get('t3', '')

        date= request.POST.get('t4', '')
        time= request.POST.get('t5', '')


        meeting_details.objects.create(loan_id=loan_id,bank_id=bank_id, gsid=gsid,date=date,time=time)

    return django.shortcuts.render(request, "meetingdetails.html")




def insertbankdetails(request):
    if request.method == "POST":
        bankid = request.POST.get('t1', '')
        bank_name= request.POST.get('t2', '')
        branch_name= request.POST.get('t3', '')

        city= request.POST.get('t4', '')



        bank.objects.create(bankid=bankid, bank_name=bank_name, branch_name=branch_name,city=city)
        login.objects.create(username=bankid, password=branch_name, type='bank')

    return django.shortcuts.render(request, "bankdetails.html")


def index(request):
    return django.shortcuts.render(request, 'index.html')

def showfarmer(request):
    userdict = farmer_reg.objects.all()
    return django.shortcuts.render(request, 'viewfarmer.html', {'userdict': userdict})

def bankfarmerview(request):
    userdict = farmer_reg.objects.all()
    return django.shortcuts.render(request, 'bankviewfarmer.html', {'userdict': userdict})


def showschemes(request):
    userdict = govt_schemes.objects.all()
    return django.shortcuts.render(request, 'viewschemes.html', {'userdict': userdict})

def homeshowschemes(request):
    userdict = govt_schemes.objects.all()
    return django.shortcuts.render(request, 'homeviewschemes.html', {'userdict': userdict})

def adminupdates(request):
    userdict=govt_schemes.objects.all()
    return  django.shortcuts.render(request, 'adminupdateschme.html', {'userdict':userdict})

def editadminschemes(request,pk):
    userdict =govt_schemes.objects.filter(id=pk).values()
    return django.shortcuts.render(request, 'schemeupdate.html', {'userdict': userdict})

def editscheme(request):
    if request.method == "POST":
        id = request.POST.get('id')
        gsid = request.POST.get('t1', '')
        schme_type= request.POST.get('t2', '')
        doc_reqrd= request.POST.get('t3', '')

        loan_rate = request.POST.get('t4', '')
        eligible = request.POST.get('t5', '')
        description  = request.POST.get('t6', '')
        govt_schemes.objects.filter(id=id).update(schme_type=schme_type, doc_reqrd=doc_reqrd,loan_rate=loan_rate,eligible=eligible,description =description )

    userdict = govt_schemes.objects.all()
    return django.shortcuts.render(request, 'adminupdateschme.html', {'userdict': userdict})


def updateshowschemes(request):
    userdict = govt_schemes.objects.all()
    return django.shortcuts.render(request, 'viewschemesupdate.html', {'userdict': userdict})

def viewcroploanstatus(request):
    userdict = crop_loan_status.objects.all()
    return django.shortcuts.render(request, 'croploanstatus.html', {'userdict': userdict})

def newstatus(request):
    uname = request.session['username']
    aanum = farmer_reg.objects.filter(email=uname).values()
    for a in aanum:
        aadharnum = a['aadhar_no']

    getlid = crop_loan.objects.filter(aadhar=aadharnum).values()
    for b in getlid:
        lid = b['loan_id']


    userdict = crop_loan_status.objects.filter(loanid=lid).values()
    return django.shortcuts.render(request, 'croploanstatusfarmern.html', {'userdict':userdict})

def showapplied(request):
    uname = request.session['username']
    aanum = farmer_reg.objects.filter(email=uname).values()
    for a in aanum:
        aadharnum = a['aadhar_no']

    userdict =crop_loan.objects.filter(aadhar=aadharnum).values()
    return django.shortcuts.render(request, 'farmerapplied.html', {'userdict': userdict})

def newstatusadmin(request):
    userdict=crop_loan_status.objects.all()
    return django.shortcuts.render(request, 'croploanstatus.html', {'userdict':userdict})

def adminloanstatus(request):
    userdict = crop_loan_status.objects.all()
    return django.shortcuts.render(request, 'adminloanstatus.html', {'userdict': userdict})

def viewcroploanstatusfarmern(request):
    userdict = crop_loan_status.objects.all()
    return django.shortcuts.render(request, 'croploanstatusfarmern.html', {'userdict': userdict})

def delcroploanstatus(request,pk):
    id=crop_loan_status.objects.get(id=pk)
    id.delete()
    userdict=crop_loan_status.objects.all()
    return django.shortcuts.render(request, 'croploanstatus.html', {'userdict':userdict})


def logcheck(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        request.session['username']=username
        #if username=="admin" and password=="admin":
        checklogin = login.objects.filter(username=username).values()
        for a in checklogin:
            utype = a['type']
            upass= a['password']
            if(upass == password):
                if (utype == "admin"):
                    return django.shortcuts.render(request, 'admin_home.html', context={'msg': 'Welcome to Admin'})
                if (utype == "bank"):
                    return django.shortcuts.render(request, 'bank_home.html', {'bankname':username})
                if (utype == "farmer"):
                    return django.shortcuts.render(request, 'farmer_home.html', {'farmername':username})
            else:
                return django.shortcuts.render(request, 'index.html', context={'msg': 'Check user name or password'})
        return django.shortcuts.render(request, 'index.html', context={'msg': 'Check user name or password'})
    return django.shortcuts.render(request, 'index.html')


def contact(request):
    return django.shortcuts.render(request, 'contact.html')




