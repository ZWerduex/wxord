# Generated from Pattern.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PatternParser import PatternParser
else:
    from PatternParser import PatternParser

import random

from grammar.CharSet import CharSet

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternVisitor(ParseTreeVisitor):

    def __init__(self, maxLength: int, charsets: list[CharSet]) -> None:
        super().__init__()
        self.remainingLength = maxLength
        self.charsets = charsets

    # Visit a parse tree produced by PatternParser#pattern.
    def visitPattern(self, ctx:PatternParser.PatternContext):
        acc = ''
        for i, child in enumerate(ctx.children):
            # Skip EOF
            if i >= len(ctx.children) - 1:
                break
            word = self.visit(child)
            self.remainingLength -= len(word)
            acc += word
        return acc

    # Visit a parse tree produced by PatternParser#quantified.
    def visitQuantified(self, ctx:PatternParser.QuantifiedContext):
        expr, quantifier = ctx.children
        # 0 or 1
        if (quantifier := quantifier.getText()) == '?':
            # If the word should be included, return it
            if random.choice([True, False]):
                word = self.visit(expr)
                self.remainingLength -= len(word)
                return word
            # Otherwise, return an empty string
            return ''
        # 0/1 or more
        acc = ''
        # While the word should be included and there are still characters to consume
        while random.choice([True, False]) and self.remainingLength > 0:
            # Visit the expression and add it to the accumulator
            word = self.visit(expr)
            acc += word
            # Update the remaining length
            self.remainingLength -= len(word)
        # O or more if the quantifier is '*', 1 or more otherwise
        if quantifier == '*':
            return acc
        word = self.visit(expr)
        self.remainingLength -= len(word)
        return word + acc

    # Visit a parse tree produced by PatternParser#parenthesized.
    def visitParenthesized(self, ctx:PatternParser.ParenthesizedContext):
        expr = self.visit(ctx.children[1])
        self.remainingLength -= len(expr)
        return expr

    # Visit a parse tree produced by PatternParser#operation.
    def visitOperation(self, ctx:PatternParser.OperationContext):
        left, op, right = ctx.children
        
        if op.getText() == '|':
            if random.choice([True, False]):
                left = self.visit(left)
                self.remainingLength -= len(left)
                return left
            right = self.visit(right)
            self.remainingLength -= len(right)
            return right
        
        raise NotImplementedError(f'Unknown operation: {op.getText()}')
        
    # Visit a parse tree produced by PatternParser#atom.
    def visitAtom(self, ctx:PatternParser.AtomContext):
        atom = ctx.getText()
        word = ''
        for char in atom:
            if char.isdigit():
                digit = int(char)
                if digit == 0 or digit > len(self.charsets):
                    charset = random.choice(self.charsets)
                else:
                    charset = self.charsets[digit - 1]
                word += charset.pick()
            else:
                word += char
        self.remainingLength -= len(word)
        return word

del PatternParser