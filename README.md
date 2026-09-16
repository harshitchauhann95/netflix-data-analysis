<div align="center">

# 🎬 Netflix Data Analysis

### Exploratory Data Analysis, Visualization & Recommendation Engine for Netflix's Global Catalog

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/harshitchauhann95/netflix-data-analysis?style=for-the-badge)](https://github.com/harshitchauhann95/netflix-data-analysis/commits/main)
[![Stars](https://img.shields.io/github/stars/harshitchauhann95/netflix-data-analysis?style=for-the-badge)](https://github.com/harshitchauhann95/netflix-data-analysis/stargazers)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Insights](#-key-insights)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Methodology](#-methodology)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🧭 Overview

**Netflix Data Analysis** is an end-to-end exploratory data analysis (EDA) and machine learning vector matching project that dives into Netflix's global content catalog to uncover patterns in content type, genre distribution, regional production, ratings, and growth over time.

The goal is to answer questions like:

- 📈 How has Netflix's content library grown year over year?
- 🎭 Which genres and content types dominate the platform?
- 🌍 Which countries produce the most Netflix content?
- 🔞 How is content distributed across maturity ratings?
- 🍿 How can vector space distance match similar titles in an interactive web application?

---

## 💡 Key Insights

| Metric | Insight |
|---|---|
| 🎬 Content Split | 69.69% Movies / 30.31% TV Shows |
| 📅 Peak Growth Year | Content additions peaked between 2018–2020 |
| 🌎 Top Country | United States (followed by India & United Kingdom) |
| 🔞 Most Common Rating | TV-MA (Adults) & TV-14 |
| ⚡ Search Engine | Euclidean Distance Vector Space in Streamlit App |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **Data Handling** | Pandas, NumPy, Scikit-Learn |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Web Framework** | Streamlit |
| **Environment** | Jupyter Notebook |
| **Version Control** | Git & GitHub |

</div>

---

## 📂 Project Structure

```
netflix-data-analysis/
├── assets/                # Logo, images, demo screenshots
├── data/
│   ├── raw/                # Original unmodified dataset(s) (netflix_titles.csv)
│   └── processed/          # Cleaned & transformed data (netflix_cleaned.csv)
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_visualization.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── cleaning.py
│   └── visualize.py
├── visuals/                # Exported charts/plots (.png)
├── app.py                 # Interactive Streamlit Recommendation Engine
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📁 Dataset

- **Source:** [Kaggle – Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Format:** CSV (`data/raw/netflix_titles.csv`)
- **Size:** ~8,807 rows × 12 columns
- **Fields include:** `title`, `type`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in` (genres), `description`

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone git@github.com:harshitchauhann95/netflix-data-analysis.git
cd netflix-data-analysis
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🚀 Run Interactive Streamlit Web App
Launch the Netflix Match Engine recommendation app locally:
```bash
streamlit run app.py
```

### 📓 Interactive Jupyter Notebooks
Launch Jupyter and run notebooks in sequence:
```bash
jupyter notebook notebooks/
```

### 🛠️ Python Source Modules
Execute modular pipeline scripts directly:
```bash
python3 -m src.data_loader
python3 -m src.cleaning
```

---

## 🔬 Methodology

1. **Data Cleaning** — Handle missing values, standardize date formats, extract temporal features (`year_added`, `month_added`), and split multi-value fields.
2. **Exploratory Analysis** — Aggregate and profile the data across content type, year, country, rating, and genre.
3. **Visualization** — Export high-resolution Seaborn and Matplotlib figures to `visuals/`.
4. **Recommendation Engine** — Encode categorical attributes (`type`, `rating`, `listed_in`, `country`) into numerical vector space for Euclidean distance similarity retrieval.

---

## 🗺️ Roadmap

- [x] Clean and preprocess raw dataset
- [x] Reorganize repository into standard data science modular layout
- [x] Perform full exploratory data analysis & export charts
- [x] Build interactive Streamlit recommendation dashboard
- [ ] Add NLP sentiment & TF-IDF similarity on title descriptions
- [ ] Deploy Streamlit Community Cloud dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

<div align="center">

**Harshit Chauhan**

[![GitHub](https://img.shields.io/badge/GitHub-harshitchauhann95-181717?style=for-the-badge&logo=github)](https://github.com/harshitchauhann95)

⭐ If you found this project useful, consider giving it a star!

</div>
