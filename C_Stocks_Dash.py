import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px   

path = './pilot_topdown_CO2_Budget_countries_v1.csv'
df_co2 = pd.read_csv(path, skiprows=52)
#df_co2.head()

st.set_page_config(
    page_title="CO2 Stocks Budget Dashboard Sample",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

with st.sidebar:
    st.title('🏂 CO2 Stocks Budget Dashboard Sample')
    
    year_list = list(df_co2['Year'].unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df_co2[df_co2['Year'] == selected_year]
    #df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap

def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth

col = st.columns((1.5, 4.5, 2), gap='medium')
with col[0]:
    st.markdown('#### Gains/Losses')

    #df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

    if selected_year > 2010:
        #first_state_name = df_population_difference_sorted.states.iloc[0]
        #first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
        #first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
        print("YEAR IS GREATER THAN 2010")

with col[1]:
    st.markdown('#### Total Budget')
    
    choropleth = make_choropleth(df_selected_year,'Year', selected_color_theme)
    st.plotly_chart(choropleth, use_container_width=True)
    
    heatmap = make_heatmap(df_co2, 'Year', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)

with col[2]:
    st.markdown('#### Top Budget')

    st.dataframe(df_selected_year,
                 column_order=("Year"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "Year": st.column_config.TextColumn(
                        "Year",
                    )}
                 )
    
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
            - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
            - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            ''')
    