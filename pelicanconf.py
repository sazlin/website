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
LINKS =  (('Project rheTOracle', 'http://ec2-54-213-173-105.us-west-2.compute.amazonaws.com/'),
               ('Code Fellows - Seattle', 'http://codefellows.org'),
               ('RIT', 'http://rit.edu'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/SeanAzlin2'),
          ('LinkedIn', 'http://linkedin.com/in/seanazlin'),
          ('GitHub', 'http://github.com/sazlin'),)

OPEN_GRAPH_IMAGE = "../images/sean1.jpg"
AVATAR = "../images/sean1.jpg"
ABOUT_ME = """
Software Engineer with 7 years of experience building world-class software. Microsoft Alum, RIT Alum, Code Fellow, and Certified Scrum Master (CSM).
"""
GITHUB_USER = 'sazlin'
GITHUB_REPO_COUNT = 8

DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_PAGES_ON_MENU = True

TAG_CLOUD_STEPS = 1
TAG_CLOUD_MAX_ITEMS = 4

DEFAULT_PAGINATION = False

READERS = {'html': None}
STATIC_PATHS = [
    'images',
    ]

GITHUB_URL = 'http://github.com/sazlin'
TWITTER_USERNAME = 'SeanAzlin2'
TWITTER_WIDGET_ID = 485870315860287488


# Where to look for plugins
PLUGIN_PATH = './pelican-plugins'
# Which plugins to enable
PLUGINS = ['liquid_tags.img']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
