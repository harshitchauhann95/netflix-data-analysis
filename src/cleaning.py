import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean_netflix_data(df: pd.DataFrame, save_path: str = None) -> pd.DataFrame:
    """Preprocesses raw Netflix dataset, handles missing values, and extracts date/duration features."""
    df_clean = df.copy()

    # 1. Fill missing values in large categorical text columns with 'Unknown'
    df_clean['director'] = df_clean['director'].fillna('Unknown')
    df_clean['cast'] = df_clean['cast'].fillna('Unknown')
    df_clean['country'] = df_clean['country'].fillna('Unknown')

    # 2. Drop rows missing critical structural values
    df_clean = df_clean.dropna(subset=['date_added', 'rating', 'duration']).reset_index(drop=True)

    # 3. Clean date_added and convert to datetime format
    df_clean['date_added'] = pd.to_datetime(df_clean['date_added'].astype(str).str.strip(), errors='coerce')

    # 4. Feature engineering: Extract year and month added
    df_clean['year_added'] = df_clean['date_added'].dt.year
    df_clean['month_added'] = df_clean['date_added'].dt.month_name()

    # 5. Extract duration numeric value and unit
    df_clean['duration_num'] = df_clean['duration'].astype(str).str.extract(r'(\d+)').astype(float)
    df_clean['duration_unit'] = df_clean['duration'].astype(str).apply(
        lambda x: 'Season' if 'Season' in x else ('min' if 'min' in x else 'Other')
    )

    # 6. Title clean for search indexing
    df_clean['title_clean'] = df_clean['title'].astype(str).str.strip().str.lower()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df_clean.to_csv(save_path, index=False)
        print(f"Cleaned dataset saved successfully to {save_path}")

    return df_clean

def build_recommendation_vectors(df: pd.DataFrame):
    """Encodes categorical features for vector similarity matching engine."""
    feature_cols = ['type', 'rating', 'listed_in', 'country']
    encoded_df = df.copy()

    for col in feature_cols:
        le = LabelEncoder()
        encoded_df[col] = le.fit_transform(encoded_df[col].astype(str))

    return df, encoded_df, feature_cols

if __name__ == "__main__":
    from .data_loader import load_raw_data
    df_raw = load_raw_data()
    df_clean = clean_netflix_data(df_raw)
    print("Cleaned data summary:")
    print(df_clean.info())
