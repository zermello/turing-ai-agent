# 🤖 Turing AI Agent

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

Turing can retrieve live weather information for a requested location.

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

This allows the agent to transform a human-readable city name into geographical coordinates before requesting weather data.

---

## 🔗 Multi-Step Data Flow

Turing already combines multiple systems in a single workflow:

```text
User
 │
 ▼
Local LLM
 │
 ▼
Tool Selection
 │
 ├───────────────┐
 ▼               ▼
Calculator     Weather
 │               │
 ▼               ▼
Python        Geocoding API
                 │
                 ▼
           Latitude / Longitude
                 │
                 ▼
             Weather API
 │               │
 └───────┬───────┘
         ▼
     Tool Result
         │
         ▼
      Local LLM
         │
         ▼
    Final Response
```

---

# 🧠 Conversation Memory

During an active session, Turing stores:

- System instructions
- User messages
- Assistant responses
- Tool-call messages
- Tool results

This allows the agent to maintain conversational context while the program is running.

> Persistent memory across program restarts is planned for a future version.

---

# 🏗️ Current Architecture

```text
                    ┌──────────────┐
                    │     USER     │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      TURING     │
                  │   Python Agent  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Local LLM    │
                  │      Qwen       │
                  └────────┬────────┘
                           │
                    Tool Required?
                     │           │
                   NO            YES
                   │              │
                   ▼              ▼
                Response     Tool Selection
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                    Calculator          Weather
                         │                 │
                         ▼                 ▼
                    Python Tool      Geocoding API
                                           │
                                           ▼
                                   Weather API
                         │                 │
                         └────────┬────────┘
                                  ▼
                             Tool Result
                                  │
                                  ▼
                              Local LLM
                                  │
                                  ▼
                            Final Response
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core agent logic and tool execution |
| Ollama | Local LLM runtime |
| Qwen 2.5 | Language model |
| REST APIs | External data retrieval |
| Open-Meteo | Geocoding and weather data |
| JSON | API response processing |

---

# 📁 Project Structure

```text
turing-ai-agent/
│
├── main.py
├── README.md
├── .gitignore
│
└── tools/
    ├── calculator.py
    └── weather.py
```

---

# 🔄 Agent Execution Flow

When the user sends a message:

```text
1. User sends a request
        ↓
2. Request is added to conversation memory
        ↓
3. Local LLM analyzes the request
        ↓
4. LLM decides:
       "Do I need a tool?"
        ↓
5. If yes, the LLM selects a tool
        ↓
6. Python extracts:
       • Tool name
       • Tool arguments
        ↓
7. Python executes the correct function
        ↓
8. Tool result is added to the conversation
        ↓
9. LLM receives the result
        ↓
10. LLM generates a natural-language answer
        ↓
11. Final response is saved to memory
```

---

# 🚀 Development Roadmap

Turing is being developed from a basic tool-using agent into a more capable and modular AI system.

## 🟢 Foundation — Completed

- [x] Local LLM integration
- [x] Conversational interaction
- [x] Session-based memory
- [x] LLM-powered tool calling
- [x] Dynamic tool routing
- [x] Calculator tool
- [x] Weather tool
- [x] City-to-coordinate geocoding
- [x] Multi-step API workflow
- [x] Tool results returned to the LLM
- [x] Final response generation after tool execution
- [x] Modular tool structure

## 🟡 Reliability & Python Engineering

- [ ] Error handling
- [ ] Custom exceptions
- [ ] API status validation
- [ ] Request timeouts
- [ ] Logging
- [ ] Configuration management
- [ ] Environment variables
- [ ] Type hints

## 🧠 Advanced Agent Capabilities

- [ ] Multiple tool calls
- [ ] Multi-step autonomous workflows
- [ ] Dynamic tool registry
- [ ] Tool discovery
- [ ] Agent state management
- [ ] Task planning
- [ ] Tool execution history

## 💾 Persistent Memory

- [ ] SQLite integration
- [ ] Long-term memory
- [ ] Conversation storage
- [ ] Memory retrieval
- [ ] Selective memory
- [ ] Context management

## 🌐 External Intelligence

- [ ] Web search
- [ ] Information retrieval
- [ ] Source-aware responses
- [ ] Additional API integrations

## 📄 Document Intelligence

- [ ] PDF processing
- [ ] CSV analysis
- [ ] JSON and file analysis
- [ ] Document question answering

## 🔎 Retrieval-Augmented Generation

- [ ] Embeddings
- [ ] Document chunking
- [ ] Semantic search
- [ ] Vector database
- [ ] Knowledge base
- [ ] Retrieval-Augmented Generation (RAG)

## ⚡ Advanced Python

- [ ] Async programming
- [ ] Concurrent tool execution
- [ ] Background tasks
- [ ] Advanced OOP architecture
- [ ] Design patterns

## 🧪 Software Quality

- [ ] Unit testing
- [ ] Integration testing
- [ ] API mocking
- [ ] Automated test suite
- [ ] Code quality checks

## 🖥️ Backend & Interface

- [ ] FastAPI backend
- [ ] REST API endpoints
- [ ] Streaming responses
- [ ] Web interface
- [ ] Agent monitoring

---

# 🎯 Project Goal

The goal of Turing is to explore how modern AI agents combine language models with external tools, APIs, memory, retrieval systems, and multi-step workflows.

The project is also a hands-on journey through Python software engineering, covering concepts ranging from APIs and modules to databases, asynchronous programming, testing, backend development, and AI systems.

Rather than simply connecting an LLM to a chat interface, Turing is being built as an extensible system capable of:

```text
Understand
    ↓
Reason
    ↓
Choose tools
    ↓
Execute actions
    ↓
Process results
    ↓
Use memory
    ↓
Perform multi-step workflows
    ↓
Respond
```

---

# 🔮 Vision

The long-term vision for Turing is a modular, extensible AI agent capable of interacting with external systems, retrieving information, using long-term memory, processing documents, and autonomously coordinating multiple tools to solve increasingly complex tasks.

```text
                 TURING

                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
      Memory      Tools      Knowledge
         │          │          │
         ▼          ▼          ▼
      SQLite      APIs       RAG
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
          Search  Files  Workflows
                    │
                    ▼
                AI AGENT
```

---

## ⚙️ Running Locally

Clone the repository:

```bash
git clone <repository-url>
cd turing-ai-agent
```

Install dependencies:

```bash
pip install ollama requests
```

Make sure Ollama is running and download the model:

```bash
ollama pull qwen2.5:1.5b
```

Run the agent:

```bash
python main.py
```

---

## 👨‍💻 Author

Built by **Zermello**.

---

> **Turing is not a finished product. It is an evolving AI agent project designed to grow in complexity alongside the engineering skills behind it.** 🤖🚀
