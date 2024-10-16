import streamlit as st
import pandas as pd
from classifier_application.content_classifier import apply_classification  

st.title("Inappropriate Content Classifier")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) 

    if 'clean_text' in df.columns:
        if st.button("Classify Inappropriate Content"):
            sample_df = df.sample(n=100, random_state=42)
            classified_sample = apply_classification(sample_df)
            st.write("Classified data:")
            st.write(classified_sample)
            csv = classified_sample.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Classified Data as CSV",
                data=csv,
                file_name='classified_data.csv',
                mime='text/csv'
            )
    else:
        st.error("The dataset does not contain a 'clean_text' column. Please upload a valid dataset.")
