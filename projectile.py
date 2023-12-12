import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math

pi = math.pi

def projectile(v, alpha, dt=0.01):
    vx = v * math.cos(alpha)
    vy = v * math.sin(alpha)
    g = 9.81
    t2 = 2 * vy / g
    t = np.linspace(0, t2, int(t2/dt))
    x = vx * t
    y = vy * t - 0.5 * g * np.square(t)
    return x, y
    

#fig, ax = plt.subplots()

st.title('Projectile') 
#st.button('Hit me')

col1, col2 = st.columns(2)
with col1:
    v = st.slider('Velocity (m/s)', value=120., min_value=1., max_value=1200.)
    st.write("Velocity = ", v)
with col2:
    alpha = st.slider('Inclination to the horizontal (deg)', value=30., min_value=0., max_value=90.)
    alpha_rad = pi * alpha / 180.
    st.write("alpha_rad = ", alpha_rad)

st.subheader("Vx = V * Cos(alpha) = ")

x, y = projectile(v, alpha_rad)

chart_data = pd.DataFrame(
   {
       "x": x,
       "y": y
   }
)

st.line_chart(chart_data, x="x", y="y")
