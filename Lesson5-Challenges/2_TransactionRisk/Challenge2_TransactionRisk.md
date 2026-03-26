# Challenge 2: Transaction Risk Scoring

## Business Problem
A digital payments company processes thousands of transactions every minute. Fraudulent transactions result in financial loss and reduced customer trust.

The company wants to flag potentially fraudulent transactions before they are approved.

---

## Data
Here is an example of given transaction data, including:

- `transaction_amount`: Amount of transaction
- `time`: Time of transaction
- `merchant_category`: Type of merchant
- `user_id`: Unique user identifier
- `location`: Transaction location
- `is_fraud`: Whether the transaction is fraudulent

Use this as a frame of reference when looking through the kaggle dataset.

Name of Dataset: Credit Card Fraud Detection  
KAGGLE CLI DOWNLOAD: kaggle datasets download -d mlg-ulb/creditcardfraud  
Kaggle Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## Tasks
- Analyze differences between fraudulent and non-fraudulent transactions
- Engineer features that may improve fraud detection
- Build a model to predict fraudulent transactions
- Evaluate model performance using appropriate metrics
- Identify the most important factors contributing to fraud