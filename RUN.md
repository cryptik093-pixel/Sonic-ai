# Sonic AI V1

Local run:

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Optional: set `SONIC_AI_UPGRADE_URL` to your checkout or sales page.
4. Start the app with `flask --app wsgi run --debug`.
5. Open `http://127.0.0.1:5000`.

Smoke-testable flow:

- `GET /health`
- `POST /api/upload` with a WAV file field named `file`
- `POST /api/analyze/<job_id>`
- `GET /api/status/<job_id>`

Uploads start as `pending`, analysis runs as `running`, and completed reports return `succeeded`.
