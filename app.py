import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('data/NYPD_Arrest_Data__Year_to_Date_.csv')
df = df.head(100)

st.title('NYPD Arrest Data')
st.text('Below shows a breakdown of every arrest effected in NYC by the NYPD in 2022')

if st.checkbox('Show first 100 records of NYPD Arrest Dataset'):
    st.dataframe(df)

code = '''def test():
    print("Hello, this is a testing code-block")'''
st.code(code, language='python')

st.subheader('Description of PD code')

df = pd.read_csv('data/NYPD_Arrest_Data__Year_to_Date_.csv')
pd_code = df['PD_DESC'].value_counts()
st.bar_chart(pd_code)
st.caption("This is a summary of the descrption of arrests")



st.subheader('Arrests in 2022')
arrest_day = df['ARREST_DATE']
st.line_chart(arrest_day)
st.caption(" A representation of the arrest dates in 2022 ")