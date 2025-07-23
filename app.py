# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# uploaded_file = st.file_uploader("Upload Excel", type=["xlsx"])
# if uploaded_file:
#     df = pd.read_excel(uploaded_file)
#     column = st.selectbox("Choose column to plot", df.columns)
#     pie_data = df[column].value_counts()
#     fig, ax = plt.subplots()
#     ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
#     st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page title
st.set_page_config(page_title="Test Plan Pie Chart Viewer", layout="wide")

st.title("Test Plan Pie Chart Viewer")
st.markdown("Upload your Excel file and visualize distribution of values as a pie chart.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Load all sheets into a dictionary
        all_sheets = pd.read_excel(uploaded_file, sheet_name=None)

        # Sheet selector
        sheet_names = list(all_sheets.keys())
        selected_sheet = st.selectbox("Select a Sheet", sheet_names)

        df = all_sheets[selected_sheet]

        # Show raw data
        if st.checkbox("Show raw data"):
            st.dataframe(df)

        # Check if dataframe is not empty
        if not df.empty:
            # Column selector for pie chart
            column = st.selectbox("Select Column for Pie Chart", df.columns)

            # Replace missing or empty values
            df[column] = df[column].fillna("Missing").replace("", "Missing")

            pie_data = df[column].value_counts()

            # Create the pie chart
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
        else:
            st.warning("Selected sheet is empty.")
    except Exception as e:
        st.error(f"Failed to process file: {e}")
