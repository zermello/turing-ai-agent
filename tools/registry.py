import tools.calculator as cal
import tools.weather as wtr
import tools.time as time
import tools.memory_tool as mry
import tools.web_search as web


tools = {

    "calculate": {
        "function": cal.calculate,
        "definition": {
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
        }
    },

    "weather": {
        "function": wtr.get_weather,
        "definition": {
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
    },

    "time": {
        "function": time.get_time,
        "definition": {
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
        }
    },

    "memory": {
        "function": mry.memory_tool,
        "definition": {
            "type": "function",
            "function": {
                "name": "memory",
                "description": "Save information to persistent memory. You MUST provide the information to save using the argument named content. Do not use any other argument name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The exact information that should be saved. Always use this field. Example: 'My name is Shon'."
                        }
                    },
                    "required": ["content"]
                }
            }
        }
    },
    "web_search": {
            "function": web.web_search,
            "definition": {
                "type": "function",
                "function": {
                    "name": "web_search",
                    "description": "search in web",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "the query to search"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        }
}
