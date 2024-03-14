from django.db import models
from styleguide_example.users.models import BaseUser

# Create your models here.
class Application(models.Model):
    TYPE_CHOICES = (
        ('Lumber', 'Lumber/Lumber Products'),
        ('Wildlife', 'Wildlife/Animals'),
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
    )
    APPROVAL_CHOICES = (
        ('Approved', 'Approved'),
        ('Conditional', 'Approved with Conditions'),
        ('Not Approved', 'Not Approved'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)   
    importer_name = models.CharField(max_length=100)
    importer_address = models.CharField(max_length=100)
    importer_city = models.CharField(max_length=100)
    importer_state = models.CharField(max_length=100)
    importer_zip = models.CharField(max_length=100)
    importer_country    = models.CharField(max_length=100)
    importer_phone = models.CharField(max_length=100)
    importer_email = models.CharField(max_length=100)
    importer_social = models.CharField(max_length=100)  
    importer_business_number = models.CharField(max_length=100)
    exporter_name = models.CharField(max_length=100)
    exporter_address = models.CharField(max_length=100)
    exporter_city = models.CharField(max_length=100)
    exporter_state = models.CharField(max_length=100)
    exporter_zip = models.CharField(max_length=100)
    exporter_country    = models.CharField(max_length=100)
    mode_of_transport = models.CharField(max_length=100, choices=TRANSPORT_CHOICES) 
    port_of_entry = models.CharField(max_length=100)
    port_of_exit = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES)
    description_of_goods = models.ManyToManyField('Goods', through='Species')
    date_received = models.DateField()
    date_approved = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)
    packaging_list_approved = models.BooleanField()
    approval = models.CharField(max_length=100, choices=APPROVAL_CHOICES, blank=True, null=True)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.importer_name
    
class Goods(models.Model):
    local_name = models.CharField(max_length=100)

    def __str__(self):
        return self.local_name
    
class Species(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    scientific_name = models.CharField(max_length=100)
    quantity = models.IntegerField()    
    grade = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.scientific_name
