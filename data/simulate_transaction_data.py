import random
import json
import time
from datetime import datetime, timedelta


with open("data/sample_wallets.json") as f:
    wallets = json.load(f)


tokens = ["DAI", "USDC", "ETH", "WBTC"]

tx_types = ["borrow", "repay", "deposit"]

simulated_data = {}

for wallet in wallets:
    tx_count = random.randint(10, 50)
    transactions = []
    
    for _ in range(tx_count):
        tx = {
            "tx_type": random.choice(tx_types),
            "amount": round(random.uniform(10, 10000), 2),
            "token": random.choice(tokens),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 180))).strftime('%Y-%m-%d %H:%M:%S')
        }
        transactions.append(tx)
    
    simulated_data[wallet] = transactions

with open("data/simulated_transaction_data.json", "w") as f:
    json.dump(simulated_data, f, indent=4)

print("Simulated transaction data saved to data/simulated_transaction_data.json")
