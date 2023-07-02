# Compensation exercise

# 1 calc_average

def calc_average(numbers: list) -> float:
    sum_of_nums = 0
    count = 0

    for number in numbers:
        if not type(number) is int or not float:
            raise ValueError("Invalid value in the list")
        sum_of_nums += number
        count += 1

    return sum_of_nums/count


try:
    numbers = [6, 5, 10]
    average = calc_average(numbers)
    print(average)

except ValueError as v:
    print(v)

# 2


def print_pyramid(rows: int):
    if not type(rows) is int:
        raise ValueError("Invalid value for rows")
    for i in range(1, rows + 1):
        print(" " * (rows-i) + "*" * (2*i-1))


print(print_pyramid(5))


# 3

import re


def clean_string(my_string: str) -> str:
    cleaned_string = re.sub(r"[^a-zA-Z\s]", "", my_string)
    return cleaned_string


my_string = input("Enter a string:")
cleaned_string = clean_string(my_string)
print(cleaned_string)

# 4


def count_special_char(my_string: str) -> str:
    special_char = 0
    for i in range(0, len(my_string)):
        ch = my_string[i]
        if my_string[i].isalpha():
            continue
        else:
            special_char += 1

    return special_char


my_string = input("Enter a sentence: ")
special_char = count_special_char(my_string)
print(special_char)

# 5


def dict_to_list(dictionary: dict) -> list:
    dict_list = list(dictionary.values())
    return dict_list


dictionary = {"name": "Eveline", "age": "41"}
dict_list = dict_to_list(dictionary)
print(dict_list)

# 6


def list_to_dict(key_list, value_list: list) -> dict:
    if len(key_list) == len(value_list):
        new_dict = dict(zip(key_list, value_list))
        return new_dict
    else:
        return ValueError("Lists must be of the same length.")


key_list = ["Anna", "Maria", "Inna"]
value_list = ["5", "6", "7"]
new_dict = list_to_dict(key_list, value_list)
print(new_dict)

# 7


def chunk_list(my_list: list, chunks: int) -> list:
    if len(my_list) < 1:
        raise ValueError("List must not be empty.")
    elif len(my_list) % chunks != 0:
        raise ValueError("List length must be divisible by chunk size")
    else:
        chunk_size = len(my_list) // chunks
        chunked_list = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
        return chunked_list


my_list = [5, 6]
chunks = 2
chunked_list = chunk_list(my_list, chunks)
print(chunked_list)

# 8


class Book:
    def __init__(self, name, author, genre, borrowed=False):
        self.name = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

    def __str__(self):
        return f"{self.name}, {self.author}, {self.borrowed}"


my_book1 = Book("Romeo and Juliet", "Shakespeare", "tragedy")
print(my_book1)


# 9

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.book_list.append(book)

    def get_all_books(self):
        return self.book_list

    def borrow_book(self, book):
        if isinstance(book, Book):
            if book in self.book_list and book.borrowed is True:
                print("Book is already borrowed")
            elif book.borrowed is False:
                book.borrowed = True
            else:
                print("Book does not exist")

    def return_book(self, book):
        if isinstance(book, Book):
            if book in self.book_list:
                if book.borrowed is False:
                    print("Book has not been borrowed")
                elif book.borrowed is True:
                    book.borrowed = False
            else:
                print("Book does not exist")


my_book2 = Book("The Hobbit", "J.R.R. Tolkien", "fantasy")
my_library = Library()
my_library.add_book(my_book1)
my_library.add_book(my_book2)

print(my_book2)

# 10


class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        if isinstance(book, Book):
            return self.stack.append(my_book1)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty.")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# 11

def count_words(file_path: str):
    with open(file_path, "r") as file:
        words = file.read()
        word_count = len(words.split())
        return word_count


file_path = "C:/Users/roxan/Desktop/pythontextfiles/Pythonexercise.txt"
word_count = count_words(file_path)
print(word_count)


# 12


def count_lines(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        return line_count


file_path = "C:/Users/roxan/Desktop/pythontextfiles/Pythonexercise.txt"
line_count = count_lines(file_path)
print(line_count)

# 13

create_file = open("linecount.txt", "w")
linecount = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5", "Line 6"]
create_file.write(" " "\n".join(linecount))
create_file.close()


def write_even(input_file_path: str, output_file_path):
    with open(input_file_path, 'r') as i_file, open(output_file_path, "w") as o_file:
        lines = i_file.readlines()
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:
                o_file.write(f"{line.strip()}\n")


input_file_path = "linecount.txt"
output_file_path = "even_count.txt"
write_even(input_file_path, output_file_path)
