import os
import json
DATABASE_PATH = "db.json"

def add_temperature(timestamp: int, temperature: float, options={}):
    if not os.path.isfile(DATABASE_PATH):
        with open(DATABASE_PATH, "w") as fp:
            fp.write(json.dumps({"temperatures": {}}))

    with open(DATABASE_PATH, "r+") as fp:
        content = json.load(fp)

        content['temperatures'][timestamp] = float(temperature)

        fp.seek(0)
        fp.write(json.dumps(content))

def get_temperatures(options={}):
    with open(DATABASE_PATH, "r") as fp:
        return json.load(fp)
