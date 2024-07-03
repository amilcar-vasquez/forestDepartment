from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.forms import formset_factory, modelformset_factory

from .models import Application, Profile, CITESList
from .forms import ApplicationForm, ForgotForm, ProfileForm, LumberForm, SourceOfLumberForm, SpeciesForm
from .services import add_application, forgot_code, add_profile
from styleguide_example.users.models import BaseUser
from styleguide_example.files.models import File

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        Applications = Application.objects.filter(user=request.user)
        completed = Applications.filter(approval='Approved').count()
        count = Applications.count()
        profile = Profile.objects.get(user=request.user)
        context = {'applications': Applications,'completed': completed, 'count': count, 'profile': profile}
        return render(request, 'licensing/index.html', context)
    return redirect('/licensing/login')
    

def lumberapplication(request, type=''):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'Account is required. Please login or create new account.')
        return redirect('/licensing/login')
    profile = Profile.objects.get(user=request.user)
    LumberFormset = formset_factory(LumberForm, extra=5)
    SourceFormset = formset_factory(SourceOfLumberForm, extra=10)
    FilesFormset = modelformset_factory(File, fields=('file',), extra=3)
    if type == 'Import':
        template = 'licensing/application.html'
    else:
        template = 'licensing/export.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = ApplicationForm(request.POST, request.FILES)
        lumber = LumberFormset(request.POST, request.FILES, prefix='lumber')
        source = SourceFormset(request.POST, prefix='source')
        files = FilesFormset(request.POST, request.FILES, prefix='files')
        if form.is_valid() and lumber.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            new_application = add_application(form, request, lumber, files)
            if new_application != False:
                messages.add_message(request, messages.SUCCESS, 'Application submitted successfully.')
                return HttpResponseRedirect('/licensing/qr/'+str(new_application.id))
            return render(request, template, {'form': form, 'form2': lumber, 'files': files, 'source': source, 'profile': profile})
    # if a GET (or any other method) we'll create a blank form
    else:
        lumber_data = {
            'lumber-TOTAL_FORMS': '10',
            'lumber-INITIAL_FORMS': '0',
            'lumber-MIN_NUM_FORMS': '0',
            'lumber-MAX_NUM_FORMS': '1000',
        }
        source_data = {
            'source-TOTAL_FORMS': '10',
            'source-INITIAL_FORMS': '0',
            'source-MIN_NUM_FORMS': '0',
            'source-MAX_NUM_FORMS': '1000',
        }
        files_data = {
            'files-TOTAL_FORMS': '3',
            'files-INITIAL_FORMS': '0',
            'files-MIN_NUM_FORMS': '0',
            'files-MAX_NUM_FORMS': '1000',
        }
        form = ApplicationForm(initial={'type': type})
        lumber = LumberFormset(lumber_data, prefix='lumber')
        source = SourceFormset(source_data, prefix='source')
        files = FilesFormset(files_data, prefix='files')
    return render(request, template, {'form': form, 'form2': lumber, 'files': files, 'source': source, 'profile': profile})

def wildlifeapplication(request,type = ''):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated == False:
        messages.add_message(request, messages.INFO, 'Account is required. Please login or create new account.')
        return redirect('/licensing/login')
    profile = Profile.objects.get(user=request.user)
    SpeciesFormset = formset_factory(SpeciesForm, extra=5)
    FilesFormset = modelformset_factory(File, fields=('file',), extra=3)
    if type == 'Import':
        template = 'licensing/wildlife.html'
    else:
        template = 'licensing/wildlife_export.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = ApplicationForm(request.POST, request.FILES)
        lumber = SpeciesFormset(request.POST, request.FILES, prefix='lumber')
        files = FilesFormset(request.POST, request.FILES, prefix='files')
        if form.is_valid() and lumber.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:            
            new_application = add_application(form, request, lumber, files)
            if new_application != False:
                messages.add_message(request, messages.SUCCESS, 'Application submitted successfully.')
                return HttpResponseRedirect('/licensing/qr/'+str(new_application.id))
            return render(request, template, {'form': form, 'form2': lumber, 'files': files, 'profile': profile})
    # if a GET (or any other method) we'll create a blank form
    else:
        lumber_data = {
            'lumber-TOTAL_FORMS': '10',
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
        form = ApplicationForm(initial={'type': type})
        lumber = SpeciesFormset(lumber_data, prefix='lumber')
        files = FilesFormset(files_data, prefix='files')
    return render(request, template, {'form': form, 'form2': lumber, 'files': files, 'profile': profile})

def view(request, id):
    context = {}
    if id is not None:
        try:
            run = Application.objects.get(id=id)
            context = {'application': run}
        except Application.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Application with this ID Does not exist.')
    template = loader.get_template('licensing/view.html')    
    return HttpResponse(template.render(context, request))

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
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            profile = form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated')
            return HttpResponseRedirect('/licensing')
        messages.add_message(request, messages.INFO, 'Something went wrong. Please try again.')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'licensing/profile.html', {'form': form, 'profile': profile})

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

def cites_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        books = CITESList.objects.filter(common_name__contains=q)
        return JsonResponse([book.serialize() for book in books], safe=False)
    else:
        HttpResponse("No cookies")