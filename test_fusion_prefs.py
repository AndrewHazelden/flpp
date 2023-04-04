from slpp import slpp
import json

FILE = "fusion_shared.prefs"

with open(str(FILE), "r") as f:
    text = f.read()

data = slpp.decode(text)
print(data)

data["Locked"] = False
with open("fusion_shared_modified.prefs", "w") as out:
    out.write(slpp.encode(data))

with open("fusion_shared_modified.json", "w") as out:
    json.dump(data, out, indent=4, sort_keys=False)