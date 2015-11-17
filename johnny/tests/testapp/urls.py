#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""URLconf for Johnny's test app."""

try:
    from django.conf.urls.defaults import patterns, url
except:
    from django.conf.urls import patterns, url

urlpatterns = patterns('johnny.tests.testapp.views',
   (r'^test/template_queries', 'template_queries'),
)

