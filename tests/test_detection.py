import pytest

from apps.security.models import Alert
from apps.security.services import SecurityLogService


@pytest.mark.django_db
def test_failed_login_anomaly_creates_alert():
    for _ in range(5):
        SecurityLogService.record(source_ip="10.0.0.8", event_type="login_failed", severity="low")
    assert Alert.objects.filter(source_ip="10.0.0.8", status=Alert.Status.OPEN).exists()
