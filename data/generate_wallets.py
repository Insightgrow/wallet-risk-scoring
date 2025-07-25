import random
import json

def generate_wallet_address():
    return "0x" + ''.join(random.choices("0123456789abcdef", k=40))

def generate_wallet_list(n=100):
    wallets = [generate_wallet_address() for _ in range(n)]
    with open("data/sample_wallets.json", "w") as f:
        json.dump(wallets, f, indent=4)
    print(f" Generated {n} wallet addresses and saved to data/sample_wallets.json")

if __name__ == "__main__":
    generate_wallet_list()
