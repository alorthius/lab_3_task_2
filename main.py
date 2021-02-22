"""
"""
import json


def read_file(path: str) -> dict:
    if not isinstance(path, str):
        return None

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def ask_user(obj) -> str:

    if isinstance(obj, dict):
        dict_keys = list(obj.keys())

        if len(dict_keys) == 1:
            return ask_user(obj[dict_keys[0]])

        users_input = str(input(f'\nChoose the dictionary key:\n{dict_keys}\n'))
        if users_input not in dict_keys:
            return f'Incorrect key. Try again.\n'

        return ask_user(obj[users_input])

    elif isinstance(obj, list):

        indexes = [num for num in range(len(obj))]
        if len(indexes) > 1:
            users_input = int(input(f'\nChoose the index of the list element:\n{indexes}\n'))

            if users_input not in indexes:
                return f'Incorrect key. Try again.\n'

            return ask_user(obj[users_input])

        elif len(indexes) == 1:
            return ask_user(obj[0])
        else:
            return f'\nThe searched value is:\n{obj}\n'

    else:
        return f'\nThe searched value is:\n{obj}\n'
    

def main_func(path: str):
    data = read_file(path)
    print(ask_user(data))
