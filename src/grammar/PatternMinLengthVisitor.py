# Generated from ../Pattern.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PatternParser import PatternParser
else:
    from PatternParser import PatternParser

import random

from grammar.CharSet import CharSet

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternMinLengthVisitor(ParseTreeVisitor):

    def __init__(self, charsets: list[CharSet]) -> None:
        super().__init__()
        self.charsetsMinLength = [
            min(len(char) for char in charset.chars) for charset in charsets
        ]

    # Visit a parse tree produced by PatternParser#pattern.
    def visitPattern(self, ctx:PatternParser.PatternContext):
        minLength = 0
        for child in ctx.children[:-1]: # Skip EOF
            minLength += self.visit(child)
        return minLength


    # Visit a parse tree produced by PatternParser#other.
    def visitOther(self, ctx:PatternParser.OtherContext):
        return len(ctx.getText())


    # Visit a parse tree produced by PatternParser#quantified.
    def visitQuantified(self, ctx:PatternParser.QuantifiedContext):
        expr, quantifier = ctx.children
        # If quantifier is '+', the minimum length is the length of the expression
        if quantifier.getText() == '+':
            return self.visit(expr)
        # Any other quantifier makes the expression optional
        return 0


    # Visit a parse tree produced by PatternParser#parenthesized.
    def visitParenthesized(self, ctx:PatternParser.ParenthesizedContext):
        minLength = 0
        for child in ctx.children[1:-1]: # Skip parentheses
            minLength += self.visit(child)
        return minLength


    # Visit a parse tree produced by PatternParser#operation.
    def visitOperation(self, ctx:PatternParser.OperationContext):
        left, op, right = ctx.children
        # If the operation is '|', the minimum length is the minimum length of the left and right expressions
        if op.getText() == '|':
            return min(self.visit(left), self.visit(right))
        
        raise NotImplementedError('Operation not implemented')


    # Visit a parse tree produced by PatternParser#digit.
    def visitDigit(self, ctx:PatternParser.DigitContext):
        digit = int(ctx.getText())

        # Take the smallest char length if the digit is 0 or greater than the number of charsets
        if digit == 0 or digit > len(self.charsetsMinLength):
            return min(self.charsetsMinLength)
        
        # Otherwise, take the smallest char length of the digit-th charset
        return self.charsetsMinLength[digit - 1]
    
del PatternParser