#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-publica-positions
------------

Tests for `django-publica-positions` models module.
"""

import os
import shutil
import unittest

from positions import models
from positions import factories


class TestPositions(unittest.TestCase):

    def setUp(self):
        self.position = factories.PositionFactory(
        	title='Position Foo')

    def test_title_is_foo(self):
        self.assertEqual(self.position.title, 'Position Foo')

    def test_slug_is_foo(self):
        self.assertEqual(self.position.slug, 'position-foo')

    def tearDown(self):
        pass