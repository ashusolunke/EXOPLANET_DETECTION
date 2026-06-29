import joblib
import pandas as pd

# Load trained model and label encoder
model = joblib.load("model/model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")


def preprocess_data(df):
    """
    Convert TOI dataset columns to the same format used for training.
    """

    df = df[
        [
            "pl_orbper",
            "pl_trandurh",
            "pl_trandep",
            "pl_rade",
            "pl_insol",
            "pl_eqt"
        ]
    ].copy()

    df.columns = [
        "koi_period",
        "koi_duration",
        "koi_depth",
        "koi_prad",
        "koi_insol",
        "koi_teq"
    ]

    df = df.dropna()

    return df


def predict(df):
    processed = preprocess_data(df)

    prediction = model.predict(processed)

    confidence = model.predict_proba(processed).max(axis=1)

    labels = label_encoder.inverse_transform(prediction)

    processed["Prediction"] = labels
    processed["Confidence"] = confidence * 100

    return processed