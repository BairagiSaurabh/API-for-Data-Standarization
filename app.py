import streamlit as st
import pandas as pd
from try_main import Data_Preprocess
import logging
import os

import feature_engine
import numpy as np
import pandas as pds
import dtale
from sklearn.model_selection import train_test_split
from feature_engine.imputation import (
    MeanMedianImputer,
    CategoricalImputer,
    ArbitraryNumberImputer
)
from feature_engine.encoding import WoEEncoder
from feature_engine.selection import DropConstantFeatures
from feature_engine.creation import CyclicalFeatures
from feature_engine.encoding import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from feature_engine.encoding import CountFrequencyEncoder
from feature_engine.selection import DropCorrelatedFeatures
from feature_engine.outliers import Winsorizer, ArbitraryOutlierCapper, OutlierTrimmer
from io import BytesIO
import base64
import warnings
warnings.filterwarnings('ignore')

# Utility function to read log file
def read_log_file(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    return logs

def main():
    st.title("Data Preprocessing Tool")
    st.sidebar.title("Existing Data Types")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        # Display existing data types in the sidebar
        existing_datatypes = df.dtypes
        st.sidebar.write(existing_datatypes)

        st.write("Sample Dataframe:")
        st.dataframe(df.head(10).style.set_properties(**{'text-align': 'left'}), width=2000)
        excel_file_name = st.text_input("Enter the name for the final Excel file (without extension):")
       
        # Inputs for changing datatype
        change_datatype = st.radio("Do you want to change the datatype?", ('Yes', 'No'))
        if change_datatype == 'Yes':
            column_name = st.text_input("Provide the list of column names to change datatype (comma-separated):")
            new_datatype = st.text_input("Provide the list of datatypes to be changed in the same order as columns above (comma-separated - int,float,datetime,str,bool):")
        else:
            column_name, new_datatype = None, None

        # Select the target column
        target_column = st.text_input("Enter the target column:")

        # Button to preprocess data
        if st.button("Preprocess Data"):
            if excel_file_name:
                # Create Data_Preprocess object
                data_processor = Data_Preprocess(df, excel_file_name)

                # Run preprocessing
                data_processor.run(change_datatype=change_datatype == 'Yes',
                                   column_name=column_name,
                                   new_datatype=new_datatype,
                                   target_column=target_column)

                st.write("Preprocessing Done!!!")

                # Provide option to download the Excel file
                st.markdown(get_binary_file_downloader_html(excel_file_name), unsafe_allow_html=True)

        # Option to view logs
        if st.button("View Logs"):
            logs_dir = os.getcwd()
            log_files = [file for file in os.listdir(logs_dir) if file.endswith("_logfile.log")]

            if log_files:
                selected_log_file = st.selectbox("Select Log File", log_files)
                logs = read_log_file(selected_log_file)
                for log in logs:
                    st.write(log)
            else:
                st.write("No log files found.")

def get_binary_file_downloader_html(file_path):
    with open(file_path + '.xlsx', 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:file/xlsx;base64,{b64}" download="{file_path}.xlsx">Download Excel file</a>'


if __name__ == "__main__":
    main()
