# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

from dknorway.models import Fylke, Kommune, PostSted
import pytest


@pytest.mark.django_db
def test_model_save():
    Fylke.objects.create(
        nr='01',
        navn="Lappland"
    )
    f = Fylke.objects.get(nr='01')
    assert f.navn == 'Lappland'
    if sys.version_info.major < 3:
        assert unicode(f) == 'Lappland'

    Kommune.objects.create(
        kode='0110',
        navn="Gokk"
    )
    k = Kommune.objects.get(kode='0110')
    assert k.navn == 'Gokk'
    assert k.fylke.navn == 'Lappland'
    if sys.version_info.major < 3:
        assert unicode(k) == 'Gokk (Lappland)'

    PostSted.objects.create(
        postnummer='9999',
        poststed='Huttiheiti',
        kommune=k,
        lat=70.1601669,
        lng=26.3844387
    )

    p = PostSted.objects.get(postnummer='9999')
    print(p)

    assert p.poststed == PostSted.get('9999')
    assert '' == PostSted.get('1234')

    assert Fylke.for_postnr('9999').navn == 'Lappland'

    with pytest.raises(Fylke.DoesNotExist):
        Fylke.for_postnr('12345')
