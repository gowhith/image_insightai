# 👗 AI-Powered Fashion Trend Insights

A comprehensive AI application that automatically scrapes fashion trend articles from leading fashion websites, processes them using advanced NLP models, and provides intelligent trend summaries through an interactive Streamlit dashboard.

## 🚀 Features

- **Automated Web Scraping**: Fetches articles from top fashion websites including Elle, Vogue, 10 Magazine, Cliche Magazine, and Fashion Magazine
- **AI-Powered Summarization**: Uses Hugging Face's BART-large-CNN model for intelligent article summarization
- **Cloud Storage**: Automatically uploads raw data to AWS S3 for persistent storage
- **Interactive Dashboard**: Beautiful Streamlit interface for easy trend analysis
- **Real-time Processing**: End-to-end pipeline from scraping to insights in one click

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Web Scraping**: BeautifulSoup4, Requests
- **AI/ML**: Hugging Face Transformers, LangChain
- **Cloud Storage**: AWS S3 (boto3)
- **NLP Model**: facebook/bart-large-cnn (summarization)
- **Environment**: Python virtual environment

## 📋 Prerequisites

- Python 3.7+
- AWS S3 bucket and credentials
- Internet connection for web scraping

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd trend_insight_ai
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   AWS_S3_BUCKET=your-s3-bucket-name
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   AWS_DEFAULT_REGION=your-region
   ```

## 🎯 Usage

### Running the Dashboard

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`
   - Click "Fetch & Analyze Trends" to run the complete pipeline

### Manual Script Execution

You can also run individual components:

- **Scrape articles only**: `python scrape_articles.py`
- **Summarize articles only**: `python summarize_trends.py`
- **Upload to S3 only**: `python upload_to_s3.py`

## 📁 Project Structure

```
trend_insight_ai/
├── app.py                 # Main Streamlit dashboard
├── scrape_articles.py     # Web scraping functionality
├── summarize_trends.py    # AI summarization using Hugging Face
├── upload_to_s3.py       # AWS S3 upload functionality
├── requirments.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Configuration

### AWS S3 Setup

1. Create an S3 bucket in your AWS account
2. Configure AWS credentials in your `.env` file
3. Ensure your AWS user has S3 write permissions

### Customizing Article Sources

Edit the `urls` list in `app.py` to add or remove fashion websites:

```python
urls = [
    "https://www.elle.com/",
    "https://www.vogue.com/",
    "https://10magazine.com/",
    "https://clichemag.com/",
    "https://fashionmagazine.com/",
    # Add your custom URLs here
]
```

## 🤖 AI Model Details

The application uses the **facebook/bart-large-cnn** model for summarization, which:
- Processes articles up to 1024 tokens
- Generates summaries between 100-320 words
- Optimized for news and article summarization
- Runs locally or via Hugging Face Hub

## 📊 Data Flow

1. **Scraping**: Fetches articles from fashion websites using BeautifulSoup
2. **Storage**: Uploads raw article data to S3 bucket
3. **Processing**: Uses BART model to generate intelligent summaries
4. **Display**: Presents insights through Streamlit dashboard

## 🔒 Security & Privacy

- AWS credentials stored in `.env` file (not committed to git)
- User-Agent headers to mimic browser requests
- Error handling for failed requests
- Timeout protection for web scraping

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated
2. **AWS errors**: Verify S3 bucket exists and credentials are correct
3. **Scraping failures**: Some websites may block automated requests
4. **Model loading**: First run may download the BART model (~1.5GB)

### Error Handling

The application includes comprehensive error handling:
- Failed article scraping continues with remaining URLs
- S3 upload failures are logged but don't stop processing
- Model inference errors are caught and reported

## 📈 Future Enhancements

- [ ] Add more fashion websites
- [ ] Implement trend classification
- [ ] Add historical trend tracking
- [ ] Create trend visualization charts
- [ ] Add sentiment analysis
- [ ] Implement real-time notifications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Hugging Face for the BART model
- Streamlit for the web framework
- AWS for cloud storage
- BeautifulSoup for web scraping capabilities

---

**Note**: This application is designed for educational and research purposes. Please respect website terms of service when scraping content. 
