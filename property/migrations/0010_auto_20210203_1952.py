# Generated by Django 2.2.4 on 2021-02-03 16:52

from django.db import migrations
from phonenumbers import parse, is_valid_number


def normalise_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = parse(flat.owners_phonenumber, 'RU')
        if is_valid_number(phonenumber):
            flat.owner_pure_phone = phonenumber
        else:
            flat.owner_pure_phone = ""
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_normalized_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalise_phonenumbers),
    ]
