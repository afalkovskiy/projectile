import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math

pi = math.pi

def ricker(f, length=0.512, dt=0.001):
    t = np.linspace(-length/2, (length-dt)/2, length/dt)
    y = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y

#fig, ax = plt.subplots()
f = 25

t, y = ricker (f)

st.title('Ricker wavelet') 
#st.button('Hit me')
st.subheader("f(x) = A*sin(B(x+C)) + D")
a = st.slider('Select a value of A from [-10, 10]', value=1., min_value=-10., max_value=10.)
st.write("A = ", a)

b = st.slider('Select a value of B from [0, 10]', value=1., min_value=0., max_value=10.)
st.write("B = ", a)

c = st.slider('Select a value of C from [-10, 10]', value=0., min_value=-10., max_value=10.)
st.write("C = ", c)

d = st.slider('Select a value of D from [-10, 10]', value=0., min_value=-10., max_value=10.)
st.write("D = ", d)

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
