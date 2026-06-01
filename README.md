# Flash Sale API

A simple Django-based flash sale API with a load-testing script.

## Prerequisites

- Python 3.11+ installed
- Git (optional)
- Windows PowerShell for the provided activation commands

## Setup

1. Open PowerShell and change to the project root:

```powershell
cd "G:\Challenge 1\flash-sale-api"
```

2. Create a virtual environment if one does not already exist:

```powershell
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install project dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

## Run the API server

From the project root, start the Django development server:

```powershell
cd backend
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/` by default.

## Run load test

With the server running, return to the project root and execute:

```powershell
cd ..
python load-test.py
```

## Notes

- If you are using a different shell or operating system, adjust the virtual environment activation command accordingly.
- The main Django project files are located in `backend/`, while the load test script is in the project root.
