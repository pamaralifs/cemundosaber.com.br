import os, sys
sys.path.append('/home/cemundos/cemundosaber.com.br/mundodosaber/')
 
from django.core.wsgi import get_wsgi_application
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mundodosaber.settings")
 
application = get_wsgi_application()