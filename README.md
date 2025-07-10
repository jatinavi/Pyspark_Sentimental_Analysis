

````markdown
# YouTube Sentiment Analysis

Fetches comments from any public YouTube video, processes them with PySpark, applies VADER sentiment analysis, and visualizes results.

---

## Description

This tool extracts comments using the YouTube Data API v3, loads them into a PySpark DataFrame, labels each comment as **Positive**, **Neutral**, or **Negative** via VADER, and outputs both CSV files and charts for easy insights.

---

## Features

- 🚀 **Comment Extraction**: Fetches up to 100 public comments per video  
- ⚙️ **Scalable Processing**: Leverages PySpark for big‑data handling  
- 📝 **Sentiment Classification**: Uses VADER for accurate NLP scoring  
- 📊 **Visualization**: Generates pie and bar charts of sentiment distribution  
- 💾 **CSV Output**: Raw (`data/comments.csv`) and labeled (`output/sentiment_output.csv`) data  

---

## Prerequisites

- Python 3.8+  
- Java 8+ (for Spark)  
- YouTube Data API v3 key  

---

## Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/youtube-sentiment-analysis.git
   cd youtube-sentiment-analysis
````

2. **Create virtual environment & install**

   ```bash
   python -m venv yt_env
   source yt_env/bin/activate      # Windows: yt_env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API Key**

   ```bash
   cp key.json.example key.json
   # Edit key.json with your API_KEY
   ```

4. **Prepare directories**

   ```bash
   mkdir -p data output
   ```

---

## Usage

* **Fetch comments**

  ```bash
  python fetch_comments.py
  ```

  Paste any YouTube video URL when prompted.

* **Run sentiment analysis**

  ```bash
  python sentiment_analysis.py
  ```

  Produces `output/sentiment_output.csv` and displays sentiment charts.

---

## File Structure

```
youtube-sentiment-analysis/
├── .gitignore
├── README.md
├── requirements.txt
├── key.json.example
├── fetch_comments.py
├── sentiment_analysis.py
├── data/                # Raw comments (gitignored)
└── output/              # Results & charts (gitignored)
```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## License

MIT © Jatin Kumar Balchandani

```
```
