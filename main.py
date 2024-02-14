from pathlib import Path
import json

def load_json(filepath: Path | str):
    with open(filepath, "r") as file:
        return json.load(file)
    
def read_txt(filepath: Path | str):
    with open(filepath, "r") as file:
        return [row.strip() for row in file]
    
def call_json(result: list | dict, filepath: Path | str):
    with open(f"{filepath}.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

WALLETS = [address.lower() for address in read_txt("wallets.txt")]

files = [
    "starknet-0.json",
    "starknet-1.json",
    "starknet-2.json",
    "starknet-3.json",
    "starknet-4.json",
    "starknet-5.json",
    "starknet-6.json",
]

eligble_wallets = []
total = 0
for name_file in files:
    _file = load_json(name_file)
    for data in _file["eligibles"]:
        address = data["identity"].lower()
        amount = float(data["amount"])

        if address in WALLETS:
            total += amount
            eligble_wallets.append(address)
            print(f'{address} : {amount}')

print(f'\nCONGRATULATIONS! YOUR $STRK DROP : {int(total)}\n')
print(f'{len(eligble_wallets)} eligble wallets\n')
call_json(eligble_wallets, "eligble_wallets")
