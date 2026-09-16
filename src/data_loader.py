import os
import pandas as pd

def get_project_root() -> str:
    """Returns the absolute path to the project root directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(current_dir, ".."))

def load_raw_data(filepath: str = None) -> pd.DataFrame:
    """Loads the raw Netflix titles dataset from data/raw/netflix_titles.csv."""
    if filepath is None:
        root_dir = get_project_root()
        filepath = os.path.join(root_dir, "data", "raw", "netflix_titles.csv")
    
    if not os.path.exists(filepath):
        # Fallback search if path was relative to execution directory
        if os.path.exists("netflix_titles.csv"):
            filepath = "netflix_titles.csv"
        elif os.path.exists(os.path.join("..", "data", "raw", "netflix_titles.csv")):
            filepath = os.path.join("..", "data", "raw", "netflix_titles.csv")
            
    df = pd.read_csv(filepath)
    print(f"Loaded raw dataset from {filepath} with shape: {df.shape}")
    return df

def load_processed_data(filepath: str = None) -> pd.DataFrame:
    """Loads the cleaned Netflix dataset from data/processed/netflix_cleaned.csv."""
    if filepath is None:
        root_dir = get_project_root()
        filepath = os.path.join(root_dir, "data", "processed", "netflix_cleaned.csv")
        
    if not os.path.exists(filepath):
        print(f"Processed file not found at {filepath}. Loading & cleaning raw dataset...")
        from .cleaning import clean_netflix_data
        df_raw = load_raw_data()
        df_cleaned = clean_netflix_data(df_raw, save_path=filepath)
        return df_cleaned
        
    df = pd.read_csv(filepath)
    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    print(f"Loaded processed dataset from {filepath} with shape: {df.shape}")
    return df

if __name__ == "__main__":
    df = load_raw_data()
    print(df.head())
