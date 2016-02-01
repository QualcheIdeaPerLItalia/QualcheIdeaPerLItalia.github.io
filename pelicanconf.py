#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'QualcheIdeaPerLItalia'
SITENAME = u'Qualche Idea Per L\'Italia'
SITEURL = ''

PATH = 'contents'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'
DEFAULT_CATEGORY = 'Blog'

# Menu
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = None
FEED_RSS = 'feeds/rss.rss'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/Qualche-idea-per-lItalia-239497079475489/'),)

# STATIC_PATHS is relative to PATH!
STATIC_PATHS = ['images', 'pdfs', '../extra/CNAME', '../extra/favicon.png', ]
# Shift the installed location of a file
EXTRA_PATH_METADATA = {
            '../extra/CNAME': {'path': 'CNAME'},
            '../extra/favicon.png': {'path': 'favicon.png'},
            'images': {'path': 'images'},
            'pdfs': {'path': 'pdfs'},
            }

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'qualcheideaperlitalia'

THEME = "themes/octopress/"
FAVICON_FILENAME = "favicon.png"
SEARCH_BOX = True
MENUITEMS = ( ( 'Blog', '/'), )

OUTPUT_PATH = '../output/'
OUTPUT_RETENTION = [ '.git' ]
DELETE_OUTPUT_DIRECTORY = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
