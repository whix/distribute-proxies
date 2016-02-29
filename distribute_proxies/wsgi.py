"""
WSGI config for distribute_proxies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# from datetime import datetime
# print 'beginning of wsgi.py', datetime.now()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distribute_proxies.settings")

application = get_wsgi_application()

# can't import at top of file
# because import models must be at end of this file (wsgi.py)
# from ManageProxies import ManageProxies


# print 'wsgi.py', datetime.now()
# manage_proxies = ManageProxies()
# manage_proxies.start_working()
# print 'end of wsgi.py', datetime.now()











