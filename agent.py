import ollama
import json
from tools import cal_sum, cal_sub, cal_multiply, save_to_file

system_prompt = """
You are an AI agent.

Your task:
- Understand the user request
- Decide which tool to use
- Respond ONLY in valid JSON
- Do not explain anything

Available tools:
- cal_sum(a, b)
- cal_sub(a, b)
- cal_multiply(a, b)

JSON format:
{
  "tool": "<tool_name>",
  "inputs": {
    "a": number,
    "b": number
  }
}
"""
user_input = input("What do you want to do? ")

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)

llm_output = response["message"]["content"]
print("\nLLM Output (Raw):")
print(llm_output)

try:
    decision = json.loads(llm_output)
except json.JSONDecodeError:
    print("LLM did not return valid JSON")
    exit()
# Parse JSON
decision = json.loads(llm_output)

tool = decision["tool"]
inputs = decision["inputs"]

# Execute tool
if tool == "cal_sum":
    result = cal_sum(**inputs)

elif tool == "cal_sub":
    result = cal_sub(**inputs)

elif tool == "cal_multiply":
    result = cal_multiply(**inputs)

else:
    print("Unsupported tool")
    exit()

print("Result:", result)
save_to_file(result)
print("saved successfully")

