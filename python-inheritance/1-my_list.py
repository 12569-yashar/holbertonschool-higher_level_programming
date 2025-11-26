#!/usr/bin/python3
"""MyList class definition"""


class MyList(list):
    """Custom list class with a method to print sorted list"""

    def print_sorted(self):
        """Prints the list in sorted order"""
        self.sort()
        print(self)
