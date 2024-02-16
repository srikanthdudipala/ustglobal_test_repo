# main.py

from word_frequency import  compute_word_frequencies, sort_frequencies_alphabetically
from circular_queue import CircularQueue
from password_validation import validate_passwords

def main():
    # Program 1: Word Frequency
    text = "which is better python 2 or python 3"
    if text:
        frequencies = compute_word_frequencies(text)
        sorted_frequencies = sort_frequencies_alphabetically(frequencies)
        print("Word Frequencies:")
        for word, frequency in sorted_frequencies:
            print(f"('{word}', {frequency})")

    # Program 2: Circular Queue
    print("\nCircular Queue:")
    queue = CircularQueue(max_length=5)
    for i in range(7):
        queue.enqueue(i)
        queue.display()

    # Program 3: Password Validation
    print("\nPassword Validation:")
    passwords = ["asqwr1234@1", "aF145#", "2w3E*", "2We3345"]
    valid_passwords = validate_passwords(passwords)
    print(", ".join(valid_passwords))

if __name__ == "__main__":
    main()
