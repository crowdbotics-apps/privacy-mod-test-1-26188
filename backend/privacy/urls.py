from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PrivacyPolicyViewSet


router = DefaultRouter()
router.register("", PrivacyPolicyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
