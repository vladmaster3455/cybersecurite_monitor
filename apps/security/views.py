from rest_framework import viewsets

from .models import Alert, Incident, SecurityLog
from .serializers import AlertSerializer, IncidentSerializer, SecurityLogSerializer


class SecurityLogViewSet(viewsets.ModelViewSet):
    queryset = SecurityLog.objects.all()
    serializer_class = SecurityLogSerializer
    filterset_fields = ("severity", "event_type", "source_ip")
    search_fields = ("source_ip", "event_type", "endpoint")
    ordering_fields = ("created_at", "severity")


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filterset_fields = ("severity", "status", "source_ip")
    ordering_fields = ("created_at",)


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.select_related("alert", "handled_by")
    serializer_class = IncidentSerializer
    filterset_fields = ("handled_by", "resolved_at")
