import Data
import uuid
import datetime

def add_habit(name, current_habits):
        id_habit = str(uuid.uuid4())
        creation_date = str(datetime.date.today())
        completed_dates = []
        if name.strip == "":
            return "No name given"
        input_values = {
            "id": id_habit,
            "name": name,
            "creation_date": creation_date,
            "completed_dates": completed_dates
        }
        current_habits.append(input_values)
        result = Data.save_data(current_habits)
        if result:
            return True
        else:
            return False


