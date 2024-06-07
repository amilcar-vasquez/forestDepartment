import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from ...models import CITESList


class Command(BaseCommand):
    help = 'Import CITES data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path of the CSV file to import')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        import_list(file_path)

def import_list(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            CITESList.objects.create(
                CITES_id=row['Id'],
                kingdom=row['Kingdom'],
                phylum=row['Phylum'],
                class_name=row['Class'],
                order=row['Order'],
                family=row['Family'],
                genus=row['Genus'],
                species=row['Species'],
                sub_species=row['Subspecies'],
                scientific_name=row['Scientific Name'],
                rank=row['Rank'],
                listing=row['Listing']
            )