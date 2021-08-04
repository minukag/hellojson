import json

FILE = "hellojson.json"

with open(FILE, "r") as f:
    data = json.load(f)

name = input("Hello World, What's your name: ")

for i in data:
    if i['name'] == name:
        city = i['city']
        print(f"Hello, {name} from {city}")
        break
else:
    city = input("Where are you from: ")
    r = {"name": name, "city": city}
    data.append(r)
    with open(FILE, "w") as f:
        json.dump(data, f)
    print(f"Hello, {name} from {city}")
    
input("Enter any key to exit...")
