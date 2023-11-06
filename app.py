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

option = st.selectbox(
    'Which semester?',
    (semesterList))

result_df = studentInfo[studentInfo['code_presentation']==option]

st.dataframe(result_df)