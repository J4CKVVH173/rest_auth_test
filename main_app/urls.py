from rest_framework import routers
from .views import MainView

ROUTER = routers.DefaultRouter()
ROUTER.register(r'view', MainView)

urlpatterns = ROUTER.urls
