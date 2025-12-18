# Import python packages
import streamlit as st
import snowflake.connector
import pandas as pd


#snowflake connection
conn = snowflake.connector.connect(
  user=st.secrets["snowflake"]["user"],

password=st.secrets["snowflake"]["password"],

account=st.secrets["snowflake"]["account"],

warehouse=st.secrets["snowflake"]["warehouse"],

database=st.secrets["snowflake"]["database"],

schema=st.secrets["snowflake"]["schema"],
)
# Query your view
query = """
    SELECT COLOR_OR_STYLE, PRICE, FILE_URL, SIZE_LIST, UPSELL_PRODUCT_DESC
    FROM zenas_athleisure_db.products.catalog_for_website
"""
df = pd.read_sql(query, conn)




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
