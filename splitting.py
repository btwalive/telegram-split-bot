import math

def split_text(text):
    # Split the text into parts of at most 500 words each
    words = text.split()
    num_words = len(words)
    max_words_per_part = 500
    num_parts = math.ceil(num_words / max_words_per_part)
    parts = []
    
    for i in range(num_parts):
        part_start = i * max_words_per_part
        part_end = min((i + 1) * max_words_per_part, num_words)
        part_text = ' '.join(words[part_start:part_end])
        parts.append(part_text)
        
    return parts
