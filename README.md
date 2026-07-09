# 🚀 FlyRank

Backend AI Engineering

## 📋 Description


## ✅ Task Status

| Task | Description | Status |
|------|-------------|--------|
| **BE-01** | Build first API endpoint | ✅ Completed |

## 🛠️ Technologies

- **FastAPI** - Modern web framework
- **Python** - Programming language
- **Uvicorn** - ASGI server

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd FlyRank
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

To start the development server:

```bash
cd BE-01
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

### Available Endpoints

#### GET /
Returns a welcome message.

**Response:**
```json
{
  "mensaje": "¡Hola, FlyRank!",
  "mensagge!": "¡Hola, FlyRank!"
}
```

#### GET /status
Returns the current application status.

**Response:**
```json
{
  "status": "ok",
  "fase": "Setup Week 1"
}
```

## 📚 Interactive Documentation

Once the server is running, you can access:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🤖 AI Tools Used

- **Claude Haiku 4.5** - For development assistance and code generation
- **Gemini Pro** - For development assistance and code generation

## 🔄 Upcoming Tasks

- BE-02: Implement authentication endpoint
- BE-03: Create data model for flights
- BE-04: Implement flight search functionality

## 🤝 Contributing

Contributions are welcome. Please open an issue or pull request.

## 📝 License

This project is under the MIT License.

---

Last updated: July 2026
