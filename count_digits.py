import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class DigitCounter:
    """Count digit characters in a given value.

    Works for integers (the sign is ignored) and for arbitrary text.
    """

    def __init__(self, value):
        self.value = value
        logger.debug("Created DigitCounter for value: %r", value)

    def count(self):
        """Return the number of digit characters in the stored value."""
        text = str(self.value)
        result = sum(1 for char in text if char.isdigit())
        logger.info("Counted %d digit(s) in %r", result, text)
        return result


if __name__ == "__main__":
    user_input = input("Enter a number or some text: ")
    logger.info("Received input from user")
    print(f"Number of digits: {DigitCounter(user_input).count()}")
