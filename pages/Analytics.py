import streamlit as st
import pandas as pd

from utils.database import get_patient_history

st.title("📊 Healthcare Analytics")

df = get_patient_history()

if df.empty:

    st.warning(
        "No patient records found."
    )

else:

    st.subheader(
        "Disease Distribution"
    )

    disease_count = (
        df["disease"]
        .value_counts()
    )

    st.bar_chart(
        disease_count
    )

    st.subheader(
        "Average Risk"
    )

    avg_risk = (
        df.groupby(
            "disease"
        )["risk"]
        .mean()
    )

    st.bar_chart(
        avg_risk
    )

    st.subheader(
        "Age Distribution"
    )

    st.line_chart(
        df["age"]
    )

    st.dataframe(df)