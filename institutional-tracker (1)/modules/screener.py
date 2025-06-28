import pandas as pd

def get_shareholding_changes():
    # Simulated sample data for institutional shareholding changes
    data = {
        "Stock": ["TCS", "Axis Bank", "Sun Pharma"],
        "Sector": ["IT", "Finance", "Pharma"],
        "Q1 Inst. Holding (%)": [35.2, 42.8, 28.6],
        "Q2 Inst. Holding (%)": [37.5, 43.1, 27.9],
        "Change (%)": [2.3, 0.3, -0.7]
    }
    df = pd.DataFrame(data)
    return df
