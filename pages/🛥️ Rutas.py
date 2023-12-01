import streamlit as st
from folium import Map
from streamlit_folium import st_folium
from utils.connection import MongoHelper
import pandas as pd
import folium

# DB Query
@st.cache_resource
def get_vessels():
    mongo_helper = MongoHelper()
    results_list = mongo_helper.get_vessels()
    mongo_helper.close()
    return results_list

@st.cache_resource
def get_vessel_name(name):
    mongo_helper = MongoHelper()
    results_list = mongo_helper.get_vessel_data(name)
    mongo_helper.close()
    return results_list

st.markdown("<h1 style='text-align: center;'>Estimación de rutas de los barcos</h1>", unsafe_allow_html=True)

vessel_list = get_vessels()
option = st.selectbox(
    'Elija el nombre del barco',
    vessel_list)
vessel_data = get_vessel_name(option)
df = pd.DataFrame.from_records(vessel_data)
df = df.sort_values(by=['VesselName','date_col'])
df['geometry']= df['geometry'].apply(lambda x : x['coordinates'])
total_miles = 0
m = Map(center=[30.989850, -92.253279])
for i in range(len(df)):
    #calculo de millas
    total_miles = total_miles + df['geom_len'].iloc[i]
    #calculo de geometrías
    l=df['geometry'].iloc[i]
    switched_list = [[b, a] for a, b in l]
    folium.PolyLine(switched_list, color="navy").add_to(m)
st.markdown("<h3 style='text-align: center;'>Mapa de la ruta del barco</h3>", unsafe_allow_html=True)
st_folium(m,width=700,zoom=6)
st.markdown("<h3 style='text-align: center;'>Estimación de longitud recorrida por el barco</h3>", unsafe_allow_html=True)
col1,col2,col3 = st.columns([3.5,3.5,3])
with col2:
    #st.metric(label='Millas recorridas',value='80')
    st.markdown("""
    <style>
    .big-font {
        font-size:80px !important;
        color: #00FF00 !important;
    }
    .small-font {
        font-size:25px !important;
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">{}</p>'.format(round(total_miles*0.000621371,2)), unsafe_allow_html=True)
st.markdown('<p class="small-font">Millas recorridas</p>', unsafe_allow_html=True)
    