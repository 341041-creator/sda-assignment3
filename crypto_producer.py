
from confluent_kafka import Producer
import json
import random
import time
from datetime import datetime, timezone


producer = Producer({
    "bootstrap.servers": "localhost:9092"
})


def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed:", err)
    else:
        print(
            f"Successfully sent to {msg.topic()} "
            f"Partition: {msg.partition()}"
        )


def generate_trade():
    price = round(random.uniform(58000, 65000), 2)
    quantity = round(random.uniform(0.05, 3), 4)

    return {
        "event_type": "trade",
        "symbol": "BTCUSDT",
        "price": price,
        "quantity": quantity,
        "trade_value_usd": round(price * quantity, 2),
        "side": random.choice(["BUY", "SELL"]),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def generate_order_book():
    bid_price = round(random.uniform(58000, 65000), 2)
    ask_price = round(bid_price + random.uniform(1, 20), 2)

    return {
        "event_type": "order_book",
        "symbol": "BTCUSDT",
        "best_bid_price": bid_price,
        "best_bid_quantity": round(random.uniform(0.1, 5), 4),
        "best_ask_price": ask_price,
        "best_ask_quantity": round(random.uniform(0.1, 5), 4),
        "spread": round(ask_price - bid_price, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def generate_liquidation():
    price = round(random.uniform(58000, 65000), 2)
    quantity = round(random.uniform(0.1, 4), 4)

    return {
        "event_type": "liquidation",
        "symbol": "BTCUSDT",
        "side": random.choice(["LONG", "SHORT"]),
        "price": price,
        "quantity": quantity,
        "liquidation_value_usd": round(price * quantity, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


print("Crypto Kafka Producer Started")
print("--------------------------------")


try:
    while True:

        trade = generate_trade()
        order_book = generate_order_book()
        liquidation = generate_liquidation()

        producer.produce(
            "btc-live-trades",
            key="BTCUSDT",
            value=json.dumps(trade),
            callback=delivery_report
        )

        producer.produce(
            "btc-order-book",
            key="BTCUSDT",
            value=json.dumps(order_book),
            callback=delivery_report
        )

        producer.produce(
            "btc-liquidations",
            key="BTCUSDT",
            value=json.dumps(liquidation),
            callback=delivery_report
        )

        producer.poll(0)

        print("\nTRADE:")
        print(json.dumps(trade, indent=2))

        print("\nORDER BOOK:")
        print(json.dumps(order_book, indent=2))

        print("\nLIQUIDATION:")
        print(json.dumps(liquidation, indent=2))

        print("--------------------------------")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nProducer stopped.")

finally:
    producer.flush()
    