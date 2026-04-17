
# HNG Stage 1 API

A simple REST API built with FastAPI.

## Requirements

- Python 3.8+
- pip

## Running Locally

1. Clone the repository and navigate into it:

```bash
git clone https://github.com/AdescoDevOps/hng-stage1.git
cd hng-stage1
```

2. Create and activate a virtual environment:

```bash
python -m venv henv
# Windows
henv\Scripts\activate
# macOS/Linux
source henv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### GET /

Returns a status message confirming the API is running.

**Response:**
```json
{
  "message": "Api is running"
}
```

---

### GET /health

Returns the health status of the API.

**Response:**
```json
{
  "message": "healthy"
}
```

---

### GET /me

Returns profile information.

**Response:**
```json
{
  "name": "Ojo Emmanuel",
  "email": "adescocloud@gmail.com",
  "github": "https://github.com/AdescoDevOps"
}
```
