from django.urls import path

from .views import SecurityDashboardView

urlpatterns = [path("dashboard/", SecurityDashboardView.as_view(), name="security-dashboard")]
