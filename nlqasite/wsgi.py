"""
WSGI config for nlqasite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/jcoreyes/NLQA-site/nlqasite')
sys.path.append('/home/jcoreyes/NLQA-site')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nlqasite.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'nlqasite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
