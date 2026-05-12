from django.conf import settings
from django.db import models

from apps.common.models import TimeStampedModel


class SecurityLog(TimeStampedModel):
    class Severity(models.TextChoices):
        INFO = "info", "Info"
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"
        CRITICAL = "critical", "Critical"

    source_ip = models.GenericIPAddressField()
    event_type = models.CharField(max_length=80)
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.INFO)
    user_agent = models.TextField(blank=True)
    endpoint = models.CharField(max_length=240, blank=True)
    metadata = models.JSONField(default=dict)

    class Meta:
        indexes = [models.Index(fields=["source_ip", "event_type", "created_at"])]
        ordering = ("-created_at",)


class Alert(TimeStampedModel):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        ACKNOWLEDGED = "acknowledged", "Acknowledged"
        RESOLVED = "resolved", "Resolved"

    title = models.CharField(max_length=180)
    severity = models.CharField(max_length=20, choices=SecurityLog.Severity.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    details = models.JSONField(default=dict)


class Incident(TimeStampedModel):
    title = models.CharField(max_length=180)
    description = models.TextField()
    alert = models.ForeignKey(Alert, on_delete=models.SET_NULL, null=True, blank=True, related_name="incidents")
    handled_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    resolved_at = models.DateTimeField(null=True, blank=True)
