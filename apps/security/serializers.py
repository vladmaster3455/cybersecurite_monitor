from rest_framework import serializers

from .models import Alert, Incident, SecurityLog
from .services import SecurityLogService


class SecurityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityLog
        fields = ("id", "source_ip", "event_type", "severity", "user_agent", "endpoint", "metadata", "created_at")

    def create(self, validated_data):
        return SecurityLogService.record(**validated_data)


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ("id", "title", "severity", "status", "source_ip", "assigned_to", "details", "created_at")


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ("id", "title", "description", "alert", "handled_by", "resolved_at", "created_at")
