import ollama
import tools.calculator as cal
import tools.weather as wtr


print("Welcome to my AI agent")

MODEL_NAME = "qwen2.5:1.5b"


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "weather",
            "description": "Get the current weather of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to get the weather for"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant, youre name is Michalangelo, you were created by zermello, youre founder is zermello. Answer clearly and concisely."
    }
]


while True:

    user_message = input("What do you want to know?: ")

    if user_message.lower() == "exit":
        print("Goodbye!")
        break


    # Add user message to memory
    messages.append({
        "role": "user",
        "content": user_message
    })


    # Ask Ollama what to do
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        tools=tools
    )


    # If Ollama wants to use a tool
    if response.message.tool_calls:

        # Save Ollama's tool-call message
        messages.append(response.message)

        tool_call = response.message.tool_calls[0]

        function_name = tool_call.function.name
        function_arguments = tool_call.function.arguments


        # Calculator tool
        if function_name == "calculate":

            expression = function_arguments["expression"]

            result = cal.calculate(expression)


        # Weather tool
        elif function_name == "weather":

            city = function_arguments["city"]

            result = wtr.get_weather(city)


        # Add tool result to memory
        messages.append({
            "role": "tool",
            "content": str(result)
        })


        # Send tool result back to Ollama
        final_response = ollama.chat(
            model=MODEL_NAME,
            messages=messages
        )


        # Print final answer
        print(final_response.message.content)


        # Save final answer to memory
        messages.append({
            "role": "assistant",
            "content": final_response.message.content
        })


    # Normal conversation without tools
    else:

        print(response.message.content)

        messages.append({
            "role": "assistant",
            "content": response.message.content
        })