import streamlit as st
from folium import Map
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from utils.connection import MongoHelper

# DB Query
@st.cache_resource
def get_data():
    mongo_helper = MongoHelper()
    results_list = mongo_helper.get_heatmap_data()
    mongo_helper.close()
    return results_list

results_list = get_data()


# Formatting data
heat_data = [[x['LAT'], x['LON'], x['cnt']] for x in results_list]


# ========== MAP ============
st.header("Mapa de Calor")
m = Map(location=[30.989850, -92.253279], zoom_start=6)
heat_map = HeatMap(heat_data,min_opacity=0.4,blur = 18)
heat_map.add_to(m)

st_data = st_folium(m, width=725)

