from antlr4 import *

from generated.Java8Lexer import Java8Lexer
from generated.Java8Parser import Java8Parser
from generated.Java8ParserListener import Java8ParserListener


class Message:

    def __init__(self, _name):
        self.name = _name
        self.members = []

    def add(self, _item):
        self.members.append(_item)

    def __str__(self):
        return "message " + self.name + " {\n" + "\n".join(["  " + self.translate(s) for s in self.members]) + "\n}"

    def translate(self, s):
        if s == "String":
            return "string"
        else:
            return s


class MyListener(Java8ParserListener):

    def __init__(self):
        self.reqs = []
        self.resps = []

    def enterClassDeclaration(self, ctx: Java8Parser.ClassDeclarationContext):
        print("Class: " + ctx.getText())
        super().enterClassDeclaration(ctx)

    def enterNormalInterfaceDeclaration(self, ctx: Java8Parser.NormalInterfaceDeclarationContext):
        print("service " + ctx.children[2].symbol.text + "{")
        super().enterNormalInterfaceDeclaration(ctx)

    def exitNormalInterfaceDeclaration(self, ctx: Java8Parser.NormalInterfaceDeclarationContext):
        print("}")
        super().enterNormalInterfaceDeclaration(ctx)

    def enterInterfaceMethodDeclaration(self, ctx: Java8Parser.InterfaceMethodDeclarationContext):
        self.method = ctx.methodHeader().methodDeclarator().Identifier().getText()
        self.response = ''
        self.reqs.append(Message(self.method + "_req"))
        self.resps.append(Message(self.method + "_resp"))

    def exitInterfaceMethodDeclaration(self, ctx: Java8Parser.InterfaceMethodDeclarationContext):
        header: Java8Parser.MethodHeaderContext = ctx.methodHeader()
        declarator: Java8Parser.MethodDeclaratorContext = header.methodDeclarator()
        print(
            " rpc " + declarator.Identifier().symbol.text + "(" + self.method + "_req) returns (" + self.method + "_resp) {}")
        super().enterInterfaceMethodDeclaration(ctx)

    def enterUnannClassType_lfno_unannClassOrInterfaceType(self,
                                                           ctx: Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        self.response = ctx.Identifier().getText()
        self.types = []
        super().enterUnannClassType_lfno_unannClassOrInterfaceType(ctx)

    def exitUnannClassType_lfno_unannClassOrInterfaceType(self,
                                                          ctx: Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        if len(self.types) > 0:
            self.response += "<" + ",".join(self.types) + ">"
        self.resps[-1].add(self.response)
        super().enterUnannClassType_lfno_unannClassOrInterfaceType(ctx)

    def enterClassType_lfno_classOrInterfaceType(self, ctx: Java8Parser.ClassType_lfno_classOrInterfaceTypeContext):
        self.types.append(ctx.Identifier().getText())
        super().enterClassType_lfno_classOrInterfaceType(ctx)

    def enterUnannPrimitiveType(self, ctx: Java8Parser.UnannPrimitiveTypeContext):
        self.response = ctx.getText()
        super().enterUnannPrimitiveType(ctx)


def main(file):
    input_stream = FileStream(file)
    lexer = Java8Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Java8Parser(stream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, tree)

    for m in listener.reqs:
        print(m)

    for m in listener.resps:
        print(m)


if __name__ == '__main__':
    main('interface.java')
    main('int2.java')
    main('pojo.java')
