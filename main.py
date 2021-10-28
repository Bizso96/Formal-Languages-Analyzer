from CustomHashMap import *
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    lexical_analyzer = LexicalAnalyzer()
    lexical_analyzer.open_file("p1.txt")
    lexical_analyzer.read_tokens_input("token.in")

    print(lexical_analyzer.reservedWords)
    print(lexical_analyzer.typeNames)
    print(lexical_analyzer.separators)
    print(lexical_analyzer.arithmetic_operators)
    print(lexical_analyzer.logical_operators)
    print(lexical_analyzer.relational_operators)
    print(lexical_analyzer.assignment_operators)

    lexical_analyzer.close_file()

    lexical_analyzer.tokenize()

    lexical_analyzer.analyze()
