# SDA Assignment 3 – Real-Time BTC Trading Dashboard

## Project Overview
This project demonstrates a real-time BTC/USDT trading data pipeline using Kafka, Python, MongoDB Atlas, and MongoDB Atlas Charts.

## Data Flow
crypto_producer.py → Kafka (btc-live-trades) → mongo_consumer.py → MongoDB Atlas → MongoDB Atlas Charts

## Dashboard Visualizations
1. BTC Price Over Time
2. Large Trades Over Time
3. BUY vs SELL Trade Value
4. Total Trade Value (USD)
5. Average Trade Value (USD)
6. Large Trade Count
7. BUY vs SELL Trade Value Over Time

## Technologies Used
- Python
- Apache Kafka
- MongoDB Atlas
- MongoDB Atlas Charts

## Key Features
- Simulated real-time BTC/USDT trading data
- Kafka-based streaming pipeline
- Automatic storage of processed trades in MongoDB Atlas
- Trade value calculation in USD
- Identification of large trades above $100,000
- BUY vs SELL trading analysis
- Real-time dashboard visualization
