import logging

def setup_logging(level):
    logging.basicConfig(level=getattr(logging, level.upper()), 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    return logger

def handle_api_error(e):
    logger.error(f"API Error: {str(e)}")
    # Handle error gracefully or retry mechanism
