import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=api_key)


def web_search(query):
    result = client.search(query)
    result = result["results"][:3]
    return result

print(web_search("what is github"))