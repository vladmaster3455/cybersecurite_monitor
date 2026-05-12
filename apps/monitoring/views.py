from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.security.models import Alert, Incident, SecurityLog


class SecurityDashboardView(APIView):
    def get(self, request):
        return Response({
            "logs": SecurityLog.objects.count(),
            "open_alerts": Alert.objects.filter(status=Alert.Status.OPEN).count(),
            "incidents": Incident.objects.count(),
            "severity_distribution": list(SecurityLog.objects.values("severity").annotate(total=Count("id")).order_by("severity")),
            "recent_alerts": list(Alert.objects.order_by("-created_at").values("id", "title", "severity", "status", "source_ip")[:10]),
        })
