from django.contrib import admin

from .models import Alert, Incident, SecurityLog

admin.site.register(SecurityLog)
admin.site.register(Alert)
admin.site.register(Incident)
