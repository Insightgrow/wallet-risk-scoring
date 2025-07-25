# Wallet Risk Scoring Report

## Objective

The aim of this project is to build a machine learning pipeline that assigns a credit risk score (ranging from 0 to 1000) to a list of wallet addresses that interact with the Compound V2 protocol. These scores are intended to reflect the wallets' creditworthiness based on their historical transaction behavior on-chain.

---

## Data Collection

- **Protocol Used**: Compound V2 (verified via DeFiLlama).
- **Wallets**: A predefined list of 100 wallet addresses was provided.
- **Source APIs**: DeFiLlama and Compound Subgraph APIs were used to extract transaction-level data.
- **Transaction Types Parsed**: `borrow`, `repay`, `deposit`, and `redeem`.
- **Data Format**: Raw transaction data was stored as structured JSON in the `data/` folder.

---

## Feature Engineering

The following features were extracted for each wallet to quantify its on-chain behavior:

| Feature | Description |
|--------|-------------|
| `total_tx` | Total number of Compound-related transactions |
| `total_borrow` | Total value borrowed |
| `total_repay` | Total value repaid |
| `total_deposit` | Total value deposited (supplied) |
| `unique_tokens` | Number of unique tokens interacted with |
| `avg_tx_amount` | Average amount per transaction |
| `last_tx_days_ago` | Days since last Compound activity (recency metric) |

These features were stored in a structured CSV file used for model training.

---

## Model Training

- **Model Type**: `RandomForestRegressor` from `scikit-learn`
- **Target Variable**: Synthetic risk scores (range: 0–1000)
- **Train/Test Split**: 80% training, 20% testing
- **Evaluation Metric**: R² score

### Model Performance:

- **R² Score on Test Set**: `0.341`

> Note: Since the risk scores were synthetically generated, a moderate R² has been obtained for this phase. The accuracy is expected to improve when real credit scoring labels are available.

---

## Output

- The final risk scores were saved in: `data/wallet_scores.csv`
- Each row contains:
  - Wallet address
  - Predicted risk score (0–1000)







