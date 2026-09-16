import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set default aesthetic theme
sns.set_theme(style="whitegrid")
NETFLIX_RED = '#E50914'
CHARCOAL = '#221F1F'
ACCENT_GRAY = '#564D4D'

def _save_or_show(fig, save_path: str = None):
    """Utility function to save plot to disk or show inline."""
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path, bbox_inches='tight', dpi=300)
        print(f"Plot saved to {save_path}")
    else:
        plt.show()
    plt.close(fig)

def plot_content_distribution(df: pd.DataFrame, save_path: str = None):
    """Plots Movie vs TV Show ratio in the dataset."""
    type_counts = df['type'].value_counts()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = [NETFLIX_RED, CHARCOAL]
    
    sns.barplot(x=type_counts.index, y=type_counts.values, hue=type_counts.index, palette=colors, legend=False, ax=ax)
    ax.set_title("Netflix Content Distribution: Movies vs TV Shows", fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel("Count of Titles", fontsize=12)
    ax.set_xlabel("Content Type", fontsize=12)
    
    total = len(df)
    for p in ax.patches:
        height = p.get_height()
        percentage = (height / total) * 100
        ax.annotate(f'{int(height)}\n({percentage:.1f}%)',
                    (p.get_x() + p.get_width() / 2., height / 2),
                    ha='center', va='center', fontsize=11, color='white', fontweight='bold')
                    
    _save_or_show(fig, save_path)

def plot_release_year_trends(df: pd.DataFrame, save_path: str = None):
    """Plots cumulative title release trends over recent decades."""
    recent_df = df[df['release_year'] >= 2000]
    yearly_counts = recent_df.groupby(['release_year', 'type']).size().reset_index(name='count')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=yearly_counts, x='release_year', y='count', hue='type',
                 palette=[NETFLIX_RED, CHARCOAL], linewidth=2.5, marker='o', ax=ax)
                 
    ax.set_title("Growth of Content Releases (2000 - Present)", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Release Year", fontsize=12)
    ax.set_ylabel("Number of Titles Released", fontsize=12)
    ax.legend(title="Type", frameon=True)
    
    _save_or_show(fig, save_path)

def plot_top_countries(df: pd.DataFrame, top_n: int = 10, save_path: str = None):
    """Plots the top N content producing countries."""
    # Split countries if multiple comma-separated
    countries_series = df['country'].dropna().apply(lambda x: [c.strip() for c in str(x).split(',') if c.strip() != 'Unknown'])
    flat_countries = pd.Series([country for sublist in countries_series for country in sublist])
    top_countries = flat_countries.value_counts().head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, color=NETFLIX_RED, ax=ax)
    
    ax.set_title(f"Top {top_n} Content Producing Countries on Netflix", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Total Titles", fontsize=12)
    ax.set_ylabel("Country", fontsize=12)
    
    for i, count in enumerate(top_countries.values):
        ax.text(count + max(top_countries.values)*0.01, i, f'{count}', va='center', fontsize=10, fontweight='bold')
        
    _save_or_show(fig, save_path)

def plot_rating_distribution(df: pd.DataFrame, save_path: str = None):
    """Plots distribution of maturity ratings across Movies and TV Shows."""
    fig, ax = plt.subplots(figsize=(12, 6))
    rating_order = df['rating'].value_counts().index
    
    sns.countplot(data=df, x='rating', hue='type', order=rating_order,
                  palette=[NETFLIX_RED, CHARCOAL], ax=ax)
                  
    ax.set_title("Content Distribution by Maturity Rating", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Rating", fontsize=12)
    ax.set_ylabel("Count of Titles", fontsize=12)
    plt.xticks(rotation=45)
    ax.legend(title="Type", frameon=True)
    
    _save_or_show(fig, save_path)

def plot_top_genres(df: pd.DataFrame, top_n: int = 10, save_path: str = None):
    """Plots top N genres across the catalog."""
    genres_series = df['listed_in'].dropna().apply(lambda x: [g.strip() for g in str(x).split(',')])
    flat_genres = pd.Series([genre for sublist in genres_series for genre in sublist])
    top_genres = flat_genres.value_counts().head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_genres.values, y=top_genres.index, color=CHARCOAL, ax=ax)
    
    ax.set_title(f"Top {top_n} Genres on Netflix", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Count of Titles", fontsize=12)
    ax.set_ylabel("Genre", fontsize=12)
    
    for i, count in enumerate(top_genres.values):
        ax.text(count + max(top_genres.values)*0.01, i, f'{count}', va='center', fontsize=10, fontweight='bold')
        
    _save_or_show(fig, save_path)
