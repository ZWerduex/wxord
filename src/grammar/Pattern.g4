grammar Pattern;

// Parser

pattern : expr* EOF;

expr
    : '(' expr+ ')' # parenthesized
    | expr QUANTIFIER # quantified
    | expr OPERATOR expr # operation
    | DIGIT # digit
    | OTHER+ # other
    ;

// Lexer

DIGIT : '0'..'9';

OPERATOR : '|';

QUANTIFIER : '+' | '*' | '?';

OTHER : .;