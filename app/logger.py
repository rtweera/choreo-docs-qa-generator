import logging
import os


class Logger:
    def __init__(self, logger_name, log_filename, level=logging.INFO, log_dir="logs"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level=level)

        os.makedirs(log_dir, exist_ok=True)
        filepath = os.path.join(log_dir, log_filename)
        file_handler = logging.FileHandler(filename=filepath)
        file_handler.setLevel(level=level)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_formatter = logging.Formatter("%(levelname)s - %(message)s")
        stream_handler.setFormatter(stream_formatter)

        # Add handlers if not already added
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)
        else:
            # Avoid duplicate logs if rerun in some environments
            self.logger.handlers.clear()
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)

    def __getattr__(self, name):
        """
        Allow us to call the method we pass into the object (like `.info()`, `error()`) on the original
        logger object. (saves us from needing to redefine the methods again)
        """
        return getattr(self.logger, name)
