"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
profile = os.environ.get("TYPEIDEA_PROFILE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)

<<<<<<< HEAD
application = get_wsgi_application()
=======
<<<<<<< HEAD
application = get_wsgi_application()
=======
application = get_wsgi_application()
>>>>>>> 初始化提交
>>>>>>> add-blog-app-model
