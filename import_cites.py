import csv
from datetime import datetime
from licensing.models import CITESList

def import_list(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            CITESList.objects.create(
                CITES_id=row['Id'],
                kingdom=row['Kingdom'],
                phylum=row['phylum'],
                class_name=row['class'],
                order=row['order'],
                family=row['family'],
                genus=row['genus'],
                species=row['species'],
                sub_species=row['sub_species'],
                scientific_name=row['scientific_name'],
                rank=row['rank'],
                listing=row['listing']
            )

if __name__ == '__main__':
    csv_file_path = 'cites_list.csv'  # Replace with your actual file path
    import_list(csv_file_path)