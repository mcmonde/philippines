import os
import django
import csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philippines.settings')
django.setup()
from regions.models import Region
from provinces.models import Province
from municipalities.models import Municipality
from cities.models import City
from barangays.models import Barangay
from districts.models import District
from submunicipalities.models import SubMunicipality
from sgu.models import Sgu


def populate_database_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        counter = 0
        for row in reader:
            counter += 1
            psgc = row['10-digit PSGC']
            geo_level = row['Geographic Level']

            if geo_level == 'Dist':
                district, created = District.objects.get_or_create(
                    name=row['Name'],
                    old_names=row['Old names']
                )
                if created:
                    print(f'DISTRICT created: {district}')
                else:
                    print(f'DISTRICT retrieved.')
            elif geo_level == 'Reg':
                region, created = Region.objects.get_or_create(
                    code=psgc,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'REGION created: {region}')
                else:
                    print(f'REGION retrieved.')
            elif geo_level == 'Prov':
                province, created = Province.objects.get_or_create(
                    code=psgc,
                    region_id=region.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'PROVINCE created: {province}')
                else:
                    print(f'PROVINCE  retrieved.')
            elif geo_level == '':
                province, created = Province.objects.get_or_create(
                    code=psgc,
                    region_id=region.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'PROVINCE created: {province}')
                else:
                    print(f'PROVINCE  retrieved.')
            elif geo_level == 'Mun':
                municipality, created = Municipality.objects.get_or_create(
                    code=psgc,
                    province_id=province.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'MUNICIPALITY created: {municipality}')
                else:
                    print(f'MUNICIPALITY retrieved')
            elif geo_level == 'City':
                municipality, created = City.objects.get_or_create(
                    code=psgc,
                    province_id=province.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'CITY created: {municipality}')
                else:
                    print(f'CITY retrieved')
            elif geo_level == 'SubMun':
                municipality, created = SubMunicipality.objects.get_or_create(
                    code=psgc,
                    province_id=province.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'SUB-MUNICIPALITY created: {municipality}')
                else:
                    print(f'SUB-MUNICIPALITY retrieved')
            elif geo_level == 'SGU':
                municipality, created = Sgu.objects.get_or_create(
                    code=psgc,
                    province_id=province.id,
                    defaults={'name': row['Name'], 'old_names': row['Old names']}
                )
                if created:
                    print(f'SGU created: {municipality}')
                else:
                    print(f'SGU retrieved')
            elif geo_level == 'Bgy':
                barangay, created = Barangay.objects.get_or_create(
                    code=psgc,
                    municipality_id=municipality.id,
                    name=row['Name'],
                    old_names=row['Old names']
                )
                if created:
                    print(f'BARANGAY created: {barangay}')
                else:
                    print(f'BARANGAY retrieved.')

            print(f'{counter}')


if __name__ == '__main__':
    populate_database_from_csv('seeders/data.csv')
