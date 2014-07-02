#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sean Azlin'
SITENAME = u'Sean Azlin'
SITEURL = ''
THEME = './pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'
BOOTSTRAP_NAVBAR_INVERSE = True
PATH = 'content'
TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('rheTOracle', 'http://ec2-54-213-173-105.us-west-2.compute.amazonaws.com/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/SeanAzlin2'),
          ('LinkedIn', 'http://linkedin.com/in/seanazlin'),
          ('GitHub', 'http://github.com/sazlin'),)

DEFAULT_PAGINATION = False

READERS = {'html': None}
STATIC_PATHS = [
    'images',
    ]

GITHUB_URL = 'http://github.com/sazlin'

# Where to look for plugins
PLUGIN_PATH = './pelican-plugins'
# Which plugins to enable
PLUGINS = ['liquid_tags.img']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
