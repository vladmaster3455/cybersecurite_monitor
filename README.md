# Cybersecurity Monitoring API

Backend Django REST Framework pour detection d'activites suspectes, logs securite, alertes, incidents et dashboard SOC.

## Stack

- Django REST Framework
- JWT SimpleJWT
- PostgreSQL
- Rate limiting DRF
- Middleware d'audit securite
- Swagger/OpenAPI

## Lancement

```bash
cp .env.example .env
docker compose up --build
```

API docs : `http://localhost:8003/api/docs/`

## Modules

- `security` : logs, detection d'anomalies, alertes, incidents
- `monitoring` : dashboard SOC
- `accounts` : roles analyste, manager SOC, admin
- `common` : pagination et gestion d'erreurs
# cybersecurite_monitor
