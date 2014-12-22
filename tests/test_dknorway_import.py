# -*- coding: utf-8 -*-
from unittest import TestCase
import dknorway.models
import dknorway.admin
import dknorway.posten_postnrimport
import dknorway.postnrcache

class TestImport(TestCase):

    def test_dkmath_import(self):
        assert dknorway.models
        assert dknorway.admin
        assert dknorway.posten_postnrimport
        assert dknorway.postnrcache
