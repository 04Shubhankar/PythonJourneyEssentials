import logging

# Create a logger
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
