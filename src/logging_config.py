"""Centralized logging configuration."""
import logging
from pathlib import Path

def setup_logging(log_file: str = "logs/copilot.log") -> logging.Logger:
    """
    Configure logging for the application.
    
    Returns a logger that writes to both console and file with timestampe.
    """

    # ensure log directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # get the application logger
    logger = logging.getLogger("copilot")
    logger.setLevel(logging.INFO)

    # prevent duplicate handlers if called multiple times
    if logger.handlers:
        return logger
    
    # format: 20260-04-26 14:30:12 [INFO] message
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # handler 1: console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # handler 2: file output
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

