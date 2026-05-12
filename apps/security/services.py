from datetime import timedelta

from django.utils import timezone

from .models import Alert, SecurityLog


class AnomalyDetectionService:
    FAILED_LOGIN_THRESHOLD = 5

    @classmethod
    def inspect(cls, log):
        window_start = timezone.now() - timedelta(minutes=10)
        failed_count = SecurityLog.objects.filter(source_ip=log.source_ip, event_type="login_failed", created_at__gte=window_start).count()
        if failed_count >= cls.FAILED_LOGIN_THRESHOLD:
            return Alert.objects.create(
                title="Tentatives de connexion suspectes",
                severity=SecurityLog.Severity.HIGH,
                source_ip=log.source_ip,
                details={"failed_login_count": failed_count, "window_minutes": 10},
            )
        if log.severity in (SecurityLog.Severity.HIGH, SecurityLog.Severity.CRITICAL):
            return Alert.objects.create(title=f"Evenement {log.severity}", severity=log.severity, source_ip=log.source_ip, details=log.metadata)
        return None


class SecurityLogService:
    @staticmethod
    def record(**payload):
        log = SecurityLog.objects.create(**payload)
        AnomalyDetectionService.inspect(log)
        return log
