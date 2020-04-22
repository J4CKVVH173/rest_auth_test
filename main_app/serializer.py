from rest_framework.serializers import ModelSerializer
from .models import MainModel


class MainModelSerializer(ModelSerializer):

    class Meta:
        model = MainModel
        fields = '__all__'
