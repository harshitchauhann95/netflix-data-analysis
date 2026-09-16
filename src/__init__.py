"""
Netflix Data Analysis Package
"""

from .data_loader import load_raw_data, load_processed_data
from .cleaning import clean_netflix_data, build_recommendation_vectors
from .visualize import (
    plot_content_distribution,
    plot_release_year_trends,
    plot_top_countries,
    plot_rating_distribution,
    plot_top_genres
)

__all__ = [
    "load_raw_data",
    "load_processed_data",
    "clean_netflix_data",
    "build_recommendation_vectors",
    "plot_content_distribution",
    "plot_release_year_trends",
    "plot_top_countries",
    "plot_rating_distribution",
    "plot_top_genres",
]
