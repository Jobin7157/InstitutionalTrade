import pandas as pd
from datetime import datetime

def get_bulk_block_deals():
    # Simulated sample data
    data = {
        "Date": [datetime.today().strftime('%Y-%m-%d')] * 3,
        "Stock": ["HDFC Bank", "Infosys", "Maruti Suzuki"],
        "Type": ["Bulk Deal", "Block Deal", "Bulk Deal"],
        "Buyer": ["XYZ Mutual Fund", "ABC FI", "LMN DII"],
        "Seller": ["Retail Investor", "Other FI", "HNIs"],
        "Quantity": [250000, 500000, 300000],
        "Price (₹)": [1550, 1380, 9750],
        "Sector": ["Finance", "IT", "Auto"]
    }
    df = pd.DataFrame(data)
    return df
