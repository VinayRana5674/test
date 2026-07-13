def count_digits(value):
    """Count the number of digit characters in the given value.

    Works for integers (the sign is ignored) and for arbitrary text.
    """
    return sum(1 for char in str(value) if char.isdigit())


if __name__ == "__main__":
    user_input = input("Enter a number or some text: ")
    print(f"Number of digits: {count_digits(user_input)}")
