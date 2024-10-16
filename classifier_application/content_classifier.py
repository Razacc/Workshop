from transformers import pipeline
import pandas as pd

def load_inappropriate_content_model():
    """Load a pre-trained model for inappropriate content classification."""
    classifier = pipeline('text-classification', model='Hate-speech-CNERG/dehatebert-mono-english')
    return classifier

def classify_inappropriate_content(classifier, text):
    """Classify text for inappropriate content using the model."""
    result = classifier(text)[0]
    
    label_mapping = {
        'HATE': 1,        
        'NON_HATE': 0    
    }
    
    return label_mapping.get(result['label'], -1)

def apply_classification(dataset):
    """Classify the dataset and flag inappropriate content."""
    classifier = load_inappropriate_content_model()
    dataset['clean_text'] = dataset['clean_text'].fillna("").astype(str)
    dataset['label'] = dataset['clean_text'].apply(lambda text: classify_inappropriate_content(classifier, text))

    return dataset
