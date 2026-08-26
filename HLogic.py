import Data
import random
import datetime
from main import loader

def add_habit():
    id = random.choices(
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], k=7)
    try:
        id_habit = ''.join(id)
        name = ''
        creation_date = str(datetime.date.today())
        completed_dates = []

        Input = {
            "id": id_habit,
            "name": name,
            "creation_date": creation_date,
            "completed_dates": completed_dates
        }

        Data.save_data(Input)
    except:
        print("error")


