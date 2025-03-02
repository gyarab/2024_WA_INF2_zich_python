import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_cms.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Add other protocols here if needed
})