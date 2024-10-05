import streamlit as st
import pandas as pd
import io
from DataBot.data_sample import data
# Load the data, imported from sample file

# Convert the string data into a DataFrame
data_io = io.StringIO(data)
df = pd.read_csv(data_io)

# Set up the Streamlit app
st.title("CO2 Loss Data Dashboard")
st.write("This dashboard displays CO2 loss data for different countries over several years.")

# Show the data in a table
st.subheader("Data Table")
st.dataframe(df)

# Allow users to select a country
countries = df['Alpha 3 Code'].unique()
selected_country = st.selectbox("Select a Country", countries)

# Filter the data based on the selected country
country_data = df[df['Alpha 3 Code'] == selected_country]

# Display country data
st.subheader(f"Data for {selected_country}")
st.line_chart(country_data[['Year', 'IS dC_loss (TgCO2)', 'LNLG dC_loss (TgCO2)']].set_index('Year'))

# Show additional statistics if needed
st.subheader("Summary Statistics")
st.write(country_data.describe())


##Session state
#if 'counter' not in st.session_state:
#    st.session_state.counter = 0

##test button 
##PRESSED TO GENERATE SUMMARY FROM LLMs
#if st.button("Increment"):
#    st.session_state.counter += 1

#st.write(f"Counter: {st.session_state.counter}")
