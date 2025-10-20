import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entre_maquinas_y_tintas.settings')

application = get_asgi_application()