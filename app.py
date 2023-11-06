import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studentInfo   = pd.read_csv('studentInfo.csv')
studentReg    = pd.read_csv('studentRegistration.csv')
studentAssess = pd.read_csv('studentAssessment.csv')

semesterList = studentInfo['code_presentation'].unique()

st.write(
    '## Dashboard Title'
)
on = st.checkbox('Show all')

option = st.selectbox(
    'Which semester?',
    (semesterList))

if on:
    result_df = studentInfo
else:
    result_df = studentInfo[studentInfo['code_presentation']==option]

st.dataframe(result_df)

student_by_gender = pd.crosstab(index=result_df['code_presentation'], columns=result_df['gender'])

st.bar_chart(student_by_gender)