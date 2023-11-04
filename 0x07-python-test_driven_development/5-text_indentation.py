#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing spaces
    punctuations = ".?:"
    start = 0
    result = []

    for i in range(len(text)):
        if text[i] in punctuations:
            result.append(text[start:i+1])
            result.append("\n\n")
            start = i + 1

    result.append(text[start:])
    print("".join(result))
