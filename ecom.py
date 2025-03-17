import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title('E-commerce Dashboard')
    st.sidebar.title("You can uplode your data here")

    upload_file = st.sidebar.file_uploader("Upload your CSV or Excel file here", type = ['csv', 'xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
               data = pd.read_csv(upload_file)

            else:
               data = pd.read_excel(upload_file) 
            st.sidebar.success('File successfully uploaded') 

            st.subheader('Data Information')
            st.dataframe(data.head()) 

            st.subheader("Lets see some more details about the data")
            st.write("Shape of the data is ", data.shape)
            st.write("Columns names are ", data.columns)
            st.write("Missing value into columns are ", data.isnull().sum())

            st.subheader("Data Statistics")
            st.write(data.describe())

            
        except Exception as e:
            print(e)       

if __name__ == "__main__":
    main()   