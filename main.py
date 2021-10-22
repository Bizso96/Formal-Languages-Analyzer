from CustomHashMap import *
from LexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    lexical_analyzer = LexicalAnalyzer()
    lexical_analyzer.open_file("p1.txt")
    lexical_analyzer.read_tokens_input("token.in")
    for line in lexical_analyzer.get_file_content():
        print(line, end="")
    lexical_analyzer.close_file()

