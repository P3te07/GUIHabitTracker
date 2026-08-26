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

data = load_data()



