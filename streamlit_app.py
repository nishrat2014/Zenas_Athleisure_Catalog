# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog 🎈")
st.write("Pick a sweatsuit color or size:")

# Get the current credentials
session = get_active_session()

# Use Snowpark to query and convert to Pandas
df = session.sql("""
    SELECT COLOR_OR_STYLE, PRICE, FILE_URL, SIZE_LIST, UPSELL_PRODUCT_DESC
    FROM zenas_athleisure_db.products.catalog_for_website
""").to_pandas()

# --- Dropdown menu for color selection ---
selected_color = st.selectbox("", df["COLOR_OR_STYLE"].unique())

# --- Filter row based on selection ---
row = df[df["COLOR_OR_STYLE"] == selected_color].iloc[0]

# --- Display jacket image ---
st.image(row["FILE_URL"], caption=f"{selected_color} Jacket", use_container_width=True)

# --- Display description ---
st.markdown(f"**Our warm, comfortable, {row['COLOR_OR_STYLE']} sweatsuit.**")

# --- Display price ---
st.markdown(f"**PRICE:** ${row['PRICE']}")

# --- Sizes available ---
st.markdown(f"**Sizes available:** ${row['SIZE_LIST']}")

# --- Sizes available ---
st.markdown(f"{row['UPSELL_PRODUCT_DESC']}")
