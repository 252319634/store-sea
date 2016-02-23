import sae
from store import wsgi

application = sae.create_wsgi_app(wsgi.application)