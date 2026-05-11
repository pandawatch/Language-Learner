"""
German Vocabulary - Sample Data

This module contains sample German vocabulary data that gets loaded into the database
on first run. Extended vocabulary list can be added here or in a separate data file.
"""

GERMAN_VOCABULARY = [
    # Greetings
    {"german": "Hallo", "english": "Hello", "pronunciation": "HAH-lo", "part_of_speech": "interjection", "difficulty": 1, "category": "greetings"},
    {"german": "Guten Morgen", "english": "Good morning", "pronunciation": "GOO-ten MOR-gen", "part_of_speech": "phrase", "difficulty": 1, "category": "greetings"},
    {"german": "Guten Abend", "english": "Good evening", "pronunciation": "GOO-ten AH-bent", "part_of_speech": "phrase", "difficulty": 1, "category": "greetings"},
    {"german": "Gute Nacht", "english": "Good night", "pronunciation": "GOO-te NAHKT", "part_of_speech": "phrase", "difficulty": 1, "category": "greetings"},
    
    # Politeness
    {"german": "Danke", "english": "Thank you", "pronunciation": "DAHN-ke", "part_of_speech": "interjection", "difficulty": 1, "category": "politeness"},
    {"german": "Bitte", "english": "Please", "pronunciation": "BIT-te", "part_of_speech": "interjection", "difficulty": 1, "category": "politeness"},
    {"german": "Entschuldigung", "english": "Excuse me/Sorry", "pronunciation": "ent-SHOOL-dee-goong", "part_of_speech": "interjection", "difficulty": 2, "category": "politeness"},
    {"german": "Ja", "english": "Yes", "pronunciation": "yah", "part_of_speech": "adverb", "difficulty": 1, "category": "politeness"},
    {"german": "Nein", "english": "No", "pronunciation": "nine", "part_of_speech": "adverb", "difficulty": 1, "category": "politeness"},
    
    # Numbers
    {"german": "Eins", "english": "One", "pronunciation": "ines", "part_of_speech": "noun", "difficulty": 1, "category": "numbers"},
    {"german": "Zwei", "english": "Two", "pronunciation": "tsvye", "part_of_speech": "noun", "difficulty": 1, "category": "numbers"},
    {"german": "Drei", "english": "Three", "pronunciation": "dry", "part_of_speech": "noun", "difficulty": 1, "category": "numbers"},
    {"german": "Vier", "english": "Four", "pronunciation": "feer", "part_of_speech": "noun", "difficulty": 1, "category": "numbers"},
    {"german": "Fünf", "english": "Five", "pronunciation": "foonf", "part_of_speech": "noun", "difficulty": 1, "category": "numbers"},
    
    # Common nouns
    {"german": "Wasser", "english": "Water", "pronunciation": "VAH-ser", "part_of_speech": "noun", "difficulty": 1, "category": "basics"},
    {"german": "Brot", "english": "Bread", "pronunciation": "broht", "part_of_speech": "noun", "difficulty": 1, "category": "food"},
    {"german": "Milch", "english": "Milk", "pronunciation": "milkh", "part_of_speech": "noun", "difficulty": 1, "category": "food"},
    {"german": "Käse", "english": "Cheese", "pronunciation": "KAY-ze", "part_of_speech": "noun", "difficulty": 2, "category": "food"},
    
    # Animals
    {"german": "Katze", "english": "Cat", "pronunciation": "KAH-tze", "part_of_speech": "noun", "difficulty": 1, "category": "animals"},
    {"german": "Hund", "english": "Dog", "pronunciation": "hoont", "part_of_speech": "noun", "difficulty": 1, "category": "animals"},
    {"german": "Vogel", "english": "Bird", "pronunciation": "FOH-gel", "part_of_speech": "noun", "difficulty": 2, "category": "animals"},
    
    # House/Home
    {"german": "Haus", "english": "House", "pronunciation": "hows", "part_of_speech": "noun", "difficulty": 1, "category": "home"},
    {"german": "Tür", "english": "Door", "pronunciation": "toor", "part_of_speech": "noun", "difficulty": 1, "category": "home"},
    {"german": "Fenster", "english": "Window", "pronunciation": "FEN-ster", "part_of_speech": "noun", "difficulty": 1, "category": "home"},
    {"german": "Bett", "english": "Bed", "pronunciation": "bet", "part_of_speech": "noun", "difficulty": 1, "category": "home"},
]

def get_vocabulary_data():
    """Get the vocabulary data"""
    return GERMAN_VOCABULARY
