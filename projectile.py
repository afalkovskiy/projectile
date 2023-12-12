import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math
# st.set_page_config(layout="wide")
padding_top = 0
st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)


pi = math.pi
g = 9.81

def projectile(v, alpha, dt=0.01):
    vx = v * math.cos(alpha)
    vy = v * math.sin(alpha)
    g = 9.81
    t1 = vy/g
    t2 = 2*t1
    d = vx*t2
    h = vy*t1 - 0.5*g*t1**2
    t2 = 2 * vy / g
    t = np.linspace(0, t2, int(t2/dt))
    x = vx * t
    y = vy * t - 0.5 * g * np.square(t)
    return x, y, t2, d, h
    

#fig, ax = plt.subplots()

st.header('Projectile Motion') 
#st.button('Hit me')

col1, col2 = st.columns(2)
with col1:
    v = st.slider('Velocity (m/s)', value=120., min_value=1., max_value=1500.)
    # st.write("Velocity = ", v)
with col2:
    alpha = st.slider('Inclination to the horizontal (deg)', value=30., min_value=0., max_value=90.)
    alpha_rad = pi * alpha / 180.
    # st.write("alpha_rad = ", alpha_rad)


x, y, t2, d, h = projectile(v, alpha_rad)
txt0 = "vel = " + str(round(v,1)) + " m/s;  angle = " + str(round(alpha,1)) + " deg"
st.subheader(txt0)
txt1 = "t = " + str(round(t2,1)) + " s;  d = " + str(round(d,1)) + " m;  h = " + str(round(h,1)) +" m"
st.subheader(txt1)

fig, ax = plt.subplots()

ax = plt.gca()
xmin = 0.
ymin = 0.
xmax = max(round(d/500.,0) * 500. + 500., round(h/500.,0) * 500. + 500.)
ymax = xmax
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])


ax.plot(x, y, linestyle='dashed')
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
st.pyplot(fig)

st.latex(r'''
v_x = v \cdot cos( \theta ); v_y = v \cdot sin( \theta )
''') 

st.latex(r'''
Ricker(t) = (1-2\pi^2 f^2 t^2)e^{-\pi^2 f^2 t^2}
''') 
st.latex(r'''
    Ormsby(t) = \frac{\pi f_4^2 sinc^2 (\pi f_4 t) - \pi f_3^2 sinc^2 (\pi f_3 t)}{f_4 - f_3}  
    - \frac{\pi f_2^2 sinc^2 (\pi f_2 t) - \pi f_1^2 sinc^2 (\pi f_1 t)}{f_2 - f_1}
    ''') 


# chart_data = pd.DataFrame(
#    { "x(m)": x, "y": y}
# )
# st.line_chart(chart_data, x="x(m)", y="y")
