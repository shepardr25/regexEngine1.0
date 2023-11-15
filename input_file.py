# input_file.py
from syntaxChecker import syntaxChecker
from scanner import Scanner
from parser import Parser
from engine import Engine

if __name__ == "__main__":
    # Take user input for regex and test string
    regex_input = input("Enter the regex: ")
    test_string = input("Enter the test string: ")

    # Syntax checking
    syntax_checker = syntaxChecker(regex_input)
    is_valid_regex = syntax_checker.is_valid_regex()

    if is_valid_regex:
        # Tokenization
        scanner = Scanner(regex_input)
        tokens = scanner.tokenize()

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Engine
        regex_engine = Engine(ast)
        result = regex_engine.match(test_string)

        print(f"Regex matches the string: {result}")
    else:
        print("Invalid regex syntax.")
