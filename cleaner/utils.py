import re
from datasets import concatenate_datasets

def remove_special_characters(text: str) -> str:
    """Removes special characters from the text."""
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

def remove_urls_and_mentions(text: str) -> str:
    """Removes URLs and social media mentions from the text."""
    return re.sub(r'http\S+|@\S+|#\S+', '', text)

def merge_and_save_dataset(dataset_dict, filename="content.csv"):
    """Merge all splits of the dataset and save to a single CSV."""
    merged_dataset = concatenate_datasets([dataset for dataset in dataset_dict.values()])
    merged_dataset.to_csv(filename)
    print(f"Saved merged dataset to {filename}")

