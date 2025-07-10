# 🚀 YouTube Sentiment Analysis

![PySpark](https://img.shields.io/badge/PySpark-3.5.0-blue) ![VADER](https://img.shields.io/badge/VADER-NLP-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

A complete end‑to‑end pipeline that **fetches YouTube comments**, **processes them at scale** with PySpark, **applies VADER sentiment analysis**, and **visualizes insights** in charts and CSVs. Perfect for learning big‑data NLP workflows or building your own analytics dashboard!

---

## 🔎 Table of Contents

1. [🌟 Features](#-features)  
2. [🛠️ Tech Stack](#️️-tech-stack)  
3. [⚙️ Prerequisites](#️⚙️-prerequisites)  
4. [⚡ Setup & Installation](#️⚡-setup--installation)  
5. [🚀 Usage](#️🚀-usage)  
6. [📂 Project Structure](#️📂-project-structure)  
7. [📈 Example Output](#️📈-example-output)  
8. [🔧 Configuration & Best Practices](#️🔧-configuration--best-practices)  
9. [🔮 Future Enhancements](#️🔮-future-enhancements)  
10. [📝 License](#️📝-license)  
11. [✉️ Contact](#️✉️-contact)

---

## 🌟 Features

- **Comment Extraction**  
  - Fetch up to 100 top‑level public comments from any YouTube video via Data API v3  
- **Scalable Processing**  
  - Leverage PySpark DataFrames for fast, distributed ETL  
- **Sentiment Classification**  
  - Apply VADER to label comments as **Positive**, **Neutral**, or **Negative**  
- **CSV Outputs**  
  - Raw comments (`data/comments.csv`) & labeled results (`output/sentiment_output.csv`)  
- **Visualization**  
  - Auto‑generated pie & bar charts for sentiment distribution  
- **Easy Deployment**  
  - Containerize with Docker or integrate into CI/CD pipelines  

---

## 🛠️ Tech Stack

| Component                    | Purpose                               |
|------------------------------|---------------------------------------|
| Python 3.8+                  | Core language                        |
| PySpark                      | Distributed data processing          |
| YouTube Data API v3          | Comment extraction                   |
| VADER (NLTK)                 | Sentiment scoring                    |
| pandas                       | Lightweight DataFrame manipulations  |
| matplotlib                   | Charting library                     |
| python-dotenv                | Environment variable management      |
| Git & GitHub                 | Version control & repository hosting |
| (Optional) Flask / Streamlit | Build a web dashboard                |

---

## ⚙️ Prerequisites

1. **Python** ≥ 3.8  
2. **Java** 8+ (for Spark)  
3. **Apache Spark** installed or accessible  
4. **YouTube Data API v3 key** (public data access)  

---

## ⚡ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/youtube-sentiment-analysis.git
cd youtube-sentiment-analysis

# 2. Create & activate virtual environment
python -m venv yt_env
source yt_env/bin/activate      # Windows: yt_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API key
cp key.json.example key.json
# → Edit key.json, inserting your YouTube API_KEY

# 5. Prepare data directories
mkdir -p data output
