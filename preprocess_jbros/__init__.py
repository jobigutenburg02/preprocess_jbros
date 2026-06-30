# entry level code and import text preprocess methods

from .text_preprocess import *

# General feature extraction
def extract_features(x):
    return {
        'word_count': word_count(x),
        'char_count': char_count(x),
        'avg_word_len': avg_word_len(x),
        'stop_words_count': stop_words_count(x),
        'hashtags_count': hashtags_count(x),
        'mentions_count': mentions_count(x),
        'numerics_count': numerics_count(x),
        'upper_case_count': upper_case_count(x),
    }

# Cleaning text
def clean_text(x):
    x = to_lower_case(x)
    x = contraction_to_expansion(x)
    x = remove_emails(x)
    x = remove_urls(x)
    x = remove_html_tags(x)
    x = remove_special_chars(x)
    x = lemmatize(x)
    return x