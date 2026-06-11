import logging

logging.basicConfig(
    filename = "app.log",       
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("App started")
logging.info("User logged in")
logging.info("Fetched 100 records from DB")
logging.warning("Memory usage at 80%")
logging.error("Failed to send email")
logging.critical("Server is down")

print("Logs written to app.log")