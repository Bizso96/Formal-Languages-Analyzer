from CustomHashMap import *
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    lexical_analyzer = LexicalAnalyzer()
    lexical_analyzer.open_file("p1.txt")
    lexical_analyzer.read_tokens_input("token.in")

    lexical_analyzer.close_file()

    lexical_analyzer.tokenize()

    #for t in lexical_analyzer.tokens:
    #    print(t)

    lexical_analyzer.analyze()
