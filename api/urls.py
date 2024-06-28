from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PDFContentViewSet

router = DefaultRouter()
router.register(r'pdf', PDFContentViewSet,  basename='pdf')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
