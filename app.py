import streamlit as st
import pandas as pd

st.title("Excel Reader")

uploaded_file = st.file_uploader(
    "เลือกไฟล์ Excel",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.success("อ่านไฟล์สำเร็จ")
    st.dataframe(df)

    st.write("จำนวนแถว:", len(df))
    st.write("จำนวนคอลัมน์:", len(df.columns))