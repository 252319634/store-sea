import sae
from vmaig_blog import wsgi

application = sae.create_wsgi_app(wsgi.application)