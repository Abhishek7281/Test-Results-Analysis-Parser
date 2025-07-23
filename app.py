import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Upload Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    column = st.selectbox("Choose column to plot", df.columns)
    pie_data = df[column].value_counts()
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
    st.pyplot(fig)
