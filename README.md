# Retail Inventory Optimization

This project implements a multi-agent system to optimize retail inventory management. The system uses demand forecasting, inventory monitoring, and pricing optimization to ensure product availability, reduce holding costs, and improve supply chain efficiency.

## Project Structure

```
retail_inventory/
├── data/
│   ├── demand_forecasting.csv
│   ├── inventory_monitoring.csv
│   ├── pricing_optimization.csv
├── src/
│   ├── __init__.py
│   ├── demand_forecasting.py
│   ├── inventory_monitoring.py
│   ├── pricing_optimization.py
│   ├── database.py
│   ├── main.py
├── README.md
```

## Components

### 1. Demand Forecasting
- Predicts future demand for products using historical data.
- Input: `data/demand_forecasting.csv`

### 2. Inventory Monitoring
- Tracks stock levels and triggers reorders.
- Input: `data/inventory_monitoring.csv`

### 3. Pricing Optimization
- Adjusts prices dynamically based on elasticity and competitor prices.
- Input: `data/pricing_optimization.csv`

### 4. Database
- SQLite database to store and manage inventory data.

### 5. Main Script
- Orchestrates the multi-agent system and integrates all components.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```bash
   python src/main.py
   ```

## Future Enhancements
- Add supplier coordination and customer interaction agents.
- Integrate Ollama embeddings for advanced analytics.