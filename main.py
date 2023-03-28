import string

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)


def main():
    filename = input("Введіть назву файлу: ")
    num_words = count_words(filename)
    print("Кількість слів: ", num_words)

if __name__ == '__main__':
    main()

