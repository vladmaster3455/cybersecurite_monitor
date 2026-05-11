from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ANALYST = "analyst", "Analyst"
        SOC_MANAGER = "soc_manager", "SOC Manager"
        ADMIN = "admin", "Admin"

    role = models.CharField(max_length=30, choices=Role.choices, default=Role.ANALYST)
