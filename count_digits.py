def count_digits(number):
    """Count the number of digits in an integer.

    Works for negative numbers too (the sign is ignored).
    """
    return len(str(abs(number)))


def count_digits_in_string(text):
    """Count how many characters in a string are digits."""
    return sum(1 for char in text if char.isdigit())


if __name__ == "__main__":
    user_input = input("Enter a number or some text: ")

    # If the input is a valid integer, count its digits;
    # otherwise count the digit characters in the text.
    stripped = user_input.strip()
    if stripped.lstrip("-").isdigit():
        print(f"Number of digits: {count_digits(int(stripped))}")
    else:
        print(f"Number of digit characters: {count_digits_in_string(user_input)}")
