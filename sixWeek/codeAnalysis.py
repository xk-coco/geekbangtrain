#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 0:41
# @File    : codeAnalysis.py

"D:\user\pys\geekbangtrain\venv\Lib\site-packages\django\core\management\__init__.py"

from collections import OrderedDict, defaultdict

from django.conf import settings

from django.core.management.base import (
    BaseCommand, CommandError, CommandParser, handle_default_options,
)

class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        if self.prog_name == '__main__.py':
            self.prog_name = 'python -m django'
        self.settings_exception = None



