import re

def clean_text(text: str) -> str:
    """Clean the given text from URLs, mentions, hashtags, and special characters."""
    text = re.sub(r'http\S+|@\S+|#\S+', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return text.strip()

def apply_cleaning(dataset):
    """Apply text cleaning to the dataset."""
    dataset = dataset.map(lambda x: {'clean_text': clean_text(x['text'])})
    return dataset