# Turing AI Agent

> **An extensible AI agent that can understand requests, decide when to use tools, execute Python functions, retrieve real-world data, maintain conversation context, and return intelligent responses.**

Turing is a locally running AI agent built with Python and Ollama.

Unlike a traditional chatbot that only generates text, Turing can determine when external tools are required, select an appropriate tool, execute it through Python, process the result, and use that information to generate a final response.

The project is being developed into a modular AI agent platform with persistent memory, multi-step workflows, web search, document intelligence, asynchronous execution, and more.

---

# ⚡ Current Capabilities

## 💬 Conversational AI

Turing can hold conversations using a locally running language model.

Conversation messages are maintained throughout the active session, allowing the agent to use previous messages as context.

```text
User
  ↓
Message added to conversation history
  ↓
Local LLM processes conversation context
  ↓
Response
  ↓
Response saved to conversation history
```

---

## 🧠 LLM-Powered Tool Calling

Turing does not manually choose a tool using simple keyword matching.

Instead, the language model receives descriptions of the available tools and decides whether a tool is necessary.

```text
User Request
      │
      ▼
   Local LLM
      │
      ├── No tool needed ──► Generate response
      │
      └── Tool needed
              │
              ▼
        Select appropriate tool
              │
              ▼
       Python executes tool
```

---

## 🧮 Calculator Tool

Turing can recognize mathematical requests and route them to a dedicated Python calculator tool.

Example:

```text
User: What is 125 * 8?

        ↓

LLM selects:

calculate(expression)

        ↓

Python executes calculation

        ↓

Result returned to LLM

        ↓

Final response
```

---

## 🌤️ Live Weather Tool

Turing can retrieve current weather information for a requested location.

The weather system uses a multi-step API workflow.

```text
City Name
    │
    ▼
Geocoding API
    │
    ▼
Latitude + Longitude
    │
    ▼
Weather API
    │
    ▼
Current Temperature
```

This allows the agent to transform a human-readable location into geographical coordinates before requesting weather data.

---

## 🔧 Tools

| Tool | Purpose |
|---|---|
| 🧮 Calculator | Mathematical calculations |
| 🌤️ Weather | Current weather information |
| ⏰ Time | Time and time zones |
| 🌐 Web Search | Internet search using Tavily |
| 🧠 Memory | Persistent storage using SQLite |

---

## 🧠 Persistent Memory

Turing can store information in a local SQLite database and retrieve it after the program is restarted.

User → Memory Tool → SQLite → Future Conversation → Turing retrieves the information

---

## 📁 Project Structure

    turing-ai-agent/
    │
    ├── main.py
    ├── README.md
    ├── requirements.txt
    ├── .env
    ├── .gitignore
    │
    ├── data/
    │   └── memory.db
    │
    ├── logs/
    │   └── agent.log
    │
    └── tools/
        ├── calculator.py
        ├── weather.py
        ├── time.py
        ├── memory_tool.py
        ├── web_search.py
        └── registry.py

> `.env` contains private API credentials and should never be committed to GitHub.

---

## 🛠️ Tech Stack

- **Python** — Agent logic and tool execution
- **Ollama** — Local LLM runtime
- **Qwen 2.5** — Language model
- **SQLite** — Persistent memory
- **Tavily** — Web search
- **Open-Meteo** — Weather data
- **python-dotenv** — Environment configuration

---

## 🚀 Run Locally

### 1. Clone the repository

    git clone <repository-url>
    cd turing-ai-agent

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Download the model

    ollama pull qwen2.5:1.5b

Make sure Ollama is running.

### 4. Configure Tavily

Create a `.env` file:

    TAVILY_API_KEY=your_api_key_here

### 5. Run Turing

    python main.py

---

## 🗺️ Roadmap

### Completed

- [x] Local LLM integration
- [x] Conversational context
- [x] Tool calling
- [x] Dynamic tool registry
- [x] Calculator
- [x] Weather
- [x] Time
- [x] Persistent SQLite memory
- [x] Web search
- [x] Multiple tool calls
- [x] Logging
- [x] Error handling

### Next

- [ ] Improved agent loop
- [ ] Multi-step autonomous tasks
- [ ] Tool validation
- [ ] Conversation persistence
- [ ] Relevant memory retrieval
- [ ] Async tool execution
- [ ] Automated testing
- [ ] FastAPI backend
- [ ] Local web interface
- [ ] Document processing
- [ ] RAG

---

## 🎯 Why I'm Building Turing

Turing is a hands-on project for understanding how **AI agents are actually engineered** — combining language models with tools, APIs, databases, memory, and eventually autonomous multi-step workflows.

The goal isn't simply to build another chatbot.

It's to build an agent whose **capabilities and architecture can grow over time**.

---

## 👨‍💻 Author

**Zermello**

Built with Python, curiosity, and a lot of debugging. 🤖

---

> **Turing is not a finished product. It is an evolving AI agent project designed to grow in complexity alongside the engineering skills behind it.** 🤖🚀
