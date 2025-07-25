import pandas as pd
import joblib


df = pd.read_csv("data/wallet_features.csv")
wallets = df["wallet"]


model = joblib.load("model/risk_model.pkl")
scaler = joblib.load("model/scaler.pkl")


features = [
    "total_tx",
    "total_borrow",
    "total_repay",
    "total_deposit",
    "unique_tokens",
    "avg_tx_amount",
    "last_tx_days_ago"
]


X_scaled = scaler.transform(df[features])


predictions = model.predict(X_scaled).clip(0, 1000)


output = pd.DataFrame({
    "wallet": wallets,
    "risk_score": predictions.round(2)
})


output.to_csv("data/wallet_scores.csv", index=False)
print("Risk scores saved to data/wallet_scores.csv")
