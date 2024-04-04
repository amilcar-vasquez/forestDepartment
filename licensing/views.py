from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms import formset_factory, modelformset_factory

from .models import Application
from .forms import ApplicationForm, ForgotForm, ProfileForm, LumberForm
from .services import add_application, forgot_code, add_profile
from styleguide_example.users.models import BaseUser
from styleguide_example.files.models import File

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        Applications = Application.objects.filter(user=request.user)
        completed = Applications.filter(approval='Approved').count()
        count = Applications.count()
        context = {'applications': Applications,'completed': completed, 'count': count}
        return render(request, 'licensing/index.html', context)
    return redirect('/licensing/login')
    

def application(request):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'Account is required. Please login or create new account.')
        return redirect('/licensing/login')
    LumberFormset = formset_factory(LumberForm, extra=3)
    FilesFormset = modelformset_factory(File, fields=('file',), extra=3)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = ApplicationForm(request.POST)
        lumber = LumberFormset(request.POST, request.FILES, prefix='lumber')
        files = FilesFormset(request.POST, request.FILES, prefix='files')
        if form.is_valid() and lumber.is_valid() and files.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            new_application = add_application(form, request, lumber, files)
            if new_application != False:
                messages.add_message(request, messages.SUCCESS, 'Application submitted successfully.')
                return HttpResponseRedirect('/licensing/login')
            return render(request, 'licensing/application.html', {'form': form, 'form2': lumber, 'files': files})
    # if a GET (or any other method) we'll create a blank form
    else:
        lumber_data = {
            'lumber-TOTAL_FORMS': '3',
            'lumber-INITIAL_FORMS': '0',
            'lumber-MIN_NUM_FORMS': '0',
            'lumber-MAX_NUM_FORMS': '1000',
        }
        files_data = {
            'files-TOTAL_FORMS': '3',
            'files-INITIAL_FORMS': '0',
            'files-MIN_NUM_FORMS': '0',
            'files-MAX_NUM_FORMS': '1000',
        }
        form = ApplicationForm()
        lumber = LumberFormset(lumber_data, prefix='lumber')
        files = FilesFormset(files_data, prefix='files')
    return render(request, 'licensing/application.html', {'form': form, 'form2': lumber, 'files': files})

def login(request):
    if request.user.is_authenticated:
        return redirect('/licensing')    
    template = loader.get_template('licensing/login.html')
    context = {}
    return HttpResponse(template.render(context, request)) 

def authorize(request):
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
        messages.add_message(request, messages.ERROR, 'Wrong Check-In code or email. Account Does Not exist')
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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            new_user = add_profile(form, request)
            if new_user != False:
                messages.add_message(request, messages.SUCCESS, 'Signup Successful')
                return HttpResponseRedirect('/licensing/login')
            messages.add_message(request, messages.INFO, 'Something went wrong. Please try again.')
            return render(request, 'licensing/signup.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()
    return render(request, 'licensing/signup.html', {'form': form})

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