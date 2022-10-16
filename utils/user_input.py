from other_methods import clear


def getIntInput(message, minValue=1, maxValue=25555):
    """
    It takes a message, a minimum value, and a maximum value as input, and returns an integer that is between the minimum
    and maximum values

    :param message: The message to display to the user
    :param minValue: The minimum value the user can input, defaults to 1 (optional)
    :param maxValue: The maximum value the user can input, defaults to 25555 (optional)
    :return: The user input is being returned.
    """
    while True:
        user_input = int(input(message))
        if minValue <= user_input <= maxValue:
            return user_input
        else:
            clear()
            continue