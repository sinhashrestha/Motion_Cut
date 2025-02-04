def count_words(text):
    """
    Count the number of words in the given text.
    Parameters:
    text (str): The input text to process.
    Returns:
    int: Number of words in the input text.
    """
    words = text.strip().split()
    return len(words)
def main():
    """
    Main function to handle user input and display the word count.
    """
    print("Welcome to the Word Counter Program!")
    print("Please enter a sentence or paragraph to count the words.")
    user_input = input("Enter your text: ").strip()
    if not user_input:
        print("Error: You must enter some text to count the words.")
        return
    word_count = count_words(user_input)
    print("\nProcessing your input...")
    print(f"The total word count is: {word_count}\n")
    if word_count == 1:
        print("You entered only one word.")
    else:
        print(f"That's a total of {word_count} words!")
    print("Thank you for using the Word Counter Program!")
if __name__ == "_main_":
    main()