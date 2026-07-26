from logging_config import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)


class PalindromeChecker:
    """Check whether a value reads the same forwards and backwards.

    Comparison ignores case and non-alphanumeric characters, so phrases
    like "A man, a plan, a canal: Panama" count as palindromes.
    """

    def __init__(self, value):
        self.value = value
        logger.debug("Created PalindromeChecker for value: %r", value)

    def is_palindrome(self):
        """Return True if the stored value is a palindrome."""
        cleaned = "".join(char.lower() for char in str(self.value) if char.isalnum())
        result = cleaned == cleaned[::-1]
        logger.info("%r is%s a palindrome", self.value, "" if result else " not")
        return result


if __name__ == "__main__":
    user_input = input("Enter a word, phrase, or number: ")
    logger.info("Received input from user")
    if PalindromeChecker(user_input).is_palindrome():
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
