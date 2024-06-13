# Generated from ../Pattern.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PatternParser import PatternParser
else:
    from PatternParser import PatternParser

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternSimplifierVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PatternParser#pattern.
    def visitPattern(self, ctx:PatternParser.PatternContext):
        simplified = ''
        additionalPatterns = 0
        for child in ctx.children[:-1]: # Skip EOF
            fragment, more = self.visit(child)
            simplified += fragment
            additionalPatterns += more
        return simplified, additionalPatterns


    # Visit a parse tree produced by PatternParser#other.
    def visitOther(self, ctx:PatternParser.OtherContext):
        return ctx.getText(), 0


    # Visit a parse tree produced by PatternParser#quantified.
    def visitQuantified(self, ctx:PatternParser.QuantifiedContext):
        expr, quantifier = ctx.children
        if quantifier.getText() == '+':
            fragment, more = self.visit(expr)
            return f'({fragment})({fragment})*', 1 + 2 * more
        return ctx.getText(), 1


    # Visit a parse tree produced by PatternParser#parenthesized.
    def visitParenthesized(self, ctx:PatternParser.ParenthesizedContext):
        acc = '('
        cpt = 0
        for expr in ctx.children[1:-1]: # Skip '(' and ')'
            fragment, more = self.visit(expr)
            acc += fragment
            cpt += more
        return acc + ')', cpt


    # Visit a parse tree produced by PatternParser#operation.
    def visitOperation(self, ctx:PatternParser.OperationContext):
        left, op, right = ctx.children
        leftFragment, leftMore = self.visit(left)
        rightFragment, rightMore = self.visit(right)
        return f'{leftFragment}{op.getText()}{rightFragment}', leftMore + rightMore + 1


    # Visit a parse tree produced by PatternParser#digit.
    def visitDigit(self, ctx:PatternParser.DigitContext):
        return ctx.getText(), 0



del PatternParser