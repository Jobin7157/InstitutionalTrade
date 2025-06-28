import os
os.environ["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"

import streamlit as st
import pandas as pd
from modules.nse import get_fii_dii_activity
from modules.bulk_block import get_bulk_block_deals
from modules.screener import get_shareholding_changes

st.set_page_config(page_title="Institutional Tracker", layout="wide")
st.title("📊 Institutional Investor Tracker")

st.sidebar.header("Filters")
selected_sector = st.sidebar.selectbox("Select Sector", ["All", "IT", "Finance", "Pharma", "Auto"])

st.header("1. FII/DII Activity Overview")
fii_dii_df = get_fii_dii_activity()
st.dataframe(fii_dii_df, use_container_width=True)

st.header("2. Bulk/Block Deals")
bulk_block_df = get_bulk_block_deals()
if selected_sector != "All":
    bulk_block_df = bulk_block_df[bulk_block_df['Sector'] == selected_sector]
st.dataframe(bulk_block_df, use_container_width=True)

st.header("3. Shareholding Pattern Changes")
shareholding_df = get_shareholding_changes()
if selected_sector != "All":
    shareholding_df = shareholding_df[shareholding_df['Sector'] == selected_sector]
st.dataframe(shareholding_df, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Data: NSE, Screener.in")
