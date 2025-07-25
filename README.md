# Wallet Risk Scoring using Compound Protocol

This project builds a machine learning model to assign **risk scores (0–1000)** to crypto wallets based on their transaction behavior on the **Compound V2** protocol. It has been designed to help estimate the financial reliability and behavior of DeFi users.

---

## Features Used

The following features have been used per wallet from on-chain activity:

| Feature             | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| `wallet`            | Wallet address (Ethereum)                                         |
| `total_tx`          | Total number of transactions (borrow, repay, deposit)             |
| `total_borrow`      | Total number of borrow events                                     |
| `total_repay`       | Total number of repay events                                      |
| `total_deposit`     | Total number of deposit (supply) events                           |
| `unique_tokens`     | Number of unique tokens interacted with                           |
| `avg_tx_amount`     | Average transaction amount across all event types                 |
| `last_tx_days_ago`  | Days since the last transaction (recency score)                   |

> The target `risk_score` was synthetically generated for training purposes.

---

## Data Source

- Compound V2 on-chain data via:
  - **Llama.fi Protocol API** 
  
The wallets were analyzed using historical borrow, repay, supply, and redeem events.

---

## Project Structure
``` 
wallet-risk-score/
│
├── data/                     # Raw and processed data files
│   |── sample_wallets.json
|   |__ wallet_scores.csv     # Output
│
├── features/                 # Feature extraction logic
│   └── extract_features.py
│
├── model/                    # ML model training and scoring
│   ├── train_model.py
│   └── score_wallets.py
│
├── scripts/                  # Utility scripts (e.g., slug finder)
│   └── find_slug.py
│
└── report.md                 # Technical writeup for explanation
```
## Model Details
- Algorithm: Random Forest Regressor
- Evaluation: R² score ≈ 0.34 (on synthetic risk scores)
  
## Future Scope
- Real risk labels from liquidations or credit history
- Time-series analysis of wallet health
- Integration into DeFi credit platforms

