def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))  # This will print the number of words

main()