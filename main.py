import ollama
import tools.calculator as cal
import tools.weather as wtr
import tools.time as time
import tools.memory_tool as mry
import logging
import os


print("Welcome to my AI agent")

MODEL_NAME = "qwen2.5:1.5b"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename = "logs/agent.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    force = True
)


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
    },
    {
            "type": "function",
            "function": {
                "name": "time",
                "description": "Get the current time of a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city to get the time"
                        }
                    },
                    "required": ["location"]
                }
            }
        },
        {
                    "type": "function",
                    "function": {
                        "name": "memory",
                        "description": "Get the memory",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "content": {
                                    "type": "string",
                                    "description": "Memory to be stored"
                                }
                            },
                            "required": ["content"]
                        }
                    }
                }
]


messages = [
    {
        "role": "system",
        "content": """You are a helpful AI assistant, youre name is TURING, you were created by zermello, youre founder is zermello too. Answer clearly and concisely.
          For current weather questions, always use the weather tool and never make up weather information.
          For calculation questions always use the calculate tool and never make up calculate information.
          For time questions always use the time tool and never make up time information
          For requests to remember, save, store, or not forget information, always use the memory tool."""
    }
]




def route_request(user_input):
    intents = []
    user_input = user_input.lower()

    if "time" in user_input:
            intents.append("time")

    if "weather" in user_input:
            intents.append("weather")

    if any(phrase in user_input for phrase in ["remember", "save this", "store this", "don't forget"]):
                intents.append("memory")

    if any(operator in user_input for operator in ["+", "-", "*", "/"]):
            intents.append("calculate")

    if not intents:
         intents.append("none")

    return intents
   
while True:

    user_message = input("What do you want to know?: ")
    intents = route_request(user_message)
    print(intents)

    if user_message.lower() == "exit":
        print("Goodbye!")
        break


    # Add user message to memory
    messages.append({
        "role": "user",
        "content": user_message
    })

    logging.info(f"USER: {user_message}")

    selected_tools = []

    for tool in tools:
         tool_name = tool["function"]["name"]

         if tool_name in intents:
              selected_tools.append(tool)


    # Ask Ollama what to do
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        tools=selected_tools
    )


    # If Ollama wants to use a tool
    if response.message.tool_calls:

        # Save Ollama's tool-call message
        messages.append(response.message)

        for  tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            function_arguments = tool_call.function.arguments

            logging.info(f"FUNCTION: {function_name}")


            # Calculator tool
            if function_name == "calculate":

                expression = function_arguments["expression"]

                result = cal.calculate(expression)
                logging.info(f"RESULT: {result}")


            # Weather tool
            elif function_name == "weather":

                city = function_arguments["city"]

                result = wtr.get_weather(city)
                logging.info(f"RESULT: {result}")
            
            elif function_name == "time":

                location = function_arguments["location"]["value"]

                result = time.get_time(location)
                logging.info(f"RESULT: {result}")

            elif function_name == "memory":
            
                    content = function_arguments["content"]
                    
            
                    result = mry.memory_tool(content)
                    logging.info(f"RESULT: {result}")



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
        logging.info(f"AI: {final_response.message.content}")


        # Save final answer to memory
        messages.append({
            "role": "assistant",
            "content": final_response.message.content
        })


    # Normal conversation without tools
    else:

        print(response.message.content)
        logging.info(f"AI: {response.message.content}")

        messages.append({
            "role": "assistant",
            "content": response.message.content
        })