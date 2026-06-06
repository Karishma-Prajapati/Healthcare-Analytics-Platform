from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import pandas as pd


def evaluate_model(
    model,
    X_test,
    y_test
):

    pred = model.predict(X_test)

    results = {

        "Accuracy":
        accuracy_score(
            y_test,
            pred
        ),

        "Precision":
        precision_score(
            y_test,
            pred
        ),

        "Recall":
        recall_score(
            y_test,
            pred
        ),

        "F1 Score":
        f1_score(
            y_test,
            pred
        )
    }

    cm = confusion_matrix(
        y_test,
        pred
    )

    return results, cm


def feature_importance(
    model,
    feature_names
):

    importance = pd.DataFrame({

        "Feature":
        feature_names,

        "Importance":
        model.feature_importances_

    })

    return importance.sort_values(
        by="Importance",
        ascending=False
    )