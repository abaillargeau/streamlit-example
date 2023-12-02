import streamlit as st 
import altair as alt
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import datetime
import subprocess
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


st.title("Steps visualization")

# 1 # Selección del intervalo

st.write('<p style="font-size:25px;">1. Interval definition', unsafe_allow_html=True)
st.write('<p style="font-size:18px;">Define the range in which you want to view the data </p>', unsafe_allow_html=True)

start_date = st.date_input("Select the beginning date")
start_time = st.time_input("Select the beginning time")

end_date = st.date_input("Select the ending date")
end_time = st.time_input("Select the ending time")

st.markdown(f"The results will be shown for the interval from <span style='color:blue;font-weight:bold;'>{start_date}</span> <span style='color:blue;font-weight:bold;'>{start_time}</span> to <span style='color:blue;font-weight:bold;'>{end_date}</span> <span style='color:blue;font-weight:bold;'>{end_time}</span>.", unsafe_allow_html=True)

# 2 # Selección del pie

st.write('<p style="font-size:25px;">2. Foot selection', unsafe_allow_html=True)

feet_options = ['Right foot', 'Left foot']
st.write('<p style="font-size:18px;">Choose the foot you want to visualize the data from.</p>', unsafe_allow_html=True)
selection = st.selectbox("Select the foot",feet_options)

if selection == 'Right foot':
    st.markdown("The results will be shown for the <span style='color:blue;font-weight:bold;'>right foot</span>.", unsafe_allow_html=True)
    
elif selection == 'Left foot':
    st.markdown("The results will be shown for the <span style='color:blue;font-weight:bold;'>left foot</span>.", unsafe_allow_html=True)

mac_izd = 'E0:52:B2:8B:2A:C2'
mac_der = 'C9:7B:84:76:32:14'
foot = 'A'
if selection == 'Right foot':
    foot = 'C9:7B:84:76:32:14'
elif selection == 'Left foot':
    foot = 'E0:52:B2:8B:2A:C2'

# 3 # Gráfico que muestra donde hay datos en el intervalo.

# Configuramos parámetros
mydb = mysql.connector.connect(
    host = "apiivm78.etsii.upm.es",
    user = "TBDA",
    password = "UPM#2324",
    database = "sclerosisTBDA")
cur = mydb.cursor()

statement = "SELECT desde, hasta FROM `actividad-G03` WHERE mac = %s AND (desde BETWEEN %s AND %s) AND (hasta BETWEEN %s AND %s)"
cur.execute(statement, (foot, f"{start_date} {start_time}", f"{end_date} {end_time}", f"{start_date} {start_time}", f"{end_date} {end_time}"))
data_intervals = pd.DataFrame(cur.fetchall(), columns=['desde', 'hasta'])

# Afficher les intervalles sur l'interface
st.write('<p style="font-size:25px;">3. Data intervals', unsafe_allow_html=True)
st.write('<p style="font-size:18px;">Intervals with available data in the selected range:</p>', unsafe_allow_html=True)


