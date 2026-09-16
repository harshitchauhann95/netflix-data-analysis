<div align="center">

# 🎬 Netflix Data Analysis

### Exploratory Data Analysis & Visualization of Netflix's Global Content Catalog

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
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
- [Results & Visualizations](#-results--visualizations)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🧭 Overview

**Netflix Data Analysis** is an end-to-end exploratory data analysis (EDA) project that dives into Netflix's global content catalog to uncover patterns in content type, genre distribution, regional production, ratings, and growth over time.

The goal is to answer questions like:

- 📈 How has Netflix's content library grown year over year?
- 🎭 Which genres and content types dominate the platform?
- 🌍 Which countries produce the most Netflix content?
- 🔞 How is content distributed across maturity ratings?
- ⏱️ How has average movie/show duration changed over time?

---

## 💡 Key Insights

| Metric | Insight |
|---|---|
| 🎬 Content Split | _e.g. 70% Movies / 30% TV Shows_ |
| 📅 Peak Growth Year | _e.g. Content additions peaked in 2019_ |
| 🌎 Top Country | _e.g. United States leads content production_ |
| 🔞 Most Common Rating | _e.g. TV-MA is the most frequent rating_ |
| ⏳ Avg. Movie Duration | _e.g. ~99 minutes_ |

> Update this table with your actual findings once analysis is complete.

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Environment** | Jupyter Notebook |
| **Version Control** | Git & GitHub |

</div>

---

## 📂 Project Structure

```
netflix-data-analysis/
├── assets/                # Logo, images, demo screenshots
├── data/
│   ├── raw/                # Original unmodified dataset(s)
│   └── processed/          # Cleaned & transformed data
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_visualization.ipynb
├── src/
│   ├── data_loader.py
│   ├── cleaning.py
│   └── visualize.py
├── visuals/                # Exported charts/plots
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📁 Dataset

- **Source:** [Kaggle – Netflix Movies and TV Shows](https://www.kaggle.com/) _(replace with your actual dataset link)_
- **Format:** CSV
- **Size:** _e.g. ~8,800 rows × 12 columns_
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
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Launch Jupyter and run the notebooks in order:

```bash
jupyter notebook
```

Or run analysis scripts directly:

```bash
python src/data_loader.py
python src/visualize.py
```

---

## 🔬 Methodology

1. **Data Cleaning** — Handle missing values, standardize date formats, split multi-value fields (cast, genres, countries).
2. **Exploratory Analysis** — Aggregate and profile the data across content type, year, country, rating, and genre.
3. **Visualization** — Build charts to communicate trends (line, bar, treemap, heatmap, word clouds).
4. **Insight Extraction** — Summarize key findings and patterns.

---

## 🗺️ Roadmap

- [ ] Clean and preprocess raw dataset
- [ ] Perform full exploratory data analysis
- [ ] Build interactive dashboard (Plotly / Streamlit)
- [ ] Add sentiment analysis on descriptions
- [ ] Deploy dashboard publicly

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Check the [issues page](https://github.com/harshitchauhann95/netflix-data-analysis/issues) for open tasks.

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
