# Generated from ../Pattern.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PatternParser import PatternParser
else:
    from PatternParser import PatternParser

import random

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternExpanderVisitor(ParseTreeVisitor):

    def __init__(self, additionalPatterns: int) -> None:
        super().__init__()
        self.additionalPatterns = additionalPatterns
        self.encounteredAdditionalPatterns = 0
        self.hasExpanded = False

    def doExpansion(self):
        self.encounteredAdditionalPatterns += 1
        return random.randint(0, self.additionalPatterns) <= self.encounteredAdditionalPatterns

    # Visit a parse tree produced by PatternParser#pattern.
    def visitPattern(self, ctx:PatternParser.PatternContext):
        expanded = ''
        for child in ctx.children[:-1]: # Skip EOF
            expanded += self.visit(child)
        return expanded, self.additionalPatterns


    # Visit a parse tree produced by PatternParser#other.
    def visitOther(self, ctx:PatternParser.OtherContext):
        return ctx.getText()


    # Visit a parse tree produced by PatternParser#quantified.
    def visitQuantified(self, ctx:PatternParser.QuantifiedContext):
        expr, quantifier = ctx.children
        quantifier = quantifier.getText()

        if not self.hasExpanded:
            if quantifier == '+':
                raise SyntaxError("Pattern contains a '+' quantifier : did you simplify it first ?")

            if self.doExpansion():
                self.hasExpanded = True

                fragment = expr.getText()
                if quantifier == '*':
                    return f'({fragment})({fragment})*'
                
                self.additionalPatterns -= 1
                return fragment # quantifier == '?'

        return self.visit(expr) + quantifier


    # Visit a parse tree produced by PatternParser#parenthesized.
    def visitParenthesized(self, ctx:PatternParser.ParenthesizedContext):
        acc = '('
        for expr in ctx.children[1:-1]: # Skip '(' and ')'
            acc += self.visit(expr)
        return acc + ')'


    # Visit a parse tree produced by PatternParser#operation.
    def visitOperation(self, ctx:PatternParser.OperationContext):
        left, op, right = ctx.children

        if op.getText() == '|':
            if not self.hasExpanded:
                if self.doExpansion():
                    self.hasExpanded = True

                    self.additionalPatterns -= 1
                    return left.getText() if random.randint(0, 1) == 0 else right.getText()
            
            return self.visit(left) + '|' + self.visit(right)
        
        raise NotImplementedError("Only '|' operation is supported")


    # Visit a parse tree produced by PatternParser#digit.
    def visitDigit(self, ctx:PatternParser.DigitContext):
        return ctx.getText()



del PatternParser