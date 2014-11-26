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
        	title='Page Header')

    def test_title_is_page_header(self):
        self.assertEqual(self.position.title, 'Page Header')

    def test_slug_is_page_header(self):
        self.assertEqual(self.position.slug, 'page-header')

    def tearDown(self):
        pass