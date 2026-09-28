from confluent_kafka import Consumer
from pymongo import MongoClient
import json
from datetime import datetime

# -----------------------------
# MongoDB Atlas Connection
# -----------------------------
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.pfnsqf3.mongodb.net/?appName=Cluster0"

mongo_client = MongoClient(MONGO_URI)

db = mongo_client["sda_course"]
collection = db["live_trades"]

# Test MongoDB connection
mongo_client.admin.command("ping")
print("Connected to MongoDB Atlas successfully!")

# -----------------------------
# Kafka Consumer Configuration
# -----------------------------

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "assignment3-mongodb-consumer",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["btc-live-trades"])

print("Listening to btc-live-trades...")
print("Press Ctrl+C to stop.")

# -----------------------------
# Consume Kafka Messages
# -----------------------------

try:
    while True:

        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print("Kafka error:", msg.error())
            continue

        trade = json.loads(msg.value().decode("utf-8"))

        # Convert timestamp string to MongoDB Date
        if "timestamp" in trade:
            trade["timestamp"] = datetime.fromisoformat(
                trade["timestamp"].replace("Z", "+00:00")
            )

        collection.insert_one(trade)

        print("Inserted into MongoDB:", trade)

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()
    mongo_client.close()