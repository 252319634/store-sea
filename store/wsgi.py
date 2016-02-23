# -*- coding:utf8 -*-
"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
root = os.path.dirname(__file__)
# 输出当前文件所在文件夹的绝对路径
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))
# 将root路径中的上级目录的site-packages加入到Path中去
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")

application = get_wsgi_application()