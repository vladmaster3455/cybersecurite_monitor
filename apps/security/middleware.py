from .services import SecurityLogService


class SecurityAuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith("/api/") and response.status_code >= 400:
            SecurityLogService.record(
                source_ip=self._client_ip(request),
                event_type="api_error",
                severity="medium" if response.status_code < 500 else "high",
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
                endpoint=request.path,
                metadata={"status_code": response.status_code, "method": request.method},
            )
        return response

    @staticmethod
    def _client_ip(request):
        forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
        return forwarded.split(",")[0] if forwarded else request.META.get("REMOTE_ADDR", "127.0.0.1")
