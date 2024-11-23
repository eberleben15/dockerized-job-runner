# src/__init__.py

# Importing the main modules
from .config import  JOBS  # Configuration settings
from .logger import logger                     # Logger setup
from .scheduler import start_scheduler          # Scheduler function


# Example of a version variable
__version__ = '1.0.0'