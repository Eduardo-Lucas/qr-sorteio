import os, sys

from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, "/home/CONTA/qr_sorteio")
os.environ['DJANGO_SETTINGS_MODULE'] = "qr_sorteio.settings"

WSGIServer(get_wsgi_application()).run()
