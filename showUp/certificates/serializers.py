from rest_framework import serializers
from .models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
      image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
      class Meta:
        model = Certificate
        fields = ('__all__')