import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import sklearn
import joblib

import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)


def header(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

header("Claimnants Dataset")

data=pd.read_csv(r"C:\Users\shubh_yuamufh\OneDrive\Desktop\claimants.csv")


# Columns

def head1(url):
     col1.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

col1,col2=st.columns(2)
head1("head")
col1.write(data.head())

def tail(url):
     col2.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

tail("Tail")
col2.write(data.tail())

Viz('Visualization')

col=data.columns

for i in data.columns:
    if data[i].max()>1:
        plt.figure(figsize=(5,5))
        fig,ax=plt.subplots()
        ax.hist(data[i])
        ax.set_title(i)
        ax.set_xlabel(f'Skewness{round(data[i].skew(),2)}\nkurt: {round(data[i].kurt(),2)}')
        # ax.set_xticks([0,1])
        st.pyplot(fig)

    else:
        
        plt.figure(figsize=(10,10))
        fig,ax=plt.subplots()

        st.write(data[i].value_counts())

        ax.bar(data[i].value_counts().keys(),data[i].value_counts().values,)
        ax.set_title(i)
        # ax.set_xlabel(i)
        ax.set_xticks([0,1])
        st.pyplot(fig)

        plt.figure(figsize=(10,10))
        fig,ax=plt.subplots()