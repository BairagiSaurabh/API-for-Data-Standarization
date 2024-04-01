import streamlit as st
import pandas as pd
import dtale

def main():
    st.title("EDA Generator")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file, na_values='Nan', low_memory=False)
        
        # Display DataFrame
        st.subheader("Sample DataFrame:")
        st.write(df)

        # Button to generate EDA
        if st.button("Generate EDA"):
            # Generate EDA using D-Tale
            d = dtale.show(df)
            d.open_browser()
            st.success("EDA Generated successfully! Click 'Shutdown' button to close.")
        
        # Button to shutdown D-Tale process
        if 'd' in locals() and st.button("Shutdown"):
            # Kill D-Tale process
            d.kill()
            st.success("D-Tale process shutdown successfully.")

if __name__ == "__main__":
    main()
