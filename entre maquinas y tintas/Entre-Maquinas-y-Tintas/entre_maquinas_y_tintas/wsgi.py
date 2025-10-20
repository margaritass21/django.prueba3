import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entre_maquinas_y_tintas.settings')

application = get_wsgi_application()