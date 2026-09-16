import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Add parent directory to path for modular imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.data_loader import load_processed_data, load_raw_data
from src.cleaning import build_recommendation_vectors, clean_netflix_data

# 1. Page Configuration & Aesthetic Vibe
st.set_page_config(
    page_title="Netflix Match Engine",
    page_icon="🎬",
    layout="wide"
)

# Dark Cinematic Minimalism
st.markdown("""
    <style>
    .main { background-color: #0E0E0E; color: #FFFFFF; }
    h1, h2, h3 { font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 800; color: #E50914 !important; }
    .rec-card {
        background-color: #181818;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #E50914;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    .stTextInput>div>div>input {
        background-color: #1F1F1F !important;
        color: white !important;
        border: 1px solid #333 !important;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Curated Recommendation Processing Engine
@st.cache_resource
def build_engine():
    try:
        df = load_processed_data()
    except Exception:
        raw_df = load_raw_data()
        df = clean_netflix_data(raw_df)

    df, encoded_df, feature_cols = build_recommendation_vectors(df)
    return df, encoded_df, feature_cols

df, encoded_df, feature_cols = build_engine()

# 3. Layout Header
st.title("🎬 NETFLIX RECOMMENDATION ENGINE")
st.markdown("<p style='color:#888; font-size:1.1rem; margin-top:-15px;'>Enter a title below to instantly discover similar content across the global catalog.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Search Form Panel
search_query = st.text_input("🍿 Type the name of a Movie or TV Show:", value="Stranger Things")

if search_query:
    target_clean = search_query.strip().lower()
    match_records = df[df['title_clean'] == target_clean]
    
    if not match_records.empty:
        target_idx = match_records.index[0]
        
        # 1. Pull vectors and explicitly convert them to float matrices
        target_vector = encoded_df.loc[target_idx, feature_cols].values.astype(float)
        all_vectors = encoded_df[feature_cols].values.astype(float)
        
        # 2. Euclidean Vector Space calculation
        distances = np.linalg.norm(all_vectors - target_vector, axis=1)
        
        # Sort indices and filter out the queried item itself
        sorted_indices = np.argsort(distances)
        matched_indices = [idx for idx in sorted_indices if idx != target_idx][:5]
        
        # Retrieve original content records
        recommendations = df.loc[matched_indices]
        
        st.subheader(f"🎯 Top 5 Recommendations for '{search_query}'")
        # Render clean content result list blocks
        for _, row in recommendations.iterrows():
            st.markdown(f"""
            <div class="rec-card">
                <span style="color:#E50914; font-weight:bold; font-size:0.85rem; text-transform:uppercase;">{row['type']}</span>
                <h3 style="margin:5px 0; color:#FFF !important;">{row['title']}</h3>
                <p style="margin:0; color:#AAA; font-size:0.9rem;">
                    <b>Genre:</b> {row['listed_in']} &nbsp;|&nbsp; 
                    <b>Maturity Rating:</b> {row['rating']} &nbsp;|&nbsp; 
                    <b>Country:</b> {row['country']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.error(f"❌ '{search_query}' wasn't found in the current Netflix inventory. Double-check your spelling and try again!")

st.markdown("---")
st.caption("⚡ Clean Vector-Distance Architecture | Harshit Chauhan Portfolio Workspace")