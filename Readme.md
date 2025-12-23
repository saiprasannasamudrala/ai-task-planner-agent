## AI Task Planner Agent (LLM-Powered)

### Overview
This project demonstrates an **Agentic AI system powered by a local Large Language Model (LLM)** using **Ollama**.  
The agent takes natural language instructions, allows the LLM to generate structured **JSON-based decisions**, and executes the appropriate tools automatically.

This version upgrades the agent from rule-based logic to **LLM-driven decision making**, reflecting real-world agent architectures.

---

### How It Works
1. Takes user input in natural language
2. Uses an LLM (via Ollama) to understand intent and extract values
3. LLM generates a structured JSON decision (tool + inputs)
4. The agent validates the JSON
5. Executes the selected tool and saves the output

---

### Agent Flow
User Input
↓
LLM (Ollama)
↓
JSON Decision
↓
Tool Execution
↓
Output Saved


---

### Tools Implemented
- `cal_sum(a, b)` – Adds two numbers  
- `cal_sub(a, b)` – Subtracts two numbers  
- `cal_multiply(a, b)` – Multiplies two numbers  
- `save_to_file(text)` – Saves the output to a file  

All tools are implemented as **safe, predefined Python functions**.

---

### Key Concepts Used
- Agentic AI design
- LLM-based decision making
- JSON as an action interface
- Tool routing and execution
- Input validation and error handling
- Local LLM integration using Ollama

---

### Example

**Input**
multiply 20 and 30

**LLM Decision (JSON)**
```json
{
  "tool": "cal_multiply",
  "inputs": {
    "a": 20,
    "b": 30
  }
}

**Output**
600

