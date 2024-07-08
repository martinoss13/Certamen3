from rest_framework import routers
from .views import RegistroViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register('registro',RegistroViewSet)

urlpatterns =[
    path('',include(router.urls)),
]