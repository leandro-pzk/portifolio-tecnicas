import re

def add(numbers_string):
    delimiter = ",|\n"

    if numbers_string.startswith("//"):
        delimiter = numbers_string[2 : numbers_string.index("\n")]
        numbers_string = numbers_string[numbers_string.index("\n") + 1 :]

    numbers_list = re.split(delimiter, numbers_string)

    negative_numbers = list(map(int, [x for x in numbers_list if x.startswith("-")]))
    if negative_numbers:
        exception_message = f"Negatives not allowed: {negative_numbers}"
        raise ValueError(exception_message)

    if numbers_list[0] == "":
        return 0

    try:
        return sum(list(map(int, numbers_list)))
    except (ValueError):
        raise ValueError("Must be an int")
