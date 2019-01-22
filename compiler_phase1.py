import ply.lex as lex

input_lex = "input3.txt"

with open(input_lex, 'r') as f:
    data = f.read()

tokens = (
    'NUMBER',
    'LETTER',
    'SEMI_COLON',
    'COLON',
    'COMMA',
    'OPEN_BRACKETS',
    'CLOSE_BRACKETS',
    'OPEN_PARANTHESES',
    'CLOSE_PARANTHESES',
    'OPEN_BRACES',
    'CLOSE_BRACES',
    'STATIC_KW',
    'CHARACTER_KW',
    'CHAR_KW',
    'INTEGER_KW',
    'INT_KW',
    'BOOLEAN_KW',
    'BOOL_KW',
    'VOID_KW',
    'SPACE',
    'IF_KW',
    'OTHER_KW',
    'TILL_KW',
    'COMEBACK_KW',
    'GIVEBACK_KW',
    'CONTINUE_KW',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'EQ',
    'INC_VAL',
    'DEC_VAL',
    'TIMES_VAL',
    'DIVIDE_VAL',
    'THEN_KW',
    'ELSE_KW',
    'LT_EQ',
    'GT_EQ',
    'IS_EQ',
    'LT',
    'GT',
    'NOT_EQ',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'QM',
    'DOT',
    'CONST_KW',
    'TRUE_KW',
    'FALSE_KW',
    'OR_OR',
    'AND_AND',
    'NOT',
    'AND_KW',
    'OR_KW',
 )

reserved = {
    'static': 'STATIC_KW',
    'character': 'CHARACTER_KW',
    'char': 'CHAR_KW',
    'integer': 'INTEGER_KW',
    'int': 'INT_KW',
    'boolean': 'BOOLEAN_KW',
    'bool': 'BOOL_KW',
    'void': 'VOID_KW',
    'IF_KW': 'if',
    'other': 'OTHER_KW',
    'till': 'TILL_KW',
    'comeback': 'COMEBACK_KW',
    'giveback': 'GIVEBACK_KW',
    'continue': 'CONTINUE_KW',
    'then': 'THEN_KW',
    'else': 'ELSE_KW',
    'const': 'CONST_KW',
    'true': 'TRUE_KW',
    'false': 'FALSE_KW',
    'and': 'AND_KW',
    'or': 'OR_KW',
}


t_SEMI_COLON = r';'
t_COLON = r':'
t_COMMA = r','
t_OPEN_BRACKETS = r'\['
t_CLOSE_BRACKETS = r'\]'
t_OPEN_BRACES = r'\{'
t_CLOSE_BRACES = r'\}'
t_OPEN_PARANTHESES = r'\('
t_CLOSE_PARANTHESES = r'\)'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

t_LT_EQ = r'<='
t_GT_EQ = r'>='
t_LT = r'<'
t_GT = r'>'
t_IS_EQ = r'=='
t_NOT_EQ = r'!='
t_EQ = r'='

t_INC_VAL = r'\+='
t_DEC_VAL = r'-='
t_TIMES_VAL = r'\*='
t_DIVIDE_VAL = r'/='

t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'

t_QM = r'\?'
t_DOT = r'\.'

t_OR_OR = r'\|\|'
t_AND_AND = r'\&\&'
t_NOT = r'~'


 # A regular expression rule with some action code
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t

def t_LETTER(t):
    r'[A-Za-z]+'
    t.type = reserved.get(t.value,'LETTER')
    return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
#t_SPACE = r' '
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()
  # Test it out
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)