TaskFlow Teams API

API backend construida con FastAPI y PostgreSQL.

Requisitos
- Docker y Docker Compose
- (Opcional local) Python 3.13+

Configuracion
1. Crea un archivo `.env` en la raiz del proyecto usando como base `.env.example`.
2. Verifica que `DATABASE_URL` coincida con los valores `POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB`.

Ejecucion con Docker
1. Construir y levantar servicios:

```bash
docker compose up --build
```

2. API disponible en:
- `http://localhost:8000`

3. Documentacion interactiva:
- `http://localhost:8000/docs`

Ejecucion local (sin Docker)
1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Ejecutar la API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Estructura base
- `app/main.py`: instancia de FastAPI y endpoint raiz.
- `app/database.py`: engine de SQLAlchemy y dependencia de sesion.
- `docker-compose.yml`: servicios `app` y `db`.

Estado actual
- Endpoint raiz: `GET /`
- Integracion inicial con base de datos lista para ampliar con routers/modelos/schemas.
