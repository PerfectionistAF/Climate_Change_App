import streamlit as st
import pandas as pd
import io
from workflow import Writer

# Load the data
# data = """Alpha 3 Code,Year,IS dC_loss (TgCO2),IS dC_loss unc (TgCO2),LNLG dC_loss (TgCO2),LNLG dC_loss unc (TgCO2),LNLGIS dC_loss (TgCO2),LNLGIS dC_loss unc (TgCO2),LNLGOGIS dC_loss (TgCO2),LNLGOGIS dC_loss unc (TgCO2),IS NBE (TgCO2),IS NBE unc (TgCO2),LNLG NBE (TgCO2),LNLG NBE unc (TgCO2),LNLGIS NBE (TgCO2),LNLGIS NBE unc (TgCO2),LNLGOGIS NBE (TgCO2),LNLGOGIS NBE unc (TgCO2),IS NCE (TgCO2),IS NCE unc (TgCO2),LNLG NCE (TgCO2),LNLG NCE unc (TgCO2),LNLGIS NCE (TgCO2),LNLGIS NCE unc (TgCO2),LNLGOGIS NCE (TgCO2),LNLGOGIS NCE unc (TgCO2),Rivers (TgCO2),River unc (TgCO2),Wood+Crop (TgCO2),Wood+Crop unc (TgCO2),FF (TgCO2),FF unc (TgCO2),Z-statistic,FUR IS,FUR LNLG,FUR LNLGIS,FUR LNLGOGIS
# AFG,2015,1.20E+00,4.19E+01,5.46E+01,1.80E+02,3.93E+01,1.54E+02,-9.77E-01,1.12E+02,2.82E+00,4.19E+01,5.63E+01,1.80E+02,4.10E+01,1.54E+02,6.47E-01,1.12E+02,2.22E+01,4.19E+01,7.56E+01,1.80E+02,6.04E+01,1.54E+02,2.00E+01,1.12E+02,-2.43E+00,1.70E+00,4.06E+00,1.22E+00,1.94E+01,7.98E-01,0.37,0.01,0.2,0.19,0.03
# AFG,2016,-1.27E+00,3.24E+01,6.76E+01,2.34E+02,5.06E+01,1.75E+02,1.77E+01,1.18E+02,6.28E-01,3.24E+01,6.94E+01,2.34E+02,5.25E+01,1.75E+02,1.96E+01,1.18E+02,2.11E+01,3.24E+01,9.00E+01,2.34E+02,7.30E+01,1.75E+02,4.01E+01,1.18E+02,-2.16E+00,2.24E+00,4.06E+00,1.22E+00,2.05E+01,6.78E-01,0.31,0.01,0.2,0.19,0.03
# AFG,2017,-7.33E-02,4.34E+01,7.71E+01,2.33E+02,5.45E+01,1.80E+02,1.03E+01,1.28E+02,1.89E+00,4.34E+01,7.91E+01,2.33E+02,5.65E+01,1.80E+02,1.23E+01,1.28E+02,2.30E+01,4.34E+01,1.00E+02,2.33E+02,7.75E+01,1.80E+02,3.33E+01,1.28E+02,-2.09E+00,2.38E+00,4.06E+00,1.22E+00,2.11E+01,6.96E-01,0.47,0.01,0.2,0.19,0.03
# AFG,2018,-9.31E-02,4.06E+01,1.32E+02,3.20E+02,1.16E+02,2.43E+02,4.42E+01,1.83E+02,1.94E+00,4.06E+01,1.34E+02,3.20E+02,1.18E+02,2.43E+02,4.63E+01,1.83E+02,2.74E+01,4.06E+01,1.59E+02,3.20E+02,1.44E+02,2.43E+02,7.18E+01,1.83E+02,-2.02E+00,2.52E+00,4.06E+00,1.22E+00,2.55E+01,6.96E-01,0.39,0.01,0.2,0.19,0.03
# AFG,2019,-8.35E+00,4.10E+01,9.13E+01,2.41E+02,6.40E+01,1.82E+02,1.31E+01,1.21E+02,-6.32E+00,4.10E+01,9.33E+01,2.41E+02,6.60E+01,1.82E+02,1.51E+01,1.21E+02,2.15E+01,4.10E+01,1.21E+02,2.41E+02,9.39E+01,1.82E+02,4.29E+01,1.21E+02,-2.03E+00,2.50E+00,4.06E+00,1.22E+00,2.79E+01,7.98E-01,0.49,0.01,0.2,0.19,0.03
# AFG,2020,3.16E+00,3.43E+01,1.04E+02,2.02E+02,8.61E+01,1.97E+02,1.47E+01,1.09E+02,5.06E+00,3.43E+01,1.06E+02,2.02E+02,8.80E+01,1.97E+02,1.66E+01,1.09E+02,3.08E+01,3.43E+01,1.31E+02,2.02E+02,1.14E+02,1.97E+02,4.23E+01,1.09E+02,-2.15E+00,2.27E+00,4.06E+00,1.22E+00,2.57E+01,7.98E-01,0.5,0.01,0.2,0.19,0.03
# AFG,mean,-2.99E-01,3.46E+01,9.05E+01,2.41E+02,6.85E+01,1.98E+02,1.29E+01,1.35E+02,1.61E+00,3.45E+01,9.25E+01,2.41E+02,7.04E+01,1.98E+02,1.48E+01,1.35E+02,2.49E+01,3.45E+01,1.16E+02,2.41E+02,9.37E+01,1.98E+02,3.82E+01,1.35E+02,-2.15E+00,2.27E+00,4.06E+00,1.22E+00,2.33E+01,7.44E-01,0.4,0.01,0.2,0.19,0.03
# """

#############################################################################

# Load the data
file_path = "../Data/pilot_topdown_CO2_Budget_countries_v1.csv"
data = pd.read_csv(file_path)


#############################################################################

# Set up the Streamlit app
st.title("CO2 Loss Data Dashboard")
st.write("This dashboard displays CO2 loss data for different countries over several years.")

# Allow users to select a country
countries = data['Alpha 3 Code'].unique()
selected_country = st.selectbox("Select a Country", countries)

# Filter the data based on the selected country
target_country_code = 'AFG'
country_data = data[data['Alpha 3 Code'] == selected_country]

# Prepare the initial state for the writer
if not country_data.empty:
    preprocessed_data = country_data.to_string()
else:
    preprocessed_data = "No data available for the specified country."

#############################################################################

# Convert the string data into a DataFrame
data_io = io.StringIO(preprocessed_data)
df = pd.read_csv(data_io)

# Show the data in a table
st.subheader("Data Table")
st.dataframe(df)

#############################################################################

initial_state = {
    'messages': [{'role': "user", "content": preprocessed_data}],
    'revision_times': 0
}
writer = Writer()
# Invoke the writer's graph to process the selected country data
if st.button("Generate Summary"):
    output = writer.graph.invoke(initial_state, {'configurable': {'thread_id': 1, 'checkpoint_ns': 0, 'checkpoint_id': 0}})
    st.subheader("Generated Summary")
    st.write(output['messages'])

#############################################################################

# Display country data
st.subheader(f"Data for {selected_country}")
st.line_chart(country_data[['Year', 'IS dC_loss (TgCO2)', 'LNLG dC_loss (TgCO2)']].set_index('Year'))

# Show additional statistics if needed
st.subheader("Summary Statistics")
st.write(country_data.describe())


##Session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

##test button 
##PRESSED TO GENERATE SUMMARY FROM LLMs
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
