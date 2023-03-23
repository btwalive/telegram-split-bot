import string

# Set of characters to remove
to_remove = set(string.digits + string.punctuation)

def clean_text(text):
    # Remove unwanted characters from the text
    filtered_text = ''.join(char for char in text if char not in to_remove)
    
    # Remove extra whitespace
    filtered_text = ' '.join(filtered_text.split())
    
    # Add full stop at end of sentence
    if filtered_text[-1] not in ['.', '!', '?']:
        filtered_text += "."
        
    return filtered_text
