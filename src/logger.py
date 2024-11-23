import logging
import os

def setup_logger():
    # Create a logger
    logger = logging.getLogger('sports_odds_scraper')
    logger.setLevel(logging.DEBUG)  # Set the overall logging level

    # Create a file handler that logs to a file
    log_file_path = os.getenv('LOG_FILE', 'scraper.log')  # Get log file path from env variable or use default
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)  # Log all messages to the file

    # Create a console handler that logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Log messages to console

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize the logger
logger = setup_logger()