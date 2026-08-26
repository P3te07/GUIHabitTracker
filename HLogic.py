import json
from Data import data


def save_data(data):
    try:
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        result = True
    except TypeError:
        print("Type Error")
        result = False
    except FileNotFoundError:
        print("File Not Found")
        result = False
    except PermissionError:
        print("Permission Error")
        result = False
    return result



