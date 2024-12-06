import logging  # Import the logging module

logging.basicConfig(  # Configure basic logging setup
    filename='log.txt',  # Specify the log file name
    level=logging.DEBUG  # Set the logging level to DEBUG
)

print("Logging Module Demo")  # Print a message to the console

logging.debug("This is debug message")  # Log a debug message
logging.info("This is info message")  # Log an info message
logging.warning("This is warning message")  # Log a warning message
logging.error("This is error message")  # Log an error message
logging.critical("This is critical message")  # Log a critical message
