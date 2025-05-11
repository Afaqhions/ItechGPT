# To display webpages
from django.shortcuts import render

# To Display or RenderMessages
from django.shortcuts import HttpResponse, redirect

# Database model to register user
from django.contrib.auth.models import User

# importing model--userreg from db
from userReg.models import usrReg

# Database model to login the user
from django.contrib.auth import authenticate ,logout as auth_logout, login

# Library to import email or to send email to user's email
from django.core.mail import send_mail

# Importing django-messages
from django.contrib import messages
# For middle ware
from django.contrib.auth.decorators import login_required

# Function to Display main page
@login_required(login_url='login')
def mainPage(request):
    return render(request , 'index.html')

# Function to display Resource Page
def resourcePage(request):
    return render(request , 'resource.html')

# Function to render product page
def productPage(request):
    return render(request , 'product.html')

# Function to render about us page
def aboutUsPage(request):
    return render(request , 'aboutus.html')

# Function to render Discover page
def discoverPage(request):
    return render(request , 'discover.html')

# Function to render login page
def loginPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')

        # Check if the user exists
        if User.objects.filter(username=user_name).exists():
            # Validating User
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged In.')  # Send message once
                return redirect('/')  # Redirect to home page
            else:
                messages.error(request, 'Invalid User & Password. Please try again.')  # Invalid password message
                return redirect('login')  # Redirect back to login page
        else:
            messages.error(request, 'User does not exist. Please check your username.')  # User does not exist message
            return redirect('login')  # Redirect back to login page

    return render(request, 'login.html')  # Render login page for GET requests

# Function to render sign up page
def signUpPage(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')
        usrEmail = request.POST.get('email')
        usrName = request.POST.get('username')
        passUsr = request.POST.get('password')
        confirmPass = request.POST.get('confirmpassword') 
        
        # Check if the user already exists with the same username or email
        if User.objects.filter(username=usrName).exists() and User.objects.filter(email=usrEmail).exists():
            messages.error(request, 'User Already Registered. Go to Login.')
        elif User.objects.filter(username=usrName).exists():
            messages.error(request, 'Username Already Exists.')
        elif User.objects.filter(email=usrEmail).exists():
            messages.error(request, 'Email Already Exists.')
        else:
            # Validation of password
            if passUsr != confirmPass:
                messages.error(request, 'Password should match Confirm Password.')
                return redirect('sign-up-user')
            else:
                # Create the user
                created_user = User.objects.create_user(username=usrName, email=usrEmail, password=passUsr)
                created_user.first_name = firstName
                created_user.last_name = lastName
                created_user.save()
                messages.success(request, 'Account Created Successfully!')
                return redirect('login')
    return render(request, 'signup.html')

# Function to Render Ai-Bot 
def aiPage(request):
    return render(request , 'aiApp.html')

# Function to render forget page
def forgetPage(request):
    if request.method == 'POST':
        userEmail = request.POST.get('email')  # Get email input from form
        # Check if user exists in the database
        if User.objects.filter(email=userEmail).exists():
            user = User.objects.get(email=userEmail)
            return redirect(f'/pass-reset-page/{user.username}/')  # Redirect correctly
        else:
            return HttpResponse("Email not found in our records.")  # Error response if email doesn't exist

    return render(request, 'forget.html')

# Function to render Password Reset page
def passResetPage(request, user):
    try:
        userObj = User.objects.get(username=user)  # Get user object
    except User.DoesNotExist:
        return HttpResponse("Invalid user")  # Handle invalid user case

    if request.method == 'POST':
        pass1 = request.POST.get('pass1') 
        pass2 = request.POST.get('pass2')

        if pass1 and pass2:  # Ensure both password fields are filled
            if pass1 == pass2:
                userObj.set_password(pass1)
                userObj.save()
                return HttpResponse("Password Updated Successfully...")
            else:
                return HttpResponse("Passwords must match.")
        else:
            return HttpResponse("Password fields cannot be empty.")

    return render(request, 'newPass.html', {'user': userObj})

# Logout function
def userLogout(request):
    auth_logout(request)  # Logout the user out
    messages.success(request,'Successfully Logout.')
    return redirect('main-page')  # Redirect to the main page
