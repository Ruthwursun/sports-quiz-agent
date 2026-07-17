# 🏆 AI-Powered Sports Quiz Generation Agent

An intelligent **Retrieval-Augmented Generation (RAG)** application that generates dynamic sports quizzes by combining a local historical knowledge base with live web information. 

Built with **Streamlit**, **ChromaDB**, **Google Gemini**, and **DuckDuckGo Search**, the application creates engaging, context-aware multiple-choice quizzes across multiple sports.

---

## 🚀 Features

* 🎯 **Multi-Sport Support:** Generate quizzes for 10+ different sports categories.
* 📊 **Dynamic Difficulty:** Choose between *Easy*, *Medium*, and *Hard* settings.
* 📚 **Hybrid Retrieval:** Blends historical sports facts from **ChromaDB** with real-time web context via **DuckDuckGo Search**.
* 🤖 **Generative AI Engine:** Leverages **Google Gemini** for high-quality, contextual question and distraction option phrasing.
* 🔍 **Context Transparency:** Inspect the exact RAG context used to build each quiz.
* 🎨 **Enhanced UI:** Custom Streamlit interface featuring a clean layout and polished user experience.

---

## 🧠 Architecture Flow

```
                  User Input
                      │
                      ▼
          Select Sport & Difficulty
                      │
                      ▼
      Retrieve Historical Facts (ChromaDB)
                      │
           ┌──────────┴──────────┐
           ▼                     ▼
   Live Sports Search    Historical Context
     (DuckDuckGo)                │
           │                     │
           └──────────┬──────────┘
                      ▼
             Combined RAG Context
                      │
                      ▼
                Google Gemini
                      │
                      ▼
              AI-Generated Quiz
                      │
                      ▼
             Streamlit Interface
```

---

## 🛠 Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **LLM Engine:** Google Gemini API (`google-generativeai`)
* **Vector Database:** ChromaDB
* **Web Search Engine:** DuckDuckGo Search API (`duckduckgo_search`)
* **Embeddings:** Sentence Transformers
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```text
sports-quiz-agent/
│
├── app.py                  # Streamlit application main entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .env                    # Local environment secrets (Git ignored)
│
├── data/
│   └── sports_facts.json   # Seed data for historical knowledge base
│
├── chroma_db/              # Persistent ChromaDB vector database files
│
└── src/
    ├── config.py           # Configuration and API setups
    ├── database.py         # ChromaDB operations (vector indexing & retrieval)
    ├── search.py           # Real-time web search implementations
    └── generator.py        # Gemini prompt templates and quiz generation logic
```

---

## 📖 Knowledge Base

The application utilizes a curated local knowledge base containing **150+ historical sports facts** covering:

* 🏏 Cricket
* ⚽ Football
* 🏸 Badminton
* 🎾 Tennis
* 🏀 Basketball
* 🏑 Hockey
* 🏎 Formula 1
* 🏐 Volleyball
* 🥊 Boxing
* ♟ Chess

These historical entries are converted to vector embeddings and stored locally inside ChromaDB to enable precise, semantic retrieval during execution.

---

## ✨ Enhancements & Upgrades

This implementation builds upon the baseline architecture with several key improvements:
* **Gemini Migration:** Transitioned the LLM core to **Google Gemini** for faster execution and nuanced content creation.
* **Expanded Corpus:** Upgraded the historical knowledge base from a basic sample script to **150+ high-yield facts** across 10 global sports.
* **Refactored UI:** Reworked standard Streamlit component layouts into structured visual blocks for a cleaner production look.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ruthwursun/sports-quiz-agent.git](https://github.com/Ruthwursun/sports-quiz-agent.git)
   cd sports-quiz-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and append your API key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

---

## 📸 Demo & Links

* 🌐 **Live Application: *[https://sports-quiz-agent.streamlit.app](https://ruthwursun-sports-quiz-agent.streamlit.app/)*
* 🎥 **Screen Recording / Walkthrough:** *[Add Google Drive link here]*

---

## 📌 Future Roadmap

* 📈 Interactive in-app scoring mechanism.
* 💡 Automated answer validation featuring step-by-step contextual explanations.
* 🏆 Global user leaderboards and session analytics.
* 🔐 User authentication and saved quiz history pipelines.

---

## 👨‍💻 Author

**Ruthwursun N**
* GitHub: [@Ruthwursun](https://github.com/Ruthwursun)
* LinkedIn: [Ruthwursun N](https://linkedin.com/in/ruthwursun)
