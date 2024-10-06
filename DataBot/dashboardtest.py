import streamlit as st
import pandas as pd
import io
from workflow import Writer
from data_sample import data
import pickle as pkl
from IPython.display import display
import folium
from folium.plugins import HeatMap
from folium import Map, TileLayer
from streamlit_folium import st_folium

map_df = pkl.load(open('merged_data.pkl', 'rb'))
def generate_map(map_df, country, year = 2020, threshold = 0, criterion = 'IS NBE (TgCO2)'):
    # Filter the data for the selected country
    merged_data = map_df[map_df['Alpha 3 Code'] == country]
    # Create a base world map
    world_map = folium.Map(
        location=[merged_data['Latitude (average)'].mean(), merged_data['Longitude (average)'].mean()],
        zoom_start=6
    )
    
    # Prepare data for the heatmap
    heat_data = [[row['Latitude (average)'], row['Longitude (average)'], row[criterion]] for index, row in merged_data.iterrows()]

    # Add the heatmap layer
    HeatMap(heat_data).add_to(world_map)
    
    # Add markers for each country
    for _, row in merged_data.iterrows():
        folium.Marker(
            location=[row['Latitude (average)'], row['Longitude (average)']],
            popup=f"{row['Alpha 3 Code']}: {row['IS NBE (TgCO2)']} TgCO2",
            icon=folium.Icon(color='blue' if row['IS NBE (TgCO2)'] < threshold else 'red')
        ).add_to(world_map)

    return world_map


# Custom CSS for space-themed design
space_theme_css = """
<style>
body {
    background-color: #0d0d0d;
    color: #ffffff;
    font-family: 'Courier New', Courier, monospace;
}

h1, h2, h3, h4, h5, h6 {
    color: #4B0082;
}

.sidebar .sidebar-content {
    background-color: #1a1a1a;
}

.stButton>button {
    background-color: #000000; /* Sky blue */
    color: #4682B4; /* Purple text */
    border: 2px solid #00008B; /* Dark blue outline */
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.stButton>button:hover {
    background-color: #4682B4; /* Steel blue */
}

.stDataFrame {
    background-color: #1a1a1a;
    color: #ffffff;
}

.stMarkdown {
    background-color: #1a1a1a;
    color: #ffffff;
    padding: 10px;
    border-radius: 5px;
}
#map {
    height: 500px; /* Set the height of the map container */
}
</style>
"""

# Inject the custom CSS
st.markdown(space_theme_css, unsafe_allow_html=True)

# Load the data
data_io = io.StringIO(data)
data = pd.read_csv(data_io)

# Set up the Streamlit app
st.title("Carbon Stock Loss Data Dashboard")
st.write("This dashboard displays CO2 loss data for different countries over several years.")

# Allow users to select a country
countries = data['Alpha 3 Code'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries)

# Call the function to generate the map and display it in the Streamlit app
st.subheader(f"Latest Carbon Stock Loss Heatmap for {map_df[map_df['Alpha 3 Code'] == selected_country]['Country'].values[0]}")
st_folium(generate_map(map_df, selected_country), height=500)

# Filter the data based on the selected country
country_data = data[data['Alpha 3 Code'] == selected_country]

# Prepare the initial state for the writer
if not country_data.empty:
    preprocessed_data = country_data.to_string()
else:
    preprocessed_data = "No data available for the specified country."

# Convert the string data into a DataFrame
data_io = io.StringIO(preprocessed_data)
df = pd.read_csv(data_io)

# Show the data in a table
st.subheader("Data Table")
st.dataframe(df)

initial_state = {
    'messages': [{'role': "user", "content": preprocessed_data}],
    'revision_times': 0
}
writer = Writer()
# Invoke the writer's graph to process the selected country data
if st.button("Generate Summary"):
    output = writer.graph.invoke(initial_state, {'configurable': {'thread_id': 1, 'checkpoint_ns': 0, 'checkpoint_id': 0}})
    st.sidebar.subheader("Generated Summary")
    st.sidebar.write(output['messages'][1:])

# Display country data
st.subheader(f"Anthropogenic Carbon Stock Loss Data for {selected_country}")
st.line_chart(country_data[['Year', 'IS dC_loss (TgCO2)', 'IS NBE (TgCO2)',
    'IS NCE (TgCO2)',
    'Rivers (TgCO2)', 'Wood+Crop (TgCO2)', 'FF (TgCO2)'
]].set_index('Year'))

# Show additional statistics if needed
st.subheader("Summary Statistics")
st.write(country_data.describe())