import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="VLSI Temperature Sensor", layout="wide")

st.title("🔬 Analog VLSI Temperature Sensor Dashboard")

# Load data
df = pd.read_csv("ptat_output.csv", delim_whitespace=True, comment='*', header=None)
df.columns = ["Index", "Temp_C", "V_PTAT", "V_CTAT", "V_OUT", "Dummy"]

# Range slider
min_temp, max_temp = int(df["Temp_C"].min()), int(df["Temp_C"].max())
temp_range = st.slider("Select Temperature Range (°C)", min_temp, max_temp, (min_temp, max_temp))

filtered_df = df[(df["Temp_C"] >= temp_range[0]) & (df["Temp_C"] <= temp_range[1])]

# Plot
fig, ax = plt.subplots()
ax.plot(filtered_df["Temp_C"], filtered_df["V_PTAT"], label="V_PTAT")
ax.plot(filtered_df["Temp_C"], filtered_df["V_CTAT"], label="V_CTAT")
ax.plot(filtered_df["Temp_C"], filtered_df["V_OUT"], label="V_OUT")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Voltage (V)")
ax.set_title("PTAT vs CTAT vs Output")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Data preview
st.subheader("Raw Output Data")
st.dataframe(filtered_df)