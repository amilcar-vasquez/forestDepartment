from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Application
from .forms import ApplicationForm, ForgotForm
from .services import add_application, forgot_code
from styleguide_example.users.models import BaseUser

# Create your views here.
def index(request):
    return render(request, 'licensing/index.html')

def application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            new_application = add_application(form, request)
            if new_application != False:
                messages.add_message(request, messages.SUCCESS, 'Signup Successful')
                return HttpResponseRedirect('/licensing/login')
            return render(request, 'licensing/application.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()
    return render(request, 'licensing/application.html', {'form': form})

def login(request):
    code = request.GET['code']
    email = request.GET['email']
    remember_me = request.GET.get('remember_me', False)
    try:
        user = BaseUser.objects.get(email=email)
        auth_login(request,user)
        request.session['user_id'] = user.id
        if remember_me == False:
            request.session.set_expiry(0)  # if remember me is 
            request.session.modified = True
        return redirect('/licensing')        
    except BaseUser.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Wrong Check-In code or email. Member Does Not exist')
        return redirect('/licensing/login')    

def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successful')
    return redirect('/licensing/login')

def qr(request, id):
    context = {}
    if id is not None:
        try:
            run = Application.objects.get(id=id)
            context = {'application': run}
        except Application.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Application with this ID Does not exist.')
    template = loader.get_template('licensing/qr.html')    
    return HttpResponse(template.render(context, request))

def signup(request):
    # if this is a POST request we need to process the form data
    return render(request, 'members/signup.html')

def profile(request):
    return render(request, 'members/profile.html')

def coupons(request):
    if request.user.is_authenticated:
        template = loader.get_template('members/coupons.html')
        context = {'coupons': coupons}
        return HttpResponse(template.render(context, request))
    else:
        messages.add_message(request, messages.INFO, 'Please login first')
        return HttpResponseRedirect('/members/login/1')

def forgot(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ForgotForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            forgot_code(form.cleaned_data['email'], request)
            messages.add_message(request, messages.SUCCESS, 'New Code sent')
            return HttpResponseRedirect('/members/forgot')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ForgotForm()

    return render(request, 'members/forgot.html', {'form': form})