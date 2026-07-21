import logging


def setup_logging(level=logging.INFO):
    """Configure application-wide logging."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def get_logger(name):
    """Return a logger for the given module name."""
    return logging.getLogger(name)
