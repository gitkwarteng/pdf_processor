from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import PDFContent
from .serializers import PDFContentSerializer, UploadPDFSerializer
from .operations import process_pdf, save_pdf_content


class PDFContentViewSet(viewsets.ModelViewSet):
    queryset = PDFContent.objects.all()
    serializer_class = UploadPDFSerializer
    response_serializer_class = PDFContentSerializer

    def create(self, request, *args, **kwargs):
        try:
            # get serializer
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            pdf_file = serializer.validated_data.get('file')

            # process file data
            processed_data = process_pdf(file=pdf_file)

            # save pdf file
            pdf_content = save_pdf_content(
                email=email,
                file_name=pdf_file.name,
                data=processed_data
            )

            return self.get_response(instance=pdf_content)

        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_response(self, *args, **kwargs):
        """Return response with response serializer."""
        kwargs.setdefault('context', self.get_serializer_context())
        response_serializer = self.response_serializer_class(*args, **kwargs)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
