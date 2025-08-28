# Zodiac Compatibility (Flask)

A simple Flask web app that calculates zodiac compatibility using `zoDATA.csv` and renders results via HTML templates and static assets.

## Quick start (Windows / PowerShell)

```powershell
# From the project root where this README lives
cd flask

# (Optional) Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

App starts in debug mode at `http://127.0.0.1:5000/`.

## Project structure

```
flask/
  app.py            # Flask entrypoint
  a.py              # Script to test compatibility function via CLI
  zoDATA.csv        # Dataset used by the app
  templates/        # Jinja2 HTML templates
  static/           # CSS, JS, images
```

## Notes

- Ensure you run the app from the `flask` directory so `zoDATA.csv` is found by relative path.
- If port 5000 is in use, set `FLASK_RUN_PORT` or change the `app.run(...)` call.
- To exit the venv: `deactivate`.

## Routes

- `/` → main page
- `/test` → test page
- `/submit` (POST) → handles form submission and renders result
- `/profile`, `/about`, `/faq` → additional pages 
