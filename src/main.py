from src.demand_forecasting import forecast_demand
from src.inventory_monitoring import monitor_inventory
from src.pricing_optimization import optimize_pricing
from src.database import create_connection, create_tables, load_data_from_csv
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

def main():
    # Define database file path
    db_file = "retail_inventory.db"

    # Establish connection to the database
    conn = create_connection(db_file)

    if conn is not None:
        # Create tables
        create_tables(conn)

        # Load data from CSV files
        data_dir = os.path.join(os.path.dirname(__file__), '../data')
        load_data_from_csv(conn, os.path.join(data_dir, 'demand_forecasting.csv'), 'demand_forecasting')
        load_data_from_csv(conn, os.path.join(data_dir, 'inventory_monitoring.csv'), 'inventory_monitoring')
        load_data_from_csv(conn, os.path.join(data_dir, 'pricing_optimization.csv'), 'pricing_optimization')

        # Run modules
        print("Demand Forecasting:")
        print(forecast_demand(os.path.join(data_dir, 'demand_forecasting.csv')))

        # Initialize LangChain LLM
        llm = OpenAI(temperature=0.7)

        # Define a LangChain tool for inventory monitoring
        inventory_tool = Tool(
            name="Inventory Monitoring",
            func=lambda file_path: monitor_inventory(file_path),
            description="Monitors inventory levels and provides insights."
        )

        # Initialize an agent with the tool
        agent = initialize_agent([inventory_tool], llm, agent="zero-shot-react-description", verbose=True)

        # Replace the inventory monitoring section with LangChain agent
        print("\nInventory Monitoring:")
        response = agent.run(os.path.join(data_dir, 'inventory_monitoring.csv'))
        print(response)

        print("\nPricing Optimization:")
        print(optimize_pricing(os.path.join(data_dir, 'pricing_optimization.csv')))

        # Close the connection
        conn.close()
    else:
        print("Error! Cannot establish a database connection.")

if __name__ == "__main__":
    main()