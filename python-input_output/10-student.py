#!/usr/bin/python3
"""Student class with to_json method"""

class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        filtered = {}
        for key in attrs:
            if hasattr(self, key):
                filtered[key] = getattr(self, key)
        return filtered
#!/usr/bin/python3
"""Student class with to_json method"""

class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """attributes"""
        if attrs is None:
            return self.__dict__.copy()

        filtered = {}
        for key in attrs:
            if hasattr(self, key):
                filtered[key] = getattr(self, key)
        return filtered

