import logging

logging.basicConfig(
    filename = "error.log",
    level = logging.ERROR,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

try:
    result = 100 / 0
except ZeroDivisionError:
    logging.error("Division by zero occurred", exc_info=True)
    print("Error logged to error.log")