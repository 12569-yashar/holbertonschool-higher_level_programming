#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
    data = f.read()
    for i in data:
        print(i, end="")
