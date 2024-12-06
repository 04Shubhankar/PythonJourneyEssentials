import logging  # Import the logging module for logging functionalities

logging.basicConfig(filename="newfile.log",  # Configure basic logging setup
                    format='%(asctime)s %(message)s',  # Set the format for log messages (timestamp and message)
                    filemode='w')  # Overwrite the log file content

main = logging.getLogger('main')  # Create a logger named 'main'
main.setLevel(logging.DEBUG)  # Set the logging level for the 'main' logger to DEBUG

main.warning("It is a warning")  # Log a warning message
main.error("You are trying to divide by zero")  # Log an error message
main.critical("Internet is down")  # Log a critical message
