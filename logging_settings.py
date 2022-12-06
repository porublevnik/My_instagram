import logging


def create_logger(logger_name):
    logger = logging.getLogger(f"{logger_name}")

    file_handler = logging.FileHandler("logs/api.log")
    formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter_api)

    logger.addHandler(file_handler)
    return(logger)