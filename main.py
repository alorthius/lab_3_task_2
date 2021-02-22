"""
GitHub link: https://github.com/alorthius/lab_3_task_2
"""
import json


def read_file(path: str) -> dict:
    """
    Read json file by its path. Return it as a dictionary.
    Return None if the path argument is not a string.
    If the file is not found by its path, message the user:
    'Invalid path. Try again'.

    >>> read_file(['friends_list_AdamMGrant.json'])

    >>> read_file('Incorrect path')
    <BLANKLINE>
    Invalid path. Try again.
    """
    if not isinstance(path, str):
        return None

    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    except FileNotFoundError:
        print('\nInvalid path. Try again.')
        return None


def ask_user(obj) -> str:
    """
    Recursive function to search for keys and values in the
    dictionary step by step, and let the user pick one. If
    there is a list, the user will be given to choose its
    elements' indexes. Works only with nested lists and
    dictionaries.
    """
    if isinstance(obj, dict):
        dict_keys = list(obj.keys())

        if len(dict_keys) == 1:  # there is no need to ask user
            return ask_user(obj[dict_keys[0]])

        users_input = str(
            input(f'\nChoose the dictionary key:\n{dict_keys}\n'))
        if users_input not in dict_keys:
            return 'Incorrect key. Try again.\n'

        return ask_user(obj[users_input])

    elif isinstance(obj, list):

        indexes = [num for num in range(len(obj))]
        if len(indexes) > 1:
            users_input = int(input(
                f'\nChoose the index of the list element:\n{indexes}\n'))

            if users_input not in indexes:
                return f'Incorrect key. Try again.\n'

            return ask_user(obj[users_input])

        elif len(indexes) == 1:  # there is no need to ask user
            return ask_user(obj[0])
        else:  # empty list
            return f'\nThe searched value is:\n{obj}\n'

    else:
        return f'\nThe searched value is:\n{obj}\n'


def main_func(path: str):
    """
    Find and print the value of the user's key in the json object.
    Return None if the path argument is not a string.

    >>> main_func(['friends_list_AdamMGrant.json'])
    """
    if not isinstance(path, str):
        return None
    data = read_file(path)
    print(ask_user(data))
