from django.db import models, connection
from styleguide_example.users.models import BaseUser
from styleguide_example.files.models import File
from datetime import datetime, date

from phonenumber_field.modelfields import PhoneNumberField 

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
    importer_phone = PhoneNumberField(region='US')
    importer_email = models.CharField(max_length=100)
    importer_social = models.CharField(max_length=100) 
    importer_id_number = models.CharField(max_length=100, blank=True, null=True) 
    importer_business_number = PhoneNumberField(region='US', blank=True, null=True)
    exporter_name = models.CharField(max_length=100)
    exporter_address = models.CharField(max_length=100)
    exporter_city = models.CharField(max_length=100)
    exporter_state = models.CharField(max_length=100)
    exporter_zip = models.CharField(max_length=100)
    exporter_country    = models.CharField(max_length=100)
    mode_of_transport = models.CharField(max_length=100, choices=TRANSPORT_CHOICES) 
    port_of_entry_bz = models.CharField(max_length=100, choices=PORT_CHOICES, blank=True, null=True)
    port_of_exit_bz = models.CharField(max_length=100, choices=PORT_CHOICES, blank=True, null=True)
    port_of_entry_int = models.CharField(max_length=100, blank=True, null=True)
    port_of_exit_int = models.CharField(max_length=100, blank=True, null=True)
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES)
    other_treatment = models.CharField(max_length=100, blank=True, null=True)
    lumber_details = models.ManyToManyField('Lumber', blank=True)
    source_of_lumber = models.ManyToManyField('SourceOfLumber', blank=True)
    species_details = models.ManyToManyField('Species', blank=True)    
    endorsement_letter = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    cites_permit = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    vet_certificate = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    id_document = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True) 
    packing_list = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    performa_invoice = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    picture_of_material = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    zero_balance_receipt = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
    sawmill_proof = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True)
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
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cubic_meters = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)    
    grade = models.CharField(max_length=100, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.scientific_name
    
class SourceOfLumber(models.Model):
    LUMBER_SOURCE_CHOICES = (
        ('License', 'Forest License'),
        ('Sawmill', 'Sawmill/Lumber Yard'),
    )
    source_of_lumber = models.CharField(max_length=100, choices=LUMBER_SOURCE_CHOICES, blank=True, null=True)    
    licensee_name = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)  
    validity_period = models.CharField(max_length=100, blank=True, null=True)
    sawmill_name = models.CharField(max_length=100, blank=True, null=True)
    sawmill_address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.source_of_lumber + ' ' + self.licensee_name
    
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
    local_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    CITES_status = models.CharField(max_length=100, choices=CITES_CHOICES)
    number_of_individuals = models.IntegerField(default=1)
    class_of_goods = models.CharField(max_length=100, choices=CLASS_CHOICES)
    identification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CITESList(models.Model):
    CITES_CHOICES = (
        ('I', 'Appendix I'),
        ('II', 'Appendix II'),
        ('III', 'Appendix III'),
    )
    CITES_id = models.CharField(max_length=100)
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    order = models.CharField(max_length=100, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100)
    sub_species = models.CharField(max_length=100, blank=True, null=True)
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=500, blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True, null=True)
    listing = models.CharField(max_length=100, choices=CITES_CHOICES)

    def __str__(self):
        return self.species
    
    def serialize(self):
        return {
            "common_name": self.common_name,
            "scientific_name": self.scientific_name
        }
    
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))

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