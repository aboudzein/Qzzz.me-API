#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.conf.urls import url

# Rest Framework imports.

# Third Party Library imports

# local imports.
from qzzzme_app.swagger import schema_view

app_name = 'qzzzme_app'

urlpatterns = [
    url(r'^docs/$', schema_view, name="schema_view"),
]