# 🖥️ Streamlit dashboard: runs full trend insight pipeline
import streamlit as st
from scrape_articles import fetch_articles
from summarize_trends import summarize_with_hf
from upload_to_s3 import upload_to_s3

# List of article URLs to scrape
urls = [
    "https://www.elle.com/",
    "https://www.vogue.com/",
    "https://10magazine.com/",
    "https://clichemag.com/",
    "https://fashionmagazine.com/"
]

st.set_page_config(page_title="Fashion Trend Insights", layout="wide")
st.title("👗 AI-Powered Fashion Trend Insights")
st.write("This tool scrapes fashion trend articles, stores them in S3, and summarizes using AI.")

# Trigger full pipeline
if st.button("Fetch & Analyze Trends"):
    st.info("🔄 Fetching articles...")
    articles = fetch_articles(urls)

    st.info("☁️ Uploading raw data to S3...")
    upload_to_s3(articles, "raw_data/fashion_articles.json")

    st.info("🧠 Summarizing with Hugging Face model...")
    summaries = summarize_with_hf(articles)

    st.success("✅ Done! Fashion insights below:")
    for item in summaries:
        st.subheader(item["title"])
        st.write(item["summary"])
