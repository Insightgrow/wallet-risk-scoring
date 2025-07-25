import json
import pandas as pd
from datetime import datetime


with open("data/simulated_transaction_data.json") as f:
    tx_data = json.load(f)

rows = []

for wallet, tx_list in tx_data.items():
    features = {
        "wallet": wallet,
        "total_tx": len(tx_list),
        "total_borrow": 0,
        "total_repay": 0,
        "total_deposit": 0,
        "unique_tokens": len(set(tx["token"] for tx in tx_list)),
        "avg_tx_amount": 0,
        "last_tx_days_ago": 0,
    }

    total_amount = 0
    latest_ts = None

    for tx in tx_list:
        amount = tx["amount"]
        tx_type = tx["tx_type"]
        timestamp = datetime.strptime(tx["timestamp"], "%Y-%m-%d %H:%M:%S")
        total_amount += amount

        if tx_type == "borrow":
            features["total_borrow"] += amount
        elif tx_type == "repay":
            features["total_repay"] += amount
        elif tx_type == "deposit":
            features["total_deposit"] += amount

        if latest_ts is None or timestamp > latest_ts:
            latest_ts = timestamp

    features["avg_tx_amount"] = round(total_amount / features["total_tx"], 2)

    if latest_ts:
        features["last_tx_days_ago"] = (datetime.now() - latest_ts).days

    rows.append(features)


df = pd.DataFrame(rows)
df.to_csv("data/wallet_features.csv", index=False)
print("Features saved to data/wallet_features.csv")
