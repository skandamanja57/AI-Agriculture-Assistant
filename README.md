# 🌱 AgriAI — AI Agriculture Assistant

An intelligent farming assistant powered by a **local LLM (Llama 3.2 via Ollama)** and a **FastAPI backend**. Get practical guidance for crops, irrigation, fertilizers, plant diseases, and more — all running locally on your machine.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 **AI Chat** | Ask farming questions powered by Llama 3.2 + RAG knowledge base |
| 🔬 **Disease Detector** | Upload a leaf photo for AI-powered plant disease analysis |
| 📅 **Crop Calendar** | Visual 12-month planting & harvest calendar by crop & region |
| 🌦️ **Weather Widget** | Live weather + farming advice based on your location |
| 🎙️ **Voice Input** | Speak your farming questions (Chrome/Edge) |
| 💾 **Chat History** | Auto-saved conversations in sidebar (localStorage) |
| 🌐 **Multi-language** | Responses in Hindi, Tamil, Telugu, Bengali, Marathi & more |

---

## 🛠️ Tech Stack

- **Frontend**: Vanilla HTML/CSS/JavaScript (no frameworks)
- **Backend**: Python + FastAPI + Uvicorn
- **AI Model**: Llama 3.2 via [Ollama](https://ollama.com) (runs locally)
- **RAG**: Custom cosine-similarity retrieval over agriculture knowledge base
- **Weather**: [Open-Meteo API](https://open-meteo.com/) (free, no API key needed)

---

## 📁 Project Structure

```
AI-Agriculture-Assistant/
├── backend/
│   └── main.py               # FastAPI server (chat + disease detection endpoints)
├── chatbot/
│   ├── ai_chatbot.py         # LLM prompt builder using Ollama
│   └── rag.py                # RAG search over agriculture knowledge
├── data/
│   └── agriculture_knowledge.txt  # Knowledge base (Rice, Wheat, Tomato, etc.)
├── frontend/
│   └── index.html            # Full single-page app UI
├── models/                   # (For future ML models)
├── disease_detection/        # (For future disease ML module)
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Agriculture-Assistant.git
cd AI-Agriculture-Assistant
```

### 2. Create virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the AI model
```bash
ollama pull llama3.2
# Optional: for image-based disease detection
ollama pull llama3.2-vision
```

### 5. Start the backend
```bash
uvicorn backend.main:app --reload
```

### 6. Open the frontend
Open `frontend/index.html` in **Chrome or Edge**.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/ask` | Send a farming question, get AI answer |
| `POST` | `/detect-disease` | Upload leaf image for disease analysis |

---

## 📝 Requirements

Create a `requirements.txt` with:
```
fastapi
uvicorn
ollama
python-multipart
```

---

## 🌿 Knowledge Base

The assistant uses a local RAG knowledge base covering:
- 🌾 Rice, Wheat, Maize
- 🍅 Tomato, Potato
- 🎋 Sugarcane
- 🧪 Fertilizer guidance
- 💧 Irrigation techniques
- 🍃 Plant diseases (early blight, late blight, etc.)

---

## 📄 License

MIT License — feel free to use and modify.

---

*Built with ❤️ for farmers everywhere.*
