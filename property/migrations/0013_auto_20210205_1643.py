# Generated by Django 2.2.4 on 2021-02-05 13:43

from django.db import migrations


def load_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(name=flat.owner, defaults={
            'phonenumber': flat.owners_phonenumber,
            'pure_phone': flat.owner_pure_phone,
        })
        owner[0].owned_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(load_owners)
    ]