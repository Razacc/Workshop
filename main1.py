from cleaner.dataset_loader import load_social_media_dataset
from cleaner.text_cleaner import apply_cleaning
from cleaner.utils import merge_and_save_dataset

def main():
    dataset = load_social_media_dataset('tweet_eval', 'sentiment')
    cleaned_dataset = apply_cleaning(dataset)
    merge_and_save_dataset(cleaned_dataset)

if __name__ == "__main__":
    main()