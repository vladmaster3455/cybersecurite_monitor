from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlertViewSet, IncidentViewSet, SecurityLogViewSet

router = DefaultRouter()
router.register("logs", SecurityLogViewSet, basename="security-log")
router.register("alerts", AlertViewSet, basename="alert")
router.register("incidents", IncidentViewSet, basename="incident")
urlpatterns = [path("", include(router.urls))]
