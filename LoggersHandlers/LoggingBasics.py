import logging

# Configure basic logging setup (optional, but recommended)
logging.basicConfig(level=logging.DEBUG)  # Set the logging level

# Create a logger instance
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug("This is a debug message")  # Detailed information for debugging
logger.info("This is an informative message")  # General information
logger.warning("This is a warning message")  # Potential issue
logger.error("This is an error message")  # An error occurred
logger.critical("This is a critical message")  # Serious error


"""

Explanation:

Import the logging module: This line imports the necessary module for logging functionality in Python.

Configure basic logging setup (optional):

logging.basicConfig(level=logging.DEBUG): This line configures the basic logging setup, specifying that all log messages with a level of DEBUG or higher will be printed to the console. You can adjust the level argument to control which log levels are displayed.
Create a logger instance:

logger = logging.getLogger(__name__): This line creates a logger instance named __name__, which is typically the name of the current module. This allows you to organize log messages from different parts of your application.
Log messages at different levels:

logger.debug("This is a debug message"): Logs a debug message, which is useful for detailed information during development and troubleshooting.
logger.info("This is an informative message"): Logs an informative message, providing general information about the application's behavior.
logger.warning("This is a warning message"): Logs a warning message, indicating a potential issue that might lead to an error in the future.
logger.error("This is an error message"): Logs an error message, indicating an error condition that has prevented some operation from completing.
logger.critical("This is a critical message"): Logs a critical message, indicating a serious error that has caused the system to become unusable.
"""
