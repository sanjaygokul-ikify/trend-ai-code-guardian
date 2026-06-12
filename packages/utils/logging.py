import logging

class LoggingMixin:
    def __init__(self, logger_name: str) -> None:
        self.logger = logging.getLogger(logger_name)

    def log_info(self, message: str) -> None:
        self.logger.info(message)

    def log_error(self, message: str) -> None:
        self.logger.error(message)