import requests
import pandas as pd
from datetime import datetime

def get_fii_dii_activity():
    # Simulate data for now, as NSE may block automated requests
    data = {
        "Date": [datetime.today().strftime('%Y-%m-%d')],
        "FII Buy (₹ Cr)": [1450],
        "FII Sell (₹ Cr)": [1290],
        "FII Net (₹ Cr)": [160],
        "DII Buy (₹ Cr)": [1100],
        "DII Sell (₹ Cr)": [1150],
        "DII Net (₹ Cr)": [-50]
    }
    df = pd.DataFrame(data)
    return df
