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


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Set the page title
# st.set_page_config(page_title="Test Plan Pie Chart Viewer", layout="wide")

# st.title("Test Plan Pie Chart Viewer")
# st.markdown("Upload your Excel file and visualize distribution of values as a pie chart.")

# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

# if uploaded_file is not None:
#     try:
#         # Load all sheets into a dictionary
#         all_sheets = pd.read_excel(uploaded_file, sheet_name=None)

#         # Sheet selector
#         sheet_names = list(all_sheets.keys())
#         selected_sheet = st.selectbox("Select a Sheet", sheet_names)

#         df = all_sheets[selected_sheet]

#         # Show raw data
#         if st.checkbox("Show raw data"):
#             st.dataframe(df)

#         # Check if dataframe is not empty
#         if not df.empty:
#             # Column selector for pie chart
#             column = st.selectbox("Select Column for Pie Chart", df.columns)

#             # Replace missing or empty values
#             df[column] = df[column].fillna("Missing").replace("", "Missing")

#             pie_data = df[column].value_counts()

#             # Create the pie chart
#             fig, ax = plt.subplots()
#             ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
#             ax.axis("equal")
#             st.pyplot(fig)
#         else:
#             st.warning("Selected sheet is empty.")
#     except Exception as e:
#         st.error(f"Failed to process file: {e}")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.title("📊 Test Plan Results for NV48_XTX_XT.xlsx")
st.markdown("**[AMD Official Use Only - AMD Internal Distribution Only]**")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="Test Results")
    
    st.subheader("Sheet: Test Results")
    st.markdown("### 🟢 Pie Charts for each tag in Sheet: Test Results")

    tags = df['RequirementName'].dropna().unique()

    for i in range(0, len(tags), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(tags):
                tag = tags[i + j]
                tag_df = df[df['RequirementName'] == tag]
                status_counts = tag_df['Status'].value_counts()

                with cols[j]:
                    st.markdown(f"**Status Distribution for Tag `{tag}`**")
                    fig, ax = plt.subplots()
                    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'orange', 'gold'])
                    ax.axis('equal')
                    st.pyplot(fig)

    st.markdown("---")
    st.markdown("### 📊 Bar Charts for each tag in Sheet: Test Results")

    for i in range(0, len(tags), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(tags):
                tag = tags[i + j]
                tag_df = df[df['RequirementName'] == tag]
                status_counts = tag_df['Status'].value_counts()

                with cols[j]:
                    st.markdown(f"**Status Distribution for Tag `{tag}`**")
                    fig, ax = plt.subplots()
                    sns.barplot(x=status_counts.index, y=status_counts.values, ax=ax, palette=['lightgreen', 'lightcoral', 'orange', 'gold'])
                    ax.set_ylabel("Frequency")
                    st.pyplot(fig)

    st.markdown("---")
    st.markdown("### 📋 Data Tables per Tag")

    for tag in tags:
        tag_df = df[df['RequirementName'] == tag]
        status_counts = tag_df['Status'].value_counts()
        total = status_counts.sum()

        table_df = pd.DataFrame({
            "Status": status_counts.index,
            "Count": status_counts.values,
            "Percentage": [f"{(count/total)*100:.2f}%" for count in status_counts.values]
        })

        st.markdown(f"**Data Table for Tag: {tag}**")
        st.table(table_df)

