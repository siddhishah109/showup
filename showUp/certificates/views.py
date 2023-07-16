from django.shortcuts import render
from .serializers import CertificateSerializer
from .models import Certificate
from rest_framework import viewsets

# Create your views here.

class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
