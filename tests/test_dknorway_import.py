# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""

import dknorway.admin
import dknorway.models
import dknorway.posten_postnrimport
import dknorway.postnrcache


def test_import_():
    "Test that all modules are importable."
    
    assert dknorway.admin
    assert dknorway.models
    assert dknorway.posten_postnrimport
    assert dknorway.postnrcache
