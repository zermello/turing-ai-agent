import os
import logging
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=api_key)


def web_search(query):
    try:
        result = client.search(query)
        result = result["results"][:3]
        return result
    except Exception as err:
        logging.error(f"ERROR: {err}")
        return f"unexpected error occured. Try again"
