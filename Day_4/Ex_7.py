import logging

logging.basicConfig(level = logging.DEBUG)

logging.debug("Starting application")
logging.info("User logged in")
logging.warning("Low disk space")
logging.error("Database connection failed")
logging.critical("System shutdown")