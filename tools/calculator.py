import logging

def calculate(expression):
    try:
      return eval(expression)
    except Exception as err:
       logging.error("fERROR: {err}")
       return f"An error has occured because of {err}"

