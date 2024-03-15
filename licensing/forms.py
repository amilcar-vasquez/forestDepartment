from django.forms import ModelForm, TextInput
from .models import Application, Profile
from django import forms
from django.core.exceptions import ValidationError

class ApplicationForm(ModelForm):

	class Meta:
		model = Application
		fields = ['type', 'importer_name', 'importer_address', 'importer_phone', 'importer_email', 'importer_city', 'importer_zip', 'importer_state', 'importer_country', 'importer_social', 'importer_business_number',
			'exporter_name', 'exporter_address', 'exporter_city', 'exporter_zip', 'exporter_state', 'exporter_country', 'mode_of_transport', 'port_of_entry', 'port_of_exit', 'treatment', 'description_of_goods'
			]
		
	def __init__(self, *args, **kwargs):
		super(ApplicationForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	def clean(self):
		cleaned_data = super().clean()
		code = cleaned_data.get('check_in_code')
		confirm = cleaned_data.get('confirm_code')

		if confirm != code:
			raise ValidationError("Check in Code do not match")

class ForgotForm(forms.Form):
	email = forms.EmailField(label = 'Your Email')

	def clean(self):
		# Get the email
		cleaned_data = super().clean()
		email = cleaned_data.get('email')

		# Check to see if any users already exist with this email as a username.
		#try:
		#	match = Member.objects.get(email=email)
		#except Member.DoesNotExist:
		#	# A user was found with this as a username, raise an error.
		#	raise forms.ValidationError('This email address does not exist.')

class ProfileForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField(label='Your Email')

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'phone_number', 'photo']
		
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	def clean(self):
		cleaned_data = super().clean()
		code = cleaned_data.get('password')
		confirm = cleaned_data.get('confirm_password')

		if confirm != code:
			raise ValidationError("Password do not match")