import re
import json
from tools import cal_sum, cal_sub, cal_multiply, save_to_file

# 1️⃣ User input
user_input = input("What do you want to do? ").lower()
print("User want to do:", user_input)

# 2️⃣ Extract numbers
numbers = list(map(int, re.findall(r"\d+", user_input)))
a, b = numbers[0], numbers[1]

# 3️⃣ Detect operation
if "add" in user_input:
    operation = "cal_sum"
    result_value = a + b

elif "subtract" in user_input:
    operation = "cal_sub"
    result_value = a - b

elif "multiply" in user_input:
    operation = "cal_multiply"
    result_value = a * b

else:
    print("Unsupported operation")
    exit()

# 4️⃣ Agent decision (JSON)
agent_decision = {
    "steps": [
        {
            "tool": operation,
            "inputs": {
                "a": a,
                "b": b
            }
        },
        {
            "tool": "save_to_file",
            "inputs": {
                "text": result_value
            }
        }
    ]
}

print(json.dumps(agent_decision, indent=2))

# 5️⃣ Execute tools
for step in agent_decision["steps"]:
    tool = step["tool"]
    inputs = step["inputs"]

    if tool == "cal_sum":
        result = cal_sum(**inputs)

    elif tool == "cal_sub":
        result = cal_sub(**inputs)

    elif tool == "cal_multiply":
        result = cal_multiply(**inputs)

    elif tool == "save_to_file":
        print(save_to_file(**inputs))
        continue

    print("Result:", result)
