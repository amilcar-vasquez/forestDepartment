from django.db import models
from styleguide_example.users.models import BaseUser
from styleguide_example.files.models import File
from datetime import datetime, date

# Create your models here.
class Application(models.Model):
    TYPE_CHOICES = (
        ('Import', 'Import'),
        ('Export', 'Export'),
        ('Re-export', 'Re-export'),
    )
    GOODS_CHOICES = (
        ('Lumber', 'Lumber/Lumber Products'),
        ('Wildlife', 'Wildlife/Animals'),
        ('Plants', 'Plants/Plant Products'),
        ('Other', 'Other'),
    )
    TRANSPORT_CHOICES = (
        ('Air', 'Air'),
        ('Sea', 'Sea'),
        ('Land', 'Land'),
    )
    TREATMENT_CHOICES = (
        ('Pressure', 'Pressure'),
        ('Kiln', 'Kiln'),
        ('Chemical', 'Chemical'),
        ('Air Dry', 'Air Dry'),
        ('None', 'None'),
        ('Other', 'Other'),
    )
    APPROVAL_CHOICES = (
        ('Approved', 'Approved'),
        ('Conditional', 'Approved with Conditions'),
        ('Not Approved', 'Not Approved'),
        ('In Review', 'In Review'),
    )
    PORT_CHOICES = (
        ('Western Border', 'Western Border'),
        ('Port of Belize', 'Port of Belize, Belize City'),
        ('Northern Border', 'Northern Border'),
        ('PGIA', 'Philip Goldson International Airport'),
        ('Big Creek', 'Big Creek Port, Stann Creek'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    goods = models.CharField(max_length=100, choices=GOODS_CHOICES)
    importer_name = models.CharField(max_length=100)
    importer_company_name = models.CharField(max_length=100, blank=True, null=True)
    company_registry_number = models.CharField(max_length=100, blank=True, null=True)
    importer_address = models.CharField(max_length=100)
    importer_city = models.CharField(max_length=100)
    importer_state = models.CharField(max_length=100)
    importer_zip = models.CharField(max_length=100)
    importer_country    = models.CharField(max_length=100)
    importer_phone = models.CharField(max_length=100)
    importer_email = models.CharField(max_length=100)
    importer_social = models.CharField(max_length=100) 
    importer_id_number = models.CharField(max_length=100, blank=True, null=True) 
    importer_business_number = models.CharField(max_length=100)
    exporter_name = models.CharField(max_length=100)
    exporter_address = models.CharField(max_length=100)
    exporter_city = models.CharField(max_length=100)
    exporter_state = models.CharField(max_length=100)
    exporter_zip = models.CharField(max_length=100)
    exporter_country    = models.CharField(max_length=100)
    mode_of_transport = models.CharField(max_length=100, choices=TRANSPORT_CHOICES) 
    port_of_entry = models.CharField(max_length=100, choices=PORT_CHOICES, blank=True, null=True)
    port_of_exit = models.CharField(max_length=100, choices=PORT_CHOICES, blank=True, null=True)
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES)
    other_treatment = models.CharField(max_length=100, blank=True, null=True)
    lumber_details = models.ManyToManyField('Lumber', blank=True)
    species_details = models.ManyToManyField('Species', blank=True)
    files = models.ManyToManyField(File, blank=True)
    date_received = models.DateField(default=date.today)
    date_approved = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)
    packaging_list_approved = models.BooleanField(default=False)
    approval = models.CharField(max_length=100, choices=APPROVAL_CHOICES, blank=True, null=True, default='In Review')
    permit_number = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.importer_name
    
class Lumber(models.Model):
    local_name = models.CharField(max_length=100, blank=True, null=True)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)    
    grade = models.CharField(max_length=100, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.scientific_name
    
class Species(models.Model):
    CITES_CHOICES = (
        ('Appendix I', 'Appendix I'),
        ('Appendix II', 'Appendix II'),
        ('Appendix III', 'Appendix III'),
        ('Not Listed', 'Not Listed'),
    )
    CLASS_CHOICES = (
        ('Research', 'Research'),
        ('Pet', 'Pet'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    CITES_status = models.CharField(max_length=100, choices=CITES_CHOICES)
    number_of_individuals = models.IntegerField(default=1)
    class_of_goods = models.CharField(max_length=100, choices=CLASS_CHOICES)
    identification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SpeciesType(models.Model):
    TYPE_CHOICES = (
        ('Live Specimen', 'Live Specimen'),
        ('Plant Sample', 'Plant Sample'),
        ('Blood Sample', 'Blood Sample'),
        ('Tissue Sample', 'Tissue Sample'),
        ('Feather Sample', 'Feather Sample'),
        ('Swab Sample', 'Swab Sample (Buccal/Skin)'),
        ('Other', 'Other'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=True, null=True)
    number_of_individuals = models.IntegerField(default=1)
    mode_of_storage = models.CharField(max_length=100, blank=True, null=True)
    tests_to_be_conducted = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type

class Profile(models.Model):
    PROFILE_TYPE_CHOICES = (
        ('Individual', 'Individual'),
        ('Business', 'Business'),
    )
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, blank=True, null=True)
    profile_type = models.CharField(max_length=100, choices=PROFILE_TYPE_CHOICES)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    business_document = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name