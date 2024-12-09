import logging
from utils.config import LOG_DIR

def setup_logger(name):
    """
    Configura um logger básico.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(f"{LOG_DIR}/{name}.log", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
