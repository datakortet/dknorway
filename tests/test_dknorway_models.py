# -*- coding: utf-8 -*-
from dknorway.models import Fylke, Kommune, PostSted
import pytest


@pytest.mark.django_db
def test_model_save():
    Fylke.objects.create(
        nr=01,
        navn="Lappland"
    )
    f = Fylke.objects.get(nr=1)
    assert f.navn == 'Lappland'

    Kommune.objects.create(
        kode=0110,
        navn="Gokk"
    )
    k = Kommune.objects.get(kode=0110)
    assert k.navn == 'Gokk'
    assert k.fylke.navn == 'Lappland'

    PostSted.objects.create(
        postnummer='9999',
        poststed='Huttiheiti',
        kommune=k,
        lat=70.1601669,
        lng=26.3844387
    )

    p = PostSted.objects.get(postnummer='9999')
    assert p == '%s %s' % (p.postnummer, p.poststed)

    assert p == PostSted.get('9999')
