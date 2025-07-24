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

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(layout="wide")

# st.title("📊 Test Plan Results for NV48_XTX_XT.xlsx")
# st.markdown("**[AMD Official Use Only - AMD Internal Distribution Only]**")

# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

# if uploaded_file:
#     df = pd.read_excel(uploaded_file, sheet_name="Test Results")
    
#     st.subheader("Sheet: Test Results")
#     st.markdown("### 🟢 Pie Charts for each tag in Sheet: Test Results")

#     tags = df['RequirementName'].dropna().unique()

#     for i in range(0, len(tags), 3):
#         cols = st.columns(3)
#         for j in range(3):
#             if i + j < len(tags):
#                 tag = tags[i + j]
#                 tag_df = df[df['RequirementName'] == tag]
#                 status_counts = tag_df['Status'].value_counts()

#                 with cols[j]:
#                     st.markdown(f"**Status Distribution for Tag `{tag}`**")
#                     fig, ax = plt.subplots()
#                     ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'orange', 'gold'])
#                     ax.axis('equal')
#                     st.pyplot(fig)

#     st.markdown("---")
#     st.markdown("### 📊 Bar Charts for each tag in Sheet: Test Results")

#     for i in range(0, len(tags), 3):
#         cols = st.columns(3)
#         for j in range(3):
#             if i + j < len(tags):
#                 tag = tags[i + j]
#                 tag_df = df[df['RequirementName'] == tag]
#                 status_counts = tag_df['Status'].value_counts()

#                 with cols[j]:
#                     st.markdown(f"**Status Distribution for Tag `{tag}`**")
#                     fig, ax = plt.subplots()
#                     sns.barplot(x=status_counts.index, y=status_counts.values, ax=ax, palette=['lightgreen', 'lightcoral', 'orange', 'gold'])
#                     ax.set_ylabel("Frequency")
#                     st.pyplot(fig)

#     st.markdown("---")
#     st.markdown("### 📋 Data Tables per Tag")

#     for tag in tags:
#         tag_df = df[df['RequirementName'] == tag]
#         status_counts = tag_df['Status'].value_counts()
#         total = status_counts.sum()

#         table_df = pd.DataFrame({
#             "Status": status_counts.index,
#             "Count": status_counts.values,
#             "Percentage": [f"{(count/total)*100:.2f}%" for count in status_counts.values]
#         })

#         st.markdown(f"**Data Table for Tag: {tag}**")
#         st.table(table_df)

#Original
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(layout="centered")

# st.title("📊 Test Results Analysis Parser")
# st.markdown("**Select a tag to visualize results**")

# uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

# if uploaded_file:
#     try:
#         df = pd.read_excel(uploaded_file, sheet_name="Test Results")
#     except Exception as e:
#         st.error(f"Error reading file: {e}")
#     else:
#         if 'RequirementName' not in df.columns or 'Status' not in df.columns:
#             st.error("Excel file must contain 'RequirementName' and 'Status' columns.")
#         else:
#             tags = sorted(df['RequirementName'].dropna().unique())

#             selected_tag = st.selectbox("🔍 Choose a tag (RequirementName)", tags)

#             tag_df = df[df['RequirementName'] == selected_tag]
#             status_counts = tag_df['Status'].value_counts()
#             total = status_counts.sum()

#             st.markdown(f"### 🥧 Pie Chart: Status Distribution for `{selected_tag}`")
#             fig1, ax1 = plt.subplots()
#             ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'orange', 'gold'])
#             ax1.axis('equal')
#             st.pyplot(fig1)

#             st.markdown(f"### 📊 Bar Chart: Status Count for `{selected_tag}`")
#             fig2, ax2 = plt.subplots()
#             ax2.bar(status_counts.index, status_counts.values, color=['lightgreen', 'lightcoral', 'orange', 'gold'])
#             ax2.set_ylabel("Count")
#             ax2.set_xlabel("Status")
#             ax2.set_title("Status Count")
#             st.pyplot(fig2)

#             st.markdown("### 📋 Summary Table")
#             table_df = pd.DataFrame({
#                 "Status": status_counts.index,
#                 "Count": status_counts.values,
#                 "Percentage": [f"{(count / total) * 100:.2f}%" for count in status_counts.values]
#             })
#             st.table(table_df)

# else:
#     st.info("Please upload an Excel file with a 'Test Results' sheet.")

#Single tags

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(layout="centered")
# st.title("📊 Test Results Analysis Parser")
# st.markdown("**Upload a Test Plan Excel and select a tag to view status charts and defect summary.**")

# uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

# if uploaded_file:
#     try:
#         df = pd.read_excel(uploaded_file, sheet_name="Test Results")
#     except Exception as e:
#         st.error(f"❌ Error reading Excel file: {e}")
#     else:
#         if 'RequirementName' not in df.columns or 'Status' not in df.columns:
#             st.error("Excel must contain columns: `RequirementName` and `Status`.")
#         else:
#             tags = sorted(df['RequirementName'].dropna().unique())
#             selected_tag = st.selectbox("🔍 Choose a tag (RequirementName)", tags)

#             tag_df = df[df['RequirementName'] == selected_tag]
#             status_counts = tag_df['Status'].value_counts()
#             total = status_counts.sum()

#             st.markdown(f"### 🥧 Pie Chart: Status Distribution for `{selected_tag}`")
#             fig1, ax1 = plt.subplots()
#             ax1.pie(
#                 status_counts,
#                 labels=status_counts.index,
#                 autopct='%1.1f%%',
#                 colors=['lightgreen', 'lightcoral', 'orange', 'gold', 'lightblue']
#             )
#             ax1.axis('equal')
#             st.pyplot(fig1)

#             st.markdown(f"### 📊 Bar Chart: Status Count for `{selected_tag}`")
#             fig2, ax2 = plt.subplots()
#             ax2.bar(
#                 status_counts.index,
#                 status_counts.values,
#                 color=['lightgreen' if s.lower() == 'passed' else 'lightcoral' for s in status_counts.index]
#             )
#             ax2.set_ylabel("Count")
#             ax2.set_xlabel("Status")
#             ax2.set_title("Status Count")
#             st.pyplot(fig2)

#             st.markdown("### 📋 Summary Table")
#             table_df = pd.DataFrame({
#                 "Status": status_counts.index,
#                 "Count": status_counts.values,
#                 "Percentage": [f"{(count / total) * 100:.2f}%" for count in status_counts.values]
#             })
#             st.table(table_df)

#             # 🔴 Defects Section (show only if defects found)
#             defect_statuses = ["Failed", "Blocked", "Not Completed", "Error"]
#             defect_df = tag_df[tag_df['Status'].isin(defect_statuses)]

#             if not defect_df.empty:
#                 st.markdown("### 🔴 Defect Summary")
#                 defect_counts = defect_df['Status'].value_counts()
#                 defect_table = pd.DataFrame({
#                     "Defect Status": defect_counts.index,
#                     "Count": defect_counts.values,
#                     "Percentage": [f"{(count / total) * 100:.2f}%" for count in defect_counts.values]
#                 })
#                 st.table(defect_table)
#             else:
#                 st.success("✅ No defects found in the selected tag.")

# else:
#     st.info("📤 Please upload an Excel file with a 'Test Results' sheet.")

# Multiple tags

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(layout="centered")
# st.title("📊 Test Results Analysis Parser (Multi-Tag View)")
# st.markdown("**Upload an Excel file and select one or more tags to visualize results and defect summaries.**")

# uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

# if uploaded_file:
#     try:
#         df = pd.read_excel(uploaded_file, sheet_name="Test Results")
#     except Exception as e:
#         st.error(f"❌ Error reading Excel file: {e}")
#     else:
#         if 'RequirementName' not in df.columns or 'Status' not in df.columns:
#             st.error("Excel must contain columns: `RequirementName` and `Status`.")
#         else:
#             tags = sorted(df['RequirementName'].dropna().unique())
#             selected_tags = st.multiselect("🔍 Choose one or more tags (RequirementName)", tags)

#             if selected_tags:
#                 for selected_tag in selected_tags:
#                     st.markdown(f"---\n## 📘 Results for: `{selected_tag}`")

#                     tag_df = df[df['RequirementName'] == selected_tag]
#                     status_counts = tag_df['Status'].value_counts()
#                     total = status_counts.sum()

#                     # Pie Chart
#                     st.markdown(f"### 🥧 Pie Chart: Status Distribution")
#                     fig1, ax1 = plt.subplots()
#                     ax1.pie(
#                         status_counts,
#                         labels=status_counts.index,
#                         autopct='%1.1f%%',
#                         colors=['lightgreen', 'lightcoral', 'orange', 'gold', 'lightblue']
#                     )
#                     ax1.axis('equal')
#                     st.pyplot(fig1)

#                     # Bar Chart
#                     st.markdown(f"### 📊 Bar Chart: Status Count")
#                     fig2, ax2 = plt.subplots()
#                     ax2.bar(
#                         status_counts.index,
#                         status_counts.values,
#                         color=['lightgreen' if s.lower() == 'passed' else 'lightcoral' for s in status_counts.index]
#                     )
#                     ax2.set_ylabel("Count")
#                     ax2.set_xlabel("Status")
#                     ax2.set_title("Status Count")
#                     st.pyplot(fig2)

#                     # Summary Table
#                     st.markdown("### 📋 Summary Table")
#                     table_df = pd.DataFrame({
#                         "Status": status_counts.index,
#                         "Count": status_counts.values,
#                         "Percentage": [f"{(count / total) * 100:.2f}%" for count in status_counts.values]
#                     })
#                     st.table(table_df)

#                     # Defects Table (if any)
#                     defect_statuses = ["Failed", "Blocked", "Not Completed", "Error"]
#                     defect_df = tag_df[tag_df['Status'].isin(defect_statuses)]

#                     if not defect_df.empty:
#                         st.markdown("### 🔴 Defect Summary")
#                         defect_counts = defect_df['Status'].value_counts()
#                         defect_table = pd.DataFrame({
#                             "Defect Status": defect_counts.index,
#                             "Count": defect_counts.values,
#                             "Percentage": [f"{(count / total) * 100:.2f}%" for count in defect_counts.values]
#                         })
#                         st.table(defect_table)
#                     else:
#                         st.success("✅ No defects found in this tag.")
#             else:
#                 st.info("Please select at least one tag to view results.")
# else:
#     st.info("📤 Please upload an Excel file with a 'Test Results' sheet.")

Final Streamlit Code (PDF Save Feature Included):
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import zipfile

st.set_page_config(layout="centered")
st.title("📊 Test Results Analysis Parser (Multi-Tag with PDF Export)")
st.markdown("**Upload Excel and select tags to view and export summaries.**")

uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])



def save_pdf(tag, status_counts, total, summary_table_df, defect_table_df, pie_buf, bar_buf):
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    spacer = Spacer(1, 12)

    # Title
    elements.append(Paragraph(f"<b>Test Summary Report - {tag}</b>", styles['Title']))
    elements.append(spacer)

    # Pie Chart Image
    pie_img = Image(pie_buf)
    pie_img.drawHeight = 200
    pie_img.drawWidth = 200
    elements.append(Paragraph("<b>Pie Chart: Status Distribution</b>", styles['Heading3']))
    elements.append(pie_img)
    elements.append(spacer)

    # Bar Chart Image
    bar_img = Image(bar_buf)
    bar_img.drawHeight = 200
    bar_img.drawWidth = 200
    elements.append(Paragraph("<b>Bar Chart: Status Count</b>", styles['Heading3']))
    elements.append(bar_img)
    elements.append(spacer)

    # Summary Table
    elements.append(Paragraph("<b>Summary Table:</b>", styles['Heading3']))
    table_data = [summary_table_df.columns.tolist()] + summary_table_df.values.tolist()
    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ]))
    elements.append(table)
    elements.append(spacer)

    # Defect Table (if present)
    if not defect_table_df.empty:
        elements.append(Paragraph("<b>Defect Summary:</b>", styles['Heading3']))
        defect_data = [defect_table_df.columns.tolist()] + defect_table_df.values.tolist()
        defect_table = Table(defect_data, hAlign='LEFT')
        defect_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightcoral),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('GRID',(0,0),(-1,-1),1,colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ]))
        elements.append(defect_table)

    doc.build(elements)
    pdf_buffer.seek(0)
    return pdf_buffer

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name="Test Results")
    except Exception as e:
        st.error(f"❌ Error reading Excel file: {e}")
    else:
        if 'RequirementName' not in df.columns or 'Status' not in df.columns:
            st.error("Excel must contain columns: `RequirementName` and `Status`.")
        else:
            tags = sorted(df['RequirementName'].dropna().unique())
            selected_tags = st.multiselect("🔍 Choose one or more tags (RequirementName)", tags)

            pdf_files = []
            if selected_tags:
                for selected_tag in selected_tags:
                    st.markdown(f"---\n## 📘 Results for: `{selected_tag}`")

                    tag_df = df[df['RequirementName'] == selected_tag]
                    status_counts = tag_df['Status'].value_counts()
                    total = status_counts.sum()

                    # Pie chart
                    fig1, ax1 = plt.subplots()
                    ax1.pie(
                        status_counts,
                        labels=status_counts.index,
                        autopct='%1.1f%%',
                        colors=['lightgreen', 'lightcoral', 'orange', 'gold', 'lightblue']
                    )
                    ax1.axis('equal')
                    pie_buf = BytesIO()
                    plt.savefig(pie_buf, format='png')
                    st.pyplot(fig1)
                    plt.close(fig1)

                    # Bar chart
                    fig2, ax2 = plt.subplots()
                    ax2.bar(
                        status_counts.index,
                        status_counts.values,
                        color=['lightgreen' if s.lower() == 'passed' else 'lightcoral' for s in status_counts.index]
                    )
                    ax2.set_ylabel("Count")
                    ax2.set_xlabel("Status")
                    ax2.set_title("Status Count")
                    bar_buf = BytesIO()
                    plt.savefig(bar_buf, format='png')
                    st.pyplot(fig2)
                    plt.close(fig2)

                    # Summary Table
                    summary_table_df = pd.DataFrame({
                        "Status": status_counts.index,
                        "Count": status_counts.values,
                        "Percentage": [f"{(count / total) * 100:.2f}%" for count in status_counts.values]
                    })
                    st.table(summary_table_df)

                    # Defect Summary
                    defect_statuses = ["Failed", "Blocked", "Not Completed", "Error"]
                    defect_df = tag_df[tag_df['Status'].isin(defect_statuses)]
                    defect_table_df = pd.DataFrame()

                    if not defect_df.empty:
                        st.markdown("### 🔴 Defect Summary")
                        defect_counts = defect_df['Status'].value_counts()
                        defect_table_df = pd.DataFrame({
                            "Defect Status": defect_counts.index,
                            "Count": defect_counts.values,
                            "Percentage": [f"{(count / total) * 100:.2f}%" for count in defect_counts.values]
                        })
                        st.table(defect_table_df)
                    else:
                        st.success("✅ No defects found in this tag.")

                    # Save to PDF
                    pdf_buf = save_pdf(selected_tag, status_counts, total, summary_table_df, defect_table_df, pie_buf, bar_buf)
                    pdf_files.append((f"{selected_tag}.pdf", pdf_buf))

                # Zip all PDFs
                zip_buf = BytesIO()
                with zipfile.ZipFile(zip_buf, "w") as zipf:
                    for filename, filedata in pdf_files:
                        zipf.writestr(filename, filedata.getvalue())
                zip_buf.seek(0)

                st.download_button(
                    label="📥 Download All Summaries as ZIP",
                    data=zip_buf,
                    file_name="Test_Summaries.zip",
                    mime="application/zip"
                )
            else:
                st.info("Please select at least one tag to view results.")
else:
    st.info("📤 Please upload an Excel file with a 'Test Results' sheet.")


# import streamlit as st
# import pandas as pd
# import os
# from pandasai import SmartDataframe
# from pandasai.llm.openai import OpenAI
# import matplotlib.pyplot as plt

# # --- Streamlit UI setup ---
# st.set_page_config(layout="centered")
# st.title("🧠 Test Results Agent (Powered by OpenRouter)")
# st.markdown("Upload a test results Excel file and ask questions in plain English.")

# # --- Upload file ---
# uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

# if uploaded_file:
#     try:
#         df = pd.read_excel(uploaded_file, sheet_name="Test Results")
#         st.success("✅ File loaded successfully.")
#         st.dataframe(df.head())
#     except Exception as e:
#         st.error(f"❌ Error reading Excel file: {e}")
#     else:
#         # --- Prompt box ---
#         prompt = st.text_area("💬 Ask a question about the data:",
#                               placeholder="Example: Show failed test cases by RequirementName")

#         if prompt:
#             with st.spinner("🤖 Thinking..."):
#                 try:
#                     # --- OpenRouter LLM via PandasAI ---
#                     llm = OpenAI(
#                         api_token="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",  # 🔑 Replace this with your OpenRouter API key
#                         api_base="https://openrouter.ai/api/v1",
#                         model="mistralai/mistral-7b-instruct"  # ✅ Fast, free model
#                     )

#                     sdf = SmartDataframe(df, config={"llm": llm, "enable_cache": False})

#                     # --- Get response ---
#                     result = sdf.chat(prompt)

#                     # --- Show response ---
#                     if isinstance(result, pd.DataFrame):
#                         st.dataframe(result)
#                     elif isinstance(result, plt.Figure):
#                         st.pyplot(result)
#                     else:
#                         st.markdown(f"**💡 Answer:** {result}")
#                 except Exception as e:
#                     st.error(f"⚠️ Agent failed: {e}")
# else:
#     st.info("Please upload an Excel file with a 'Test Results' sheet.")

