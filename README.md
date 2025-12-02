# 🧠 Memory + Personality Engine

A fully functional **Memory Extraction Module** and **Personality Engine**.  
This system analyzes user chat history (up to 30 messages), extracts structured memory,  
generates a neutral response, and transforms it into different personalities.

Perfect for AI assistant assignments, companion AI prototypes, and interviewing evaluations.

---

# ☁️ Deployment (Render — Free)

- API: `https://memory-personality-engine.onrender.com`
- Docs: `https://memory-personality-engine.onrender.com/docs`

---

## 🚀 Features

### ✅ **Memory Extraction Engine**
Extracts:
- User **preferences**
- **Emotional patterns**
- Long-term **facts worth remembering**

### ✅ **Personality Engine**
Transforms a neutral response into one of several tones:
- `calm_mentor`
- `witty_friend`
- `therapist`
- `strict_coach`
- `formal_consultant`
- `neutral`

### ✅ **Before/After Comparison**
Displays:
- `original` neutral response  
- `transformed` personality-based response  

### ✅ **FastAPI-based API**
+ Interactive documentation at `/docs`  
+ Clean modular code  
+ Fully deployable on Render (free)

---

## 🏗 Architecture Overview

### High-Level Flow

```
User Messages (30)
       ↓
Memory Extraction Module
       ↓
Structured Memory
       ↓
Neutral Response Generator (Static)
       ↓
Personality Engine
       ↓
Final Response
```

# 🧪 Example Input

```json
{
  "messages": [
    "I work as a data engineer.",
    "I like short explanations.",
    "Sometimes I feel anxious about interviews.",
    "I want to learn machine learning."
  ],
  "personality": "witty_friend"
}
```

---

# 📗 Example Output

```json
{
  "memory": {
    "preferences": ["I like short explanations."],
    "emotional_patterns": ["Sometimes I feel anxious about interviews."],
    "facts": ["I 
work as a data engineer.", "I want to learn machine learning."]
  },
  "personality_response": {
    "original": "Here is a neutral response to your message: 'I want to learn machine learning.'. Let me know if you'd like more details.",
    "transformed": "Alright, here’s the tea ☕:\n\nHere is a neutral response to your message: 'I want to learn machine learning.'. Let me know if you'd like more details.\n\nNow go shine, legend 😎"
  }
}
```

---

# ▶️ Run Locally

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Start the server
```
uvicorn app.main:app --reload
```

### 3️⃣ Open the API docs  
👉 http://127.0.0.1:8000/docs

---
