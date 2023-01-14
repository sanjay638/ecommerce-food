from django.shortcuts import render, redirect
from django.db.models import Q, Count, Avg
from django.contrib import messages
# Create your views here.
from Owner.form import AdminForm
from Customer.models import Feeback_Model, UserRegistration, AdminModel
from Owner.models import Adminregister_Model


def adminlogin(request):
    if request.method =="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check = Adminregister_Model.objects.get(name=name, password=password)
            request.session['userid'] = check.id

            return redirect('uploadpage')
        except:
            pass
    return render(request,'admin/adminlogin.html')


def adminregister(request):

    if request.method == "POST":

        adminid=request.POST.get('adminid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        dob= request.POST.get('dob')        
        address= request.POST.get('address')


        Adminregister_Model.objects.create(adminid=adminid, name=name, email=email, password=password, phoneno=phoneno, dob=dob,address=address)
    return render(request, 'admin/adminregister.html')




def uploadpage(request):
    if request.method =="POST":

        forms =AdminForm(request.POST,request.FILES)
        if forms.is_valid():

            forms.save()
            return redirect('uploadpage')

    else:
        forms = AdminForm()

    return render(request,"admin/uploadpage.html",{'v':forms})




def viewfeedback(request):
    obj=Feeback_Model.objects.all()
    return render(request,'admin/viewfeedback.html',{'objects':obj})



def adminlogout(request):
    return redirect('adminlogin')

def updatefood(request):
    obj = AdminModel.objects.all()
    return render(request,'admin/updatefood.html',{'objects':obj})

def customerdetails(request):
    ted = UserRegistration.objects.all()
    return render(request, 'admin/customerdetails.html',{'objects':ted})


def foodchart(request,chart_type):

    chart = Feeback_Model.objects.values('productname').annotate(dcount=Avg('ratings'))

    return render(request,"admin/foodchart.html", {'form':chart, 'chart_type':chart_type})




