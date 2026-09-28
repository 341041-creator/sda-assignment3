# SDA Assignment 3 – Real-Time BTC Trading Dashboard

## Project Overview
This project demonstrates a real-time streaming data pipeline for BTC/USDT trading data using Apache Kafka, Python, MongoDB Atlas, and MongoDB Atlas Charts.

## Data Flow
crypto_producer.py → Kafka (btc-live-trades) → mongo_consumer.py → MongoDB Atlas → MongoDB Atlas Charts

## Components

### 1. Kafka Producer
`crypto_producer.py` generates simulated BTC/USDT trading events and publishes them to the Kafka topic `btc-live-trades`.

### 2. Kafka Consumer
`mongo_consumer.py` subscribes to the `btc-live-trades` topic, consumes the messages, and stores them in MongoDB Atlas.

Database: `sda_course`  
Collection: `live_trades`

### 3. Dashboard
The dashboard was created using MongoDB Atlas Charts.

It contains:
- BTC Price Over Time
- BUY vs SELL Trade Value
- Large Trades Over Time
- Total Trade Value (USD)

## Technologies Used
- Python
- Apache Kafka
- Docker
- MongoDB Atlas
- MongoDB Atlas Charts

## Business Use
The dashboard helps monitor BTC price movements, compare BUY and SELL activity, identify large-value trades, and track overall trading value.
