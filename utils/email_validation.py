import re


def isGmailValid(gmail):
    """
    It returns True if the gmail parameter is a valid gmail address, and False otherwise

    :param gmail: The gmail address to check
    :return: A boolean value
    """
    return re.search("^.*@gmail.com$", gmail)


def isEmailValid(email):
    """
    It returns true if the email address contains at least one letter or number, followed by an @ symbol, followed by at
    least one letter or number, followed by a period, followed by at least one letter or number

    :param email: The email address to be validated
    :return: A boolean value.
    """
    return re.search("([a-zA-Z]|[0-9])*@.([a-zA-Z]|[0-9])*\.([a-zA-Z]|[0-9])*", email)


def isEmailListValid(emails):
    """
    If the length of the list is 1, then check if the email is valid. If the length of the list is greater than 1, then
    check if each email in the list is valid

    :param emails: a list of emails
    :return: A boolean value
    """
    if len(emails) == 1:
        return isEmailValid(emails)
    else:
        for email in emails:
            if isEmailValid(email):
                continue
            else:
                return False
        return True