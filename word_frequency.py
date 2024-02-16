# word_frequency.py

def read_input_file(filename):
    """Read input text from a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def compute_word_frequencies(text):
    """Compute word frequencies."""
    words = text.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def sort_frequencies_alphabetically(frequencies):
    """Sort the frequencies alphabetically."""
    return sorted(frequencies.items(), key=lambda x: x[0])
