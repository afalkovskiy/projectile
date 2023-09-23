import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math

pi = math.pi

def ricker(f, length=0.512, dt=0.001):
    t = np.linspace(-length/2, (length-dt)/2, int(length/dt))
    y = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y

#fig, ax = plt.subplots()
f = 25

st.title('Ricker wavelet') 
#st.button('Hit me')
st.subheader("f(t) = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))")
f = st.slider('Select frequency from [1, 240] Hz', value=60., min_value=1., max_value=240.)
st.write("Frequency = ", f)
t, y = ricker (f)

chart_data = pd.DataFrame(
   {
       "t": t,
       "y": y
   }
)

st.line_chart(chart_data, x="t", y="y")
