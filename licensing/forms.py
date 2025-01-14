from django.forms import ModelForm, TextInput
from .models import Application, Profile, Lumber, SourceOfLumber, Species
from django import forms
from django.core.exceptions import ValidationError

class ApplicationForm(ModelForm):
	TREATMENT_CHOICES = (
        ('Pressure', 'Pressure'),
        ('Kiln', 'Kiln'),
        ('Chemical', 'Chemical'),
        ('Air Dry', 'Air Dry'),
        ('None', 'None'),
        ('Other', 'Other'),
    )
	goods = forms.CharField(widget=forms.HiddenInput(), initial='Lumber')
	treatment = forms.MultipleChoiceField(choices=TREATMENT_CHOICES, required=False, label='Treatment(s)')
	type = forms.CharField(widget=forms.HiddenInput())

	class Meta:
		model = Application
		fields = ['importer_name', 'importer_company_name', 'company_registry_number', 'importer_address', 'importer_phone', 'importer_email', 'importer_city', 'importer_zip', 'importer_state', 'importer_country', 'importer_social', 'importer_business_number',
			'exporter_name', 'exporter_address', 'exporter_city', 'exporter_zip', 'exporter_state', 'exporter_country', 'exporter_company_name', 'exporter_email', 'exporter_social', 'exporter_id_number', 'exporter_business_number', 'exporter_phone', 'exporter_registry_number', 'mode_of_transport', 'port_of_entry_bz', 'port_of_entry_int', 'port_of_exit_bz', 'port_of_exit_int', 'other_treatment', 'packing_list', 
			'performa_invoice', 'picture_of_material', 'zero_balance_receipt', 'sawmill_proof', 'forest_license', 'cites_permit', 'export_form', 'certificate_of_origin', 'export_permit', 'legal_acquisition', 'vet_certificate', 'class_of_goods', 'business_registry_document', 'id_document', 'species_details', 'reason_for_import_export',
			]
		
	def __init__(self, *args, **kwargs):
		super(ApplicationForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

class LumberForm(ModelForm):
	local_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'basicAutoComplete',
            'data-url': "/licensing/cites_autocomplete/"
        }), required=False, label='Local Name')
	class Meta:
		model = Lumber
		fields = ['scientific_name', 'quantity', 'cubic_meters', 'grade', 'value', 'remarks']
		
	def __init__(self, *args, **kwargs):
		super(LumberForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			if field == 'local_name':
				self.fields[field].widget.attrs['class'] = 'form-control basicAutoComplete'
			else:
				self.fields[field].widget.attrs['class'] = 'form-control ' + field

class SourceOfLumberForm(ModelForm):
	class Meta:
		model = SourceOfLumber
		fields = ['source_of_lumber', 'licensee_name', 'license_number', 'validity_period', 'sawmill_name', 'sawmill_address']
		
	def __init__(self, *args, **kwargs):
		super(SourceOfLumberForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control ' + field

class SpeciesForm(ModelForm):
	local_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'basicAutoComplete',
            'data-url': "/licensing/cites_autocomplete/"
        }), required=False, label='Local Name')
	class Meta:
		model = Species
		fields = ['scientific_name', 'country_of_origin', 'CITES_status', 'number_of_individuals', 'identification']
		
	def __init__(self, *args, **kwargs):
		super(SpeciesForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			if field == 'local_name':
				self.fields[field].widget.attrs['class'] = 'form-control basicAutoComplete'
			else:
				self.fields[field].widget.attrs['class'] = 'form-control ' + field

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
	password = forms.CharField(widget=forms.PasswordInput(), required=False)
	confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False, label='Confirm Password')
	email = forms.EmailField(widget=forms.EmailInput(), required=True, label='Email Address')

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'phone_number', 'photo', 'profile_type', 'business_name', 'business_document']
		
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	def clean(self):
		cleaned_data = super().clean()
		code = cleaned_data.get('password')
		confirm = cleaned_data.get('confirm_password')

		type = cleaned_data.get('profile_type')
		if type == 'Business':
			business = cleaned_data.get('business_name')
			if business == None:
				raise ValidationError("Please enter a business name")

		if confirm != code:
			raise ValidationError("Password do not match")