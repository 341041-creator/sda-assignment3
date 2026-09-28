# MongoDB Atlas Dashboard Configuration

## Data Source
Database: sda_course  
Collection: live_trades  
Dashboard Tool: MongoDB Atlas Charts

## Chart 1: BTC Price Over Time
- Chart Type: Discrete Line
- X-Axis: timestamp
- Y-Axis: price
- Aggregation: Mean
- Purpose: Monitor BTC/USDT price movements over time.

## Chart 2: BUY vs SELL Trade Value
- Chart Type: Grouped Column
- X-Axis: side
- Y-Axis: trade_value_usd
- Aggregation: Sum
- Purpose: Compare the total USD value of BUY and SELL trades.

## Chart 3: Large Trades Over Time
- Chart Type: Scatter
- X-Axis: timestamp
- Y-Axis: trade_value_usd
- Filter: trade_value_usd > 100000
- Purpose: Identify high-value BTC transactions.

## Chart 4: Total Trade Value (USD)
- Chart Type: Number
- Field: trade_value_usd
- Aggregation: Sum
- Purpose: Display the total USD value of trades processed.

## Chart 5: Average Trade Value (USD)
- Chart Type: Number
- Field: trade_value_usd
- Aggregation: Mean
- Purpose: Displays the average USD value per BTC trade.

## Chart 6: Large Trade Count
- Chart Type: Number
- Field: trade_value_usd
- Filter: trade_value_usd >= 100000
- Purpose: Shows the number of high-value BTC trades.

## Chart 7: BUY vs SELL Trade Value Over Time
- Chart Type: Discrete Line
- X-Axis: timestamp
- Y-Axis: trade_value_usd
- Aggregation: Sum
- Series: side (BUY/SELL)
- Purpose: Compares BUY and SELL trading activity over time.
