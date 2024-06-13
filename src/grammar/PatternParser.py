# Generated from ../Pattern.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,40,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,1,
        1,1,1,1,1,4,1,16,8,1,11,1,12,1,17,1,1,1,1,1,1,1,1,4,1,24,8,1,11,
        1,12,1,25,3,1,28,8,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,
        9,1,1,1,0,1,2,2,0,2,0,0,44,0,7,1,0,0,0,2,27,1,0,0,0,4,6,3,2,1,0,
        5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,0,0,0,9,7,
        1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,6,1,-1,0,13,15,5,1,0,0,
        14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,
        0,0,0,18,19,1,0,0,0,19,20,5,2,0,0,20,28,1,0,0,0,21,28,5,3,0,0,22,
        24,5,6,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,
        0,26,28,1,0,0,0,27,12,1,0,0,0,27,21,1,0,0,0,27,23,1,0,0,0,28,36,
        1,0,0,0,29,30,10,3,0,0,30,31,5,4,0,0,31,35,3,2,1,4,32,33,10,4,0,
        0,33,35,5,5,0,0,34,29,1,0,0,0,34,32,1,0,0,0,35,38,1,0,0,0,36,34,
        1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,36,1,0,0,0,6,7,17,25,27,34,
        36
    ]

class PatternParser ( Parser ):

    grammarFileName = "Pattern.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DIGIT", "OPERATOR", 
                      "QUANTIFIER", "OTHER" ]

    RULE_pattern = 0
    RULE_expr = 1

    ruleNames =  [ "pattern", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DIGIT=3
    OPERATOR=4
    QUANTIFIER=5
    OTHER=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PatternParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatternParser.ExprContext)
            else:
                return self.getTypedRuleContext(PatternParser.ExprContext,i)


        def getRuleIndex(self):
            return PatternParser.RULE_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = PatternParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0):
                self.state = 4
                self.expr(0)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(PatternParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PatternParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OtherContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(PatternParser.OTHER)
            else:
                return self.getToken(PatternParser.OTHER, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther" ):
                return visitor.visitOther(self)
            else:
                return visitor.visitChildren(self)


    class QuantifiedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PatternParser.ExprContext,0)

        def QUANTIFIER(self):
            return self.getToken(PatternParser.QUANTIFIER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantified" ):
                return visitor.visitQuantified(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatternParser.ExprContext)
            else:
                return self.getTypedRuleContext(PatternParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesized" ):
                return visitor.visitParenthesized(self)
            else:
                return visitor.visitChildren(self)


    class OperationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PatternParser.ExprContext)
            else:
                return self.getTypedRuleContext(PatternParser.ExprContext,i)

        def OPERATOR(self):
            return self.getToken(PatternParser.OPERATOR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)


    class DigitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIGIT(self):
            return self.getToken(PatternParser.DIGIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PatternParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PatternParser.ParenthesizedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(PatternParser.T__0)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 14
                    self.expr(0)
                    self.state = 17 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0)):
                        break

                self.state = 19
                self.match(PatternParser.T__1)
                pass
            elif token in [3]:
                localctx = PatternParser.DigitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(PatternParser.DIGIT)
                pass
            elif token in [6]:
                localctx = PatternParser.OtherContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 22
                        self.match(PatternParser.OTHER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 25 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PatternParser.OperationContext(self, PatternParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        self.match(PatternParser.OPERATOR)
                        self.state = 31
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = PatternParser.QuantifiedContext(self, PatternParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        self.match(PatternParser.QUANTIFIER)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




