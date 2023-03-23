from cleaning import clean_text
from splitting import split_text

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    global total_words
    global part_count

    # Clean the text by removing unwanted characters
    filtered_text = clean_text(message.text)

    # Split the text into parts of at most 500 words each
    parts = split_text(filtered_text)

    # Update total word count
    total_words += len(parts)

    # Update part count
    part_count += len(parts)

    # Send the parts as separate messages
    for part in parts:
        bot.reply_to(message, part)
