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
st.subheader("f(x) = A*sin(B(x+C)) + D")
f = st.slider('Select a value of A from [1, 240]', value=60., min_value=1., max_value=240.)
st.write("Frequency = ", f)
t, y = ricker (f)


x = np.arange(0, 4*np.pi, 0.1)
sinx = a * np.sin(b*(x+c)) + d
cosx = np.cos(x)

chart_data = pd.DataFrame(
   {
       "t": t,
       "y": y
   }
)

st.line_chart(chart_data, x="t", y="y")
