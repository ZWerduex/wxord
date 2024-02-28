grammar Pattern;

// Parser

pattern : expr* EOF;

expr
    : OPEN_PAREN expr CLOSE_PAREN # parenthesized
    | expr QUANTIFIER # quantified
    | expr OPERATOR expr # operation
    | ( DIGIT | OTHER )+ # atom
    ;

// Lexer

DIGIT : [0-9];

OPERATOR : '|';

QUANTIFIER : '+' | '*' | '?';

OPEN_PAREN : '(';
CLOSE_PAREN : ')';

OTHER : .;