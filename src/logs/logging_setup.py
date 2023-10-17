import logging
import os
from logging.handlers import RotatingFileHandler
import sys


def log():
    home = os.path.expanduser("~")

    # For Windows
    app_data_folder = os.path.join(home, "AppData", "Local", "Hangman", "Logs")

    if not os.path.exists(app_data_folder):
        os.makedirs(app_data_folder)

    logger = logging.getLogger("hangman_logger")
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(
        f"{app_data_folder}/hangman.log", maxBytes=int(1e6), backupCount=5
    )  # Maximum filesize = 1MB
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


# Custom function to log unhandled exceptions
def log_unhandled_exceptions(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("hangman_logger")
    if exc_type is KeyboardInterrupt:
        # Don't log keyboard interrupts, just pass through.
        logger.info("Game ended")
    else:
        logger.error(
            "Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback)
        )


# Override the default sys.excepthook with our custom function
sys.excepthook = log_unhandled_exceptions
