#!/usr/bin/env bash
java -Xmx500M -cp tools/antlr-4.8-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -o ../generated/ Java8Lexer.g4 Java8Parser.g4