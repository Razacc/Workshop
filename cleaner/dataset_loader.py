from datasets import load_dataset

def load_social_media_dataset(dataset_name: str, subset_name: str):
    """Loads a social media dataset from Hugging Face"""
    dataset = load_dataset(dataset_name, subset_name)
    return dataset
