import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt
import numpy as np
import pickle as pkl
import folium
import folium.plugins
from folium import Map, TileLayer


# Load data
data = """
Entity,Year,Access to electricity (% of population),Access to clean fuels for cooking,Renewable-electricity-generating-capacity-per-capita,Electricity from fossil fuels (TWh),Electricity from nuclear (TWh),Electricity from renewables (TWh),Low-carbon electricity (% electricity),Latitude,Longitude
Afghanistan,2000,1.613591,6.2,9.22,0.16,0,0.31,65.95744,33.93911,67.709953
Afghanistan,2001,4.074574,7.2,8.86,0.09,0,0.5,84.745766,33.93911,67.709953
Afghanistan,2002,9.409158,8.2,8.47,0.13,0,0.56,81.159424,33.93911,67.709953
Afghanistan,2003,14.738506,9.5,8.09,0.31,0,0.63,67.02128,33.93911,67.709953
Afghanistan,2004,20.064968,10.9,7.75,0.33,0,0.56,62.92135,33.93911,67.709953
Afghanistan,2005,25.390894,12.2,7.51,0.34,0,0.59,63.440857,33.93911,67.709953
Albania,2000,100,38.2,0,0.14,0,4.55,97.01493,41.153332,20.168331
Albania,2001,100,40.5,0,0.13,0,3.52,96.438354,41.153332,20.168331
Albania,2002,100,43.2,0,0.16,0,3.48,95.60439,41.153332,20.168331
Albania,2003,100,46.4,0,0.1,0,5.12,98.0843,41.153332,20.168331
Albania,2004,100,49,0,0.13,0,5.41,97.65343,41.153332,20.168331
Albania,2005,100,51.9,0,0.07,0,5.32,98.7013,41.153332,20.168331
Algeria,2000,98.9731,97.1,8.91,23.84,0,0.05,0.20929259,28.033886,1.659626
Algeria,2001,98.96687,97.3,8.79,24.96,0,0.07,0.2796644,28.033886,1.659626
Algeria,2002,98.95306,97.8,8.68,25.94,0,0.06,0.23076923,28.033886,1.659626
Algeria,2003,98.93401,98,8.57,27.54,0,0.26,0.93525183,28.033886,1.659626
Algeria,2004,98.91208,98.2,8.46,29.14,0,0.25,0.8506295,28.033886,1.659626
Algeria,2005,98.88961,98.5,8.34,31.36,0,0.55,1.7235976,28.033886,1.659626
Angola,2000,24.212744,41.1,14.37,0.5,0,0.9,64.28571,-11.202692,17.873887
Angola,2001,20,41.7,13.9,0.58,0,1.01,63.52201,-11.202692,17.873887
Angola,2002,26.352118,41.7,13.46,0.58,0,1.13,66.08187,-11.202692,17.873887
Angola,2003,27.412777,42,13.01,0.71,0,1.23,63.40206,-11.202692,17.873887
Angola,2004,28.47055,41.9,26.44,0.45,0,1.73,79.357796,-11.202692,17.873887
Angola,2005,29.527786,42.6,25.53,0.53,0,2.2,80.58608,-11.202692,17.873887
Antigua and Barbuda,2000,97.68926,100,0,0.14,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2001,97.785255,100,0,0.16,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2002,100,100,0,0.18,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2003,97.956825,100,0,0.2,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2004,98.0371,100,0,0.21,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2005,92.2,100,0,0.23,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2006,100,100,0,0.24,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2007,100,100,0,0.26,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2008,100,100,0,0.27,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2009,98.48128,100,1.15,0.31,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2010,98.59724,100,1.14,0.32,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2011,94.55202,100,3.36,0.32,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2012,100,100,3.32,0.31,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2013,100,100,4.37,0.31,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2014,100,100,4.32,0.32,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2015,100,100,36.34,0.32,0,0.01,3.030303,17.060816,-61.796428
Antigua and Barbuda,2016,100,100,37.03,0.32,0,0,0,17.060816,-61.796428
Antigua and Barbuda,2017,100,100,40.87,0.32,0,0.01,3.030303,17.060816,-61.796428
Antigua and Barbuda,2018,100,100,86.21,0.32,0,0.01,3.030303,17.060816,-61.796428
Antigua and Barbuda,2019,100,100,85.47,0.33,0,0.01,2.9411764,17.060816,-61.796428
Antigua and Barbuda,2020,100,100,167.98,0.31,0,0.02,6.060606,17.060816,-61.796428
Argentina,2000,95.78329,95,235.62,50.37,5.99,28.89,40.914955,-38.416097,-63.616672
Argentina,2001,95.51106,95.6,234.09,42.91,6.54,37.04,50.38733,-38.416097,-63.616672
Argentina,2002,96.22887,96.1,236.78,39.7,5.39,36.06,51.07825,-38.416097,-63.616672
Argentina,2003,96.442635,96.45,234.82,46.73,7.03,34.38,46.982075,-38.416097,-63.616672
Argentina,2004,96.6535,97.2,236.15,57.35,7.31,31.03,40.066883,-38.416097,-63.616672
Argentina,2005,96.863846,97.5,234.67,59.89,6.37,34.6,40.620663,-38.416097,-63.616672
"""

# Convert the string data into a DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))
#use pickle to read the map_df
map_df = pkl.load(open('merged_data.pkl', 'rb'))


##Function for endpoint=====CHANGE HER TO ADD VISUALIZATIONS
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data

def send_data(entity, year, electricity_access, cooking_fuel_access, 
              renewable_electricity_capacity, fossil_fuel_electricity, 
              nuclear_electricity, renewable_electricity, low_carbon_electricity):
    data = {
        'entity': entity,
        'year': year,
        'electricity_access': electricity_access,
        'cooking_fuel_access': cooking_fuel_access,
        'renewable_electricity_capacity': renewable_electricity_capacity,
        'fossil_fuel_electricity': fossil_fuel_electricity,
        'nuclear_electricity': nuclear_electricity,
        'renewable_electricity': renewable_electricity,
        'low_carbon_electricity': low_carbon_electricity,
    }
    response = requests.post(api_url, data=data)
    return response.json()

def generate_map(map_df, country, year = 2020, threshold = 0, criterion = 'IS NBE (TgCO2)'):
    # Filter the data for the selected country
    merged_data = map_df[map_df['Alpha 3 Code'] == country]
    # Create a base world map
    world_map = folium.Map(location=[merged_data['Latitude'].mean(), merged_data['Longitude'].mean()], zoom_start=2)
    # Add markers for each country
    world_map = folium.Map(location=[0, 0], zoom_start=2)

    # Prepare data for the heatmap
    heat_data = [[row['Latitude (average)'], row['Longitude (average)'], row[criterion]] for index, row in merged_data.iterrows()]

    # Add the heatmap layer
    HeatMap(heat_data).add_to(world_map)
    # Add markers for each country
    for _, row in map_df.iterrows():
        if row['Year'] != year:
            continue
        
        folium.Marker(
            location=[row['Latitude (average)'], row['Longitude (average)']],
            popup=f"{row['Alpha 3 Code']}: {row['IS NBE (TgCO2)']} TgCO2",
            icon=folium.Icon(color='blue' if row['IS NBE (TgCO2)'] < threshold else 'red')
        ).add_to(world_map)

    # Display the map in the notebook
    return world_map




# Streamlit app
st.title("Energy Access Dashboard")

# Sidebar filters
countries = df['Entity'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries)

#years = df['Year'].unique()
#selected_year = st.sidebar.selectbox("Select Year", years)


# Filter data based on selections
filtered_data = df[(df['Entity'] == selected_country)]# & (df['Year'] == selected_year)]

# Display filtered data
st.write("Filtered Data:")
st.write(filtered_data)

# Plotting
fig, ax = plt.subplots()
ax.plot(filtered_data['Year'], filtered_data['Access to electricity (% of population)'], marker='x', label='Access to Electricity')
ax.plot(filtered_data['Year'], filtered_data['Access to clean fuels for cooking'], marker='x', label='Access to Clean Fuels for Cooking')
ax.set_title(f'Population Access to Electricity in {selected_country}')
ax.set_xlabel('Year')
ax.set_ylabel('Access to Electricity (%)')
ax.grid()
ax.legend()

# Display plot
st.pyplot(fig)


##Session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

##test button 
##PRESSED TO GENERATE SUMMARY FROM LLMs
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")


##DATA FROM SWAPI API   ##EXAMPLE
swapi_endpoint = "https://swapi.dev/api/people/1/"

##FETCH DATA FROM OUR API
api_url = "http://127.0.0.1:8000/api/emissions/"
data = fetch_data(api_url)


if data:
    df = pd.DataFrame(data)
    st.dataframe(df)
