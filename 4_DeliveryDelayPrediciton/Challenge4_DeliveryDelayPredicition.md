# Challenge 4: Delivery Delay Prediction

## Business Problem
A logistics company is experiencing inconsistent delivery times, leading to customer dissatisfaction.

They want to predict delivery delays in advance and identify key factors that contribute to late deliveries.

---

## Data
Here is an example of given shipment data, including:

- `distance`: Distance of delivery
- `pickup_time`: Time package was picked up
- `delivery_time`: Time package was delivered
- `weather_condition`: Weather during delivery
- `traffic_index`: Traffic level indicator
- `delay_minutes`: Delay in minutes

Use this as a frame of reference when looking through the kaggle dataset.

Name of Dataset: Brazilian E-Commerce Public Dataset by Olist  
KAGGLE CLI DOWNLOAD: kaggle datasets download -d olistbr/brazilian-ecommerce  
Kaggle Link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Tasks
- Analyze patterns in delivery delays
- Engineer features that may influence delays (e.g., time of day, day of week)
- Build a model to predict delivery delay
- Evaluate how accurately your model predicts delays
- Identify the most important factors contributing to delays