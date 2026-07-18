class DigitCounter:
    """Count digit characters in a given value.

    Works for integers (the sign is ignored) and for arbitrary text.
    """

    def __init__(self, value):
        self.value = value

    def count(self):
        """Return the number of digit characters in the stored value."""
        return sum(1 for char in str(self.value) if char.isdigit())


if __name__ == "__main__":
    user_input = input("Enter a number or some text: ")
    print(f"Number of digits: {DigitCounter(user_input).count()}")
