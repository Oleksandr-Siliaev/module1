import string

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

def count_sentences(filename):
    with open(filename, 'r') as file:
        text = file.read()
        count = 0
        for char in text:
            if char in ['.', '!', '?']:
                count += 1
        return count

def main():
    filename = input("Введіть назву файлу: ")
    num_words = count_words(filename)
    num_sentences = count_sentences(filename)
    print("Кількість слів: ", num_words)
    print("Кількість речень: ", num_sentences)

if __name__ == '__main__':
    main()
import unittest
import os

class TestCountFunctions(unittest.TestCase):

    def test_count_words(self):
        filename = 'test_file.txt'
        with open(filename, 'w') as file:
            file.write("Це тестовий файл. В ньому повинно бути дев'ять слів.")
        self.assertEqual(count_words(filename), 9)
        os.remove(filename)

    def test_count_sentences(self):
        filename = 'test_file.txt'
        with open(filename, 'w') as file:
            file.write("Це тестовий файл. В ньому повинно бути два речення.")
        self.assertEqual(count_sentences(filename), 2)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
