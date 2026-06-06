import streamlit as st
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix
)

from utils.evaluate_models import (
    evaluate_model,
    feature_importance
)

st.title("🤖 Model Performance")

heart = pd.read_csv(
    "datasets/heart.csv"
)

X = heart.drop(
    "target",
    axis=1
)

y = heart["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load(
    "models/heart_model.pkl"
)

scaler = joblib.load(
    "models/heart_scaler.pkl"
)

X_test = scaler.transform(
    X_test
)

results, cm = evaluate_model(
    model,
    X_test,
    y_test
)

st.subheader(
    "Metrics"
)

st.json(results)

st.subheader(
    "Confusion Matrix"
)

st.write(cm)

if hasattr(
    model,
    "feature_importances_"
):

    st.subheader(
        "Feature Importance"
    )

    importance = feature_importance(
        model,
        X.columns
    )

    st.dataframe(
        importance
    )

    st.bar_chart(
        importance.set_index(
            "Feature"
        )
    )