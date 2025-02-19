def count_words(text):
    words = text.split()
    return len(words)
def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)
main()def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))  # This will print the number of words

main()
