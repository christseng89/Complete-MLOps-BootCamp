# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title('Simple Streamlit App')

# Create a slider widget to get input from the user
slider_value = st.slider('Select a value', 0, 100, 50)

# Display the slider value
st.write(f'Slider value: {slider_value}')

# Display a random chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Display a DataFrame
st.write("Here's a simple DataFrame:")
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write(df)
