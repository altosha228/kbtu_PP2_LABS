import json

with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print(f"{'DN':<45} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    desc = attributes.get("pathSDescr", "N/A")  # Если нет описания, ставим "N/A"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<45} {desc:<20} {speed:<10} {mtu:<5}")
