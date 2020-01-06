# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def new_fylke_2020(apps, schema_editor):
    Fylke = apps.get_model("dknorway", "Fylke")
    f, _ = Fylke.objects.get_or_create(nr='30', navn='Viken')
    f.note = 'Buskerud, Akershus, Østfold'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='34', navn='Innlandet')
    f.note = 'Oppland, Hedemark'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='38', navn='Vestfold og Telemark')
    f.note = 'Vestfold, Telemark'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='42', navn='Agder')
    f.note = 'Aust-Agder, Vest-Agder'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='46', navn='Vestland')
    f.note = 'Hordaland, Sogn og Fjordane'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='50', navn='Trøndelag')
    f.note = 'Sør-Trøndelag, Nord-Trøndelag'
    f.save()
    f, _ = Fylke.objects.get_or_create(nr='54', navn='Troms og Finnmark')
    f.note = 'Troms, Finnmark'
    f.save()

    f = Fylke.objects.get(nr='01')
    f.active = False
    f.note = 'Viken'
    f.save()

    f = Fylke.objects.get(nr='02')
    f.active = False
    f.note = 'Viken'
    f.save()

    f = Fylke.objects.get(nr='04')
    f.active = False
    f.note = 'Innlandet'
    f.save()

    f = Fylke.objects.get(nr='05')
    f.active = False
    f.note = 'Innlandet'
    f.save()

    f = Fylke.objects.get(nr='06')
    f.active = False
    f.note = 'Viken'
    f.save()

    f = Fylke.objects.get(nr='07')
    f.active = False
    f.note = 'Vestfold og Telemark'
    f.save()

    f = Fylke.objects.get(nr='08')
    f.active = False
    f.note = 'Vestfold og Telemark'
    f.save()

    f = Fylke.objects.get(nr='09')
    f.active = False
    f.note = 'Agder'
    f.save()

    f = Fylke.objects.get(nr='10')
    f.active = False
    f.note = 'Agder'
    f.save()

    f = Fylke.objects.get(nr='12')
    f.active = False
    f.note = 'Vestland'
    f.save()

    f = Fylke.objects.get(nr='14')
    f.active = False
    f.note = 'Vestland'
    f.save()

    f = Fylke.objects.get(nr='16')
    f.active = False
    f.note = 'Trøndelag'
    f.save()

    f = Fylke.objects.get(nr='17')
    f.active = False
    f.note = 'Trøndelag'
    f.save()

    f = Fylke.objects.get(nr='19')
    f.active = False
    f.note = 'Troms og Finnmark'
    f.save()

    f = Fylke.objects.get(nr='20')
    f.active = False
    f.note = 'Troms og Finnmark'
    f.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dknorway', '0002_auto_20181202_2348'),
    ]

    operations = [
        migrations.RunPython(new_fylke_2020),
    ]
