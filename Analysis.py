from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os
os.makedirs("output", exist_ok=True)


# ✅ Start Spark session
spark = SparkSession.builder.appName("YouTubeSentiment").getOrCreate()

# ✅ Load CSV into Spark DataFrame
df = spark.read.csv("/Users/jatinbalchandani/Documents/projects/pysparksentimentalanalysis/data/comments.csv", header=True)

# ✅ Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# ✅ Define function to return sentiment label
def get_sentiment(text):
    if text is None:
        return "Neutral"
    score = analyzer.polarity_scores(text)
    compound = score["compound"]
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# ✅ Convert Python function to Spark UDF
sentiment_udf = udf(get_sentiment, StringType())

# ✅ Apply UDF to DataFrame
df_with_sentiment = df.withColumn("sentiment", sentiment_udf(df["comment"]))

# ✅ Save to CSV
df_with_sentiment.toPandas().to_csv("output/sentiment_output.csv", index=False)
print("✅ Saved sentiment_output.csv")

# ✅ Plot sentiment distribution
sentiment_counts = df_with_sentiment.groupBy("sentiment").count().toPandas()

plt.figure(figsize=(6,6))
plt.pie(sentiment_counts["count"], labels=sentiment_counts["sentiment"], autopct="%1.1f%%")
plt.title("YouTube Comment Sentiment Distribution")
plt.show()
