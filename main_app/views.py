from rest_framework.viewsets import ModelViewSet
from .models import MainModel
from .serializer import MainModelSerializer

# Create your views here.


class MainView(ModelViewSet):
    queryset = MainModel.objects.all()
    serializer_class = MainModelSerializer
