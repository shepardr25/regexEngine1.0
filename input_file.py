from syntaxChecker import syntaxChecker

if __name__ == "__main__":
    test_regex = "A\d+"
    test_string = "A123"

    # Syntax Checker
    if syntaxChecker.is_valid(test_regex):
        print(f"Regex: {test_regex}")
        print(f"Input String: {test_string}")
        print("Both regex and string are valid.")
    else:
        print("Invalid regex syntax.")
