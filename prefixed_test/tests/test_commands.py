# -*- coding:utf-8 -*-
from django.test import TestCase
from django.conf import settings

from prefixed_test.management.commands.test import Command


class TestCommand(TestCase):
    def setUp(self):
        self._old_installed_apps = settings.INSTALLED_APPS
        settings.INSTALLED_APPS = (
            'pref.apps.my_cool_app',
            'pref.apps.my_uncool_app',
            'north',
            'unregistration',
            'some.strange.app',
            'pref.apps.my_another_app',
        )

    def tearDown(self):
        settings.INSTALLED_APPS = self._old_installed_apps

    def test_apps_are_filtered_by_prefix(self):
        labels = Command.prepare_labels(prefix='pref.apps')
        self.assertEqual(set(labels), set(['my_cool_app', 'my_uncool_app', 'my_another_app']))

    def test_apps_are_filtered_by_prefix_even_with_args(self):
        labels = Command.prepare_labels('my_cool_app', 'my_uncool_app', 'north', prefix='pref.apps')
        self.assertEqual(set(labels), set(['my_cool_app', 'my_uncool_app']))

    def test_no_filtering_without_prefix(self):
        labels = Command.prepare_labels()
        self.assertEqual(set(labels), set([]))
