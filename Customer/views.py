from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg, Sum, F
from django.db.models import Q

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

# Create your views here.

from Customer.models import UserRegistration, Addtocard_Model, Feeback_Model
from Owner.models import AdminModel

def index(request):
    return render(request,'user/home.html')

def userlogin(request):
    if request.method =="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check = UserRegistration.objects.get(firstname=name, password=password)
            request.session['userid'] = check.id

            return  redirect('viewdetails')
        except:
            pass
    return render(request,'user/userlogin.html')

def register(request):

    if request.method == "POST":


        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobilenumber = request.POST.get('mobilenumber')
        dob= request.POST.get('dob')
        gender= request.POST.get('gender')
        address= request.POST.get('address')


        UserRegistration.objects.create(firstname=firstname, email=email, password=password, mobilenumber=mobilenumber, dob=dob,gender=gender,address=address)
    return render(request, 'user/register.html')


def viewdetails(request):
    obj = AdminModel.objects.all()
    return render(request,'user/viewdetails.html',{'objects':obj})

def viewmodeldetails(requset, pk):
    name = requset.session['userid']
    userObj = UserRegistration.objects.get(id=name)
    gymObj = AdminModel.objects.get(id=pk)
    amount = gymObj.amount


    if requset.method =="POST":
        Quality =  requset.POST.get('Quality')
        day = requset.POST.get('day')
        month = requset.POST.get('month')
        year = requset.POST.get('year')
        amount = int(Quality) * (amount)



        Addtocard_Model.objects.create(userid=userObj,salesid=gymObj, Quality=Quality, day=day, month=month, year=year, amount=amount, requeststatus="PROCESS")
    return render(requset,'user/viewmodeldetails.html',{'v':gymObj})

def addtocard(request,pk):

    obj = Addtocard_Model.objects.all()

    return render(request, 'user/addtocard.html', {'objects': obj})

def feedback(request):


    if request.method == "POST":
        name = request.POST.get('name')
        productname = request.POST.get('productname')
        feedback = request.POST.get('feedback')
        ratings = request.POST.get('ratings')
        Feeback_Model.objects.create(name=name,productname=productname,ratings=ratings, feedback=feedback)



    return render(request, 'user/feedback.html')


def mydetails(request):
    name = request.session['userid']
    ted = UserRegistration.objects.get(id=name)
    return render(request, 'user/mydetails.html',{'object':ted})


def updatedetails(request):
    name = request.session['userid']
    obj = UserRegistration.objects.get(id=name)
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        mobilenumber = request.POST.get('mobilenumber', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address','')

        obj = get_object_or_404(UserRegistration, id=name)
        obj.firstname = firstname
        obj.email = email
        obj.password = password
        obj.mobilenumber = mobilenumber
        obj.dob = dob
        obj.gender = gender
        obj.address = address
        obj.save(update_fields=["firstname", "email", "password", "mobilenumber", "dob","gender","address"])
        return redirect('mydetails')


    return render(request, 'user/updatedetails.html',{'form':obj})
def userlogout(request):
    return redirect('userlogin')


def userchart(request,chart_type):

    chart = Feeback_Model.objects.values('productname').annotate(dcount=Avg('ratings'))

    return render(request,"user/userchart.html", {'form':chart, 'chart_type':chart_type})


def reviewspage(request):
    obj = Feeback_Model.objects.all()
    return render(request, 'user/reviewspage.html', {'objects': obj})


def ordertacking(request):
    return render(request,'user/ordertacking.html')

def contactus(request):
    return render(request,'user/contactus.html')

def orderchart(request,schart_type)    :

    year = 1



    if request.method == "POST":
        year = request.POST.get('year1')


    chart = Addtocard_Model.objects.filter(year=year).values('month').annotate(dcount=Sum('Quality'))

    return render(request,"user/orderchart.html", {'form': chart, 'chart_type':schart_type})


def linear(request):
    data = pd.read_csv("Sales.csv")
    data.head()
    # Let’s select some features to explore more :
    data = data[["price", "Rating"]]
    # ENGINESIZE vs CO2EMISSIONS:
    plt.scatter(data["price"], data["Rating"], color="blue")
    plt.xlabel("price")
    plt.ylabel("Rating")
    plt.show()

    # Generating training and testing data from our data:
    # We are using 80% data for training.
    train = data[:(int((len(data) * 0.8)))]
    test = data[(int((len(data) * 0.8))):]
    # Modeling:
    # Using sklearn package to model data :
    regr = linear_model.LinearRegression()
    train_x = np.array(train[["price"]])
    train_y = np.array(train[["Rating"]])
    regr.fit(train_x, train_y)
    # The coefficients:
    print("coefficients : ", regr.coef_)  # Slope
    print("Intercept : ", regr.intercept_)  # Intercept
    # Plotting the regression line:
    plt.scatter(train["price"], train["Rating"], color='blue')
    plt.plot(train_x, regr.coef_ * train_x + regr.intercept_, '-r')
    plt.xlabel("Unit Price")
    plt.ylabel("Rating")
    plt.show()

    # Predicting values:
    # Function for predicting future values :
    def get_regression_predictions(input_features, intercept, slope):
        predicted_values = input_features * slope + intercept
        return predicted_values

    # Predicting emission for future car:
    my_engine_size = 3.5
    estimatd_emission = get_regression_predictions(my_engine_size, regr.intercept_[0], regr.coef_[0][0])
    print("Estimated Emission :", estimatd_emission)
    # Checking various accuracy:

    test_x = np.array(test[['price']])
    test_y = np.array(test[['Rating']])
    test_y_ = regr.predict(test_x)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_, test_y)))
    print("Mean sum of squares (MSE): %.2f" % np.mean(np.absolute(test_y_, test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y_, test_y))
    return render(request,'user/linear.html')
