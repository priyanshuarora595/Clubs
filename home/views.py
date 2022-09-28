from django.shortcuts import render , redirect 
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login as auth_login , logout
from .models import UserData , club

valid_username='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'

# Create your views here.

club_data = club.objects.all()
index_content = { 'club_data' : club_data }


def index(request):
    return render(request, 'index_clubs.html',index_content)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def handlesignup(request):
    
    if request.method == "POST":
        #Get parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        EmailAddress = request.POST['EmailAddress']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #check for errorneous input
        if len(username)>20:
            messages.error(request, "username length not more than 20 allowed")
            return render(request, 'signup.html')
        
        if  len(pass1)<8:
            messages.error(request, "minimum length of password = 8")
            return render(request, 'signup.html')
        
        if pass1 != pass2:
            messages.error(request, "passwords do not match")
            return render(request, 'signup.html')
            
        for c in username:
            if c not in valid_username:
                messages.error(request, "username can contain letter , numbers and underscore ( _ ) only!")
                return render(request, 'signup.html')
        user = authenticate(username=username,password=pass1)
        
        if user is None:
            #create user
            myuser=User.objects.create_user(username,email=EmailAddress,password=pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            
            
            new_user = UserData(username=username,password=pass1,first_name=firstname,last_name=lastname,email_id=EmailAddress)
            new_user.save()
            myuser.save()

            messages.success(request, "Your Account has been successfully created")
            return redirect('login')

        else:
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')
    
    else:
        return HttpResponse('404 - Not Found')
    
def handlelogin(request):
    
    if request.method == "POST":
        #Get parameters
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            auth_login(request,user)
            messages.success(request, 'Successfully logged in')
            return redirect('index_clubs')

        
        else:
            messages.error(request, 'Invalid Credentials ! Please try again .')
            return redirect('login')
    
    else:
        return HttpResponse('404 - Not Found')
    
    
def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully logged Out.')
    return redirect('index_clubs')


def view_club(request):
    name=request.POST['club-name']
    context = { 'club' : name}
    return render(request, 'clubs.html',context)

def club_signup(request):
    print(request.user)
    data = UserData.objects.filter(username=request.user).values()
    print(data)
    return redirect('index_clubs')