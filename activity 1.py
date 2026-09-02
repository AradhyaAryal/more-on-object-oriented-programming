class IOString:
        def __init__(self):
            self.str = ""
        def get_String(self):
            self.str = input("Enter a string: ")
        def print_String(self):
            print("Result is", self.str.upper())
str1 = IOString()

str1.get_String()
str1.print_String()