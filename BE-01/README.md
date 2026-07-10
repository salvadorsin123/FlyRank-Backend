## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. Clone the repository:
```bash
git clone < https://github.com/salvadorsin123/FlyRank-Backend/tree/84d99449885ffe4f01cf06e70fc6ea4814e8db82/BE-01 >
cd BE-01
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
Returns the current application status at `http://localhost:8000/status`

**Response:**
```json
{
  "status": "ok",
  "fase": "Setup Week 1"
}
```