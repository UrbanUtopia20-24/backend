import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_utopia_2024.settings')

application = get_wsgi_application()
