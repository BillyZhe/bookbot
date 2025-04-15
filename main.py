def main():
    count = 0
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        words = file_contents.split()
        for num in words:
            count += 1
    print(f"{count} words found in the document")
main()
