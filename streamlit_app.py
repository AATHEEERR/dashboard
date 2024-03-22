

import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# with open('C:/Users/96650/Downloads/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.write( """
<style>
/* Logo */
[data-testid="stSidebar"] {
    background-image: url(https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png);
    background-size: 200px;
    background-repeat: no-repeat;
    background-position: 4px 20px;
}

/* Card */
div.css-1r6slb0.e1tzin5v2 {
    background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    border-left: 0.5rem solid #9AD8E1 !important;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;
}

label.css-mkogse.e16fv1kl2 {
    color: #36b9cc !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
}

/* Move block container higher */
div.block-container.css-18e3th9.egzxvld2 {
  margin-top: -5em;
}

/* Hide hamburger menu and footer */
div.css-r698ls.e8zbici2, footer.css-ipbk5a.egzxvld4, footer.css-12gp8ed.eknhn3m4, div.vg-tooltip-element {
  display: none;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.header('Dashboard `version 2`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
''')

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv',
                              parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom',
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x='date', y=plot_data, height=plot_height)

