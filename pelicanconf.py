#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sean Azlin'
SITENAME = u'Sean Azlin'
SITEURL = ''
THEME = './pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'
PATH = 'content'
TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

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
