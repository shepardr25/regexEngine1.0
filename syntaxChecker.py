import re

class syntaxChecker:
    @staticmethod
    def is_valid(regex):
        try:
            re.compile(regex)
            return True
        except re.error:
            return False
