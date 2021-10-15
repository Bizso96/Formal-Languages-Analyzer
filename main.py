from CustomHashMap import *

if __name__ == '__main__':
    symbolTable = CustomHashMap(8)

    symbolTable.add("a")
    symbolTable.add("b")
    symbolTable.add("dog")
    symbolTable.add("bear")
    symbolTable.add("pear")
    symbolTable.add("sparta")
    symbolTable.add("wok")
    symbolTable.add("bottle")
    symbolTable.add("cat")
    symbolTable.add("cat")

    print(symbolTable.search("a"))
    print(symbolTable.search("dog"))
    print(symbolTable.search("wok"))

    print(symbolTable.search("asdasd"))


