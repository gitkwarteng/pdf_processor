from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers
from .models import PDFContent


class PDFContentSerializer(DocumentSerializer):
    class Meta:
        model = PDFContent
        depth = 2


class UploadPDFSerializer(serializers.Serializer):
    email = serializers.EmailField()
    file = serializers.FileField(allow_empty_file=False)
