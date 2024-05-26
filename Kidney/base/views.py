from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pickle
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
global scaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import load_model





def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')



def getPredictions(a,b,c,d,e,f,g,h,i,j,k,l):
    loaded_model = load_model("final_model.h5")
    input_data = np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
    predictions = loaded_model.predict(input_data)
    prediction = np.round(predictions).astype(int)
    return prediction


def result(request):
    if request.method == 'POST':
        # Retrieve form data
        a = int(request.POST.get('age'))
        b = int(request.POST.get('bp'))
        c = float(request.POST.get('sg'))
        d = int(request.POST.get('al'))
        e = int(request.POST.get('su'))
        f = int(request.POST.get('rbc'))
        g = int(request.POST.get('pc'))
        h = int(request.POST.get('pcc'))
        i = int(request.POST.get('ba'))
        j = int(request.POST.get('appet'))
        k = int(request.POST.get('pe'))
        l = int(request.POST.get('ane'))  
    result= getPredictions(a,b,c,d,e,f,g,h,i,j,k,l)
    print(result)
    if result==0:
        res='Chronic Kidney Disease'
    else:
        res='Healthy'
    
    return render(request, 'result.html', {'result': res})