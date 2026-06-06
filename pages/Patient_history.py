import streamlit as st

from utils.database import (
    get_patient_history
)

st.title(
    "📋 Patient History"
)

df = get_patient_history()

if df.empty:

    st.warning(
        "No records available."
    )

else:

    search_name = st.text_input(
        "Search Patient"
    )

    if search_name:

        df = df[
            df["name"]
            .str.contains(
                search_name,
                case=False
            )
        ]

    disease_filter = st.selectbox(

        "Filter Disease",

        [
            "All",
            "Heart Disease",
            "Diabetes"
        ]
    )

    if disease_filter != "All":

        df = df[
            df["disease"]
            == disease_filter
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(

        "Download CSV",

        df.to_csv(
            index=False
        ),

        "patient_history.csv",

        "text/csv"
    )