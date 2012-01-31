# -*- coding:utf-8 -*-
from optparse import make_option

from django.core.management.commands.test import Command as TestCommand
from django.conf import settings


class Command(TestCommand):
    '''
    Extends ``test`` command with ``--app_prefix`` option. If set only apps
    with given prefix will be tested. App name is got from ``INSTALLED_APPS``.

    It makes easy to test only "your" apps (and not third-party) which are
    usually prefixed with project name (something like
    ``my_project.apps.my_app``).
    '''
    option_list = TestCommand.option_list + (
        make_option('--app_prefix', action='store', type='string',
                    dest='prefix', default='',
                    help='Test only apps with names which start with given prefix.'),
    )

    def handle(self, *test_labels, **options):
        test_labels = Command.prepare_labels(*test_labels, **options)
        return super(Command, self).handle(*test_labels, **options)

    @staticmethod
    def prepare_labels(*test_labels, **options):
        # The logic is placed in static method to make testing easier.
        prefix = options.pop('prefix', '')
        if prefix:
            apps = (x for x in settings.INSTALLED_APPS if x.startswith(prefix))
            labels = [x.split('.')[-1] for x in apps]
            if test_labels:
                labels = [x for x in test_labels if x in labels]
            test_labels = tuple(labels)
        return test_labels