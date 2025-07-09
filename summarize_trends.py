# 🧠 Summarize fashion articles using Hugging Face + LangChain (latest API)
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

def summarize_with_hf(articles):
    # Load Hugging Face summarization model (local or from HF Hub)
    summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
    max_length=320,
    min_length=100,
    truncation=True
)


    # Wrap it for LangChain usage
    hf_pipeline = HuggingFacePipeline(pipeline=summarizer)

    # Define the summarization prompt
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize this fashion article:\n\n{text}"
    )

    # Combine prompt + model using RunnableSequence (LangChain 0.1.17+)
    summarization_chain = RunnableSequence(prompt | hf_pipeline)

    summaries = []
    for article in articles:
        try:
            result = summarization_chain.invoke({"text": article["text"]})
            summaries.append({
                "title": article["title"],
                "summary": result
            })
        except Exception as e:
            print(f"❌ Failed to summarize {article['title']}: {e}")

    return summaries
