from django.urls import path
from .views import IndexView, SaltView


app_name = "web"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('salt', SaltView.as_view(), name='salt'),
]