import logging  # Import the logging module

logging.basicConfig(  # Configure basic logging setup
    filename='msg.log',  # Specify the log file name
    filemode='w',  # Set the file mode to overwrite existing content
    format='%(name)s %(levelname)s - %(message)s'  # Define the log message format
)

logging.warning("This will get logged to a file.")  # Log a warning message
