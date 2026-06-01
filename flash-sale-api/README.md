# Flash Sale API

## Setup

1. Activate the virtual environment on Windows PowerShell:

```powershell
cd "G:\Challenge 1\flash-sale-api"
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r backend/requirements.txt
```

3. Run the Django development server:

```powershell
cd backend
python manage.py runserver
```

4. Run the load test from the project root after the server is running:

```powershell
python load-test.py
```
