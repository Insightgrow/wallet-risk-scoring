import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np
import os


df = pd.read_csv("data/wallet_features.csv")


np.random.seed(42)
df["risk_score"] = (
    0.25 * df["total_borrow"]
    - 0.2 * df["total_repay"]
    + 0.3 * df["last_tx_days_ago"]
    + 0.15 * df["total_tx"]
    + np.random.normal(0, 50, len(df))
)
df["risk_score"] = df["risk_score"].clip(0, 1000)  


df.to_csv("data/wallet_features_with_risk.csv", index=False)


features = [
    "total_tx",
    "total_borrow",
    "total_repay",
    "total_deposit",
    "unique_tokens",
    "avg_tx_amount",
    "last_tx_days_ago"
]

X = df[features]
y = df["risk_score"]


scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


print(f"Model trained! R² on test set: {model.score(X_test, y_test):.3f}")


os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/risk_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
