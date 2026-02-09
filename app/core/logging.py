import logging
import os
from datetime import datetime

import logging.handlers

# Create logs directory if it doesn't exist
LOG_DIR = os.path.join(os.path.dirname(__file__), '../../logs')
os.makedirs(LOG_DIR, exist_ok=True)

#

def setup_logger():
    """ Configure logger"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(LOG_DIR, 'app.log'),
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    

def get_logger(name):
    """Get a logger instance"""
    return logging.getLogger(name)