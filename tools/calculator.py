import logging

def calculate(expression):
    try:
      return eval(expression)
    except Exception as err:
       logging.error(f"ERROR: {err}")
       return f"An error has occured because of {err}"

