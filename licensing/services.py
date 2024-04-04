from .models import Application
from django.contrib import messages
from styleguide_example.users.services import user_create
import random
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from datetime import datetime, date

def add_application(form, request, lumber, files):
	try:		
		member = form.save()
		member.user = request.user
		member.save()
		for form2 in lumber:
			if form2.is_valid():
				lumber = form2.save(commit=False)				
				lumber.save()
				member.lumber_details.add(lumber)
		for form3 in files:
			if form3.is_valid():
				file = form3.save(commit=False)
				file.uploaded_by = request.user
				file.save()
				member.files.add(file)
	except ValidationError:
		messages.add_message(request,messages.ERROR, 'User with this Email address already exists')
		return False

def forgot_code(email, request):
	code = random.randint(1000,9999)

	send_mail('New Check-In Code', 'Your new check-in code is: ' + str(code), 'jashua@savageroasters.com',[email])

def add_profile(form, request):
	try:
		user = user_create(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
		if user:
			profile = form.save()
			profile.user = user
			profile.save()
	except ValidationError:
		messages.add_message(request,messages.ERROR, 'User with this Email address already exists')
		return False

