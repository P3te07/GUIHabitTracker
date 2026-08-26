import os
import json
import sys


def load_data():
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                return data
        except json.decoder.JSONDecodeError:
            print("Error decoding the JSON file")
            return []
        except PermissionError:
            print("Permission denied")
            return[]
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return []
    else:
        print("Data file not found")
        return []

def save_data(data):
    try:
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        result = True
    except TypeError:
        print("Type Error")
        result = False
    except PermissionError:
        print("Permission Error")
        result = False
    return result





