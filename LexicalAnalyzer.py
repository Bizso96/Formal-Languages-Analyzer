from CustomHashMap import CustomHashMap


class LexicalAnalyzer:
    def __init__(self):
        self.file = None
        self.symbolTable = CustomHashMap(64)
        self.fileContent = []
        self.reservedWords = []
        self.separators = []
        self.operators = []
        self.tokenList = []

    def open_file(self, filename):
        self.file = open("input/" + filename, "r")
        if self.file.closed:
            return False

        self.fileContent = self.file.readlines()

        return True

    def close_file(self):
        if not self.file.closed:
            self.file.close()

    def get_file_content(self):
        return self.fileContent

    def read_tokens_input(self, filename):
        token_file = open("input/" + filename, "r")
        if self.file.closed:
            return False

        self.reservedWords = token_file.readline().split(":")[1].strip().split(",")
        self.separators = token_file.readline().split(":")[1].replace('"', '').strip().split(",")
        self.separators.append(" ")
        self.operators = token_file.readline().split(":")[1].replace('"', '').strip().split(",")

        print(self.reservedWords)
        print(self.separators)
        print(self.operators)

    def tokenize(self):
        pass
