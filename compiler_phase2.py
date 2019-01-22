import ply.lex as lex
import ply.yacc as yacc
import pickle

 
def p_num(p):
	 'num : NUM'
	 logger(p, 'Rule1: num -> NUM')
 
def p_letter(p):
	 'letter : LETTER'
	 logger(p, 'Rule2.1: letter -> LETTER')
 
def p_letter_letter(p):
	 'letter : letterletter'
	 logger(p, 'Rule2.2: letter -> LETTER LETTER')
 
def p_program(p):
	 'program : list'
	 logger(p, 'Rule4: program -> list')
 
def p_list_list(p):
	 'list : list declaration'
	 logger(p, 'Rule5: list -> list declaration')
 
def p_list_dec(p):
	 'list : declaration'
	 logger(p, 'Rule5: list -> declaration')
 
def p_dec_fun(p):
	 'declaration : function'
	 logger(p, 'Rule6: declaration -> function')
 
def p_dec_varDec(p):
	 'declaration : varDeclaration'
	 logger(p, 'Rule6: declaration -> varDeclaration')
 
def p_varDec(p):
	 'varDeclaration : type variableList SEMICOLON'
	 logger(p, 'Rule7: varDeclaration -> type variableList ;')
 
def p_scopedVarDec(p):
	 'scopedVariableDec : scopedSpecifier variableList;'
	 logger(p, 'Rule8: scopedVariableDec -> scopedSpecifier variableList')
 
def p_varList(p):
	'''variableList: variableList COMMA varInitialization
				   | varInitialization'''
	if len(p) == 3:
		logger(p, 'Rule9.1: varList -> variableList , varInitialization')
	elif len(p) == 1:
		logger(p, 'Rule9.2: varList -> varInitialization')
 
def p_varInit(p):
	 '''varInitialization : varForm
						  | varForm COLON OPEN_PARANTHESES eachExpression CLOSE_PARANTHESES'''
	 if len(p) == 1:
		 logger(p, 'Rule10.1: varInitialization -> varForm')
	 elif len(p) == 5:
		 logger(p, 'Rule10.2: varInitialization -> varForm : ( eachExpression )')

def p_varForm(p):
	'''varFrom: letter numOrletter OPEN_BRACKETS num CLOSE_BRACKETS 
			  | letter numOrletter'''
	if len(p) == 5:
		logger(p, 'Rule11.1: varForm -> letter numOrletter [ num ]')
	elif len(p) == 2:
		logger(p, 'Rule11.2: varFrom -> letter numOrletter')
 
def p_scopedSpecifier(p):
	'''scopedSpecifier: STATIC_KW type
					  | type'''
	if len(p) == 2:
		logger(p, 'Rule12.1: scopedSpecifier -> static type')
	elif len(p) == 1:
		logger(p, 'Rule12.2: scopedSpecifier -> type')
 
def type_1(p):
	 'type: BOOLEAN_KW'
	 logger(p, 'Rule13.1: type -> boolean')
 
def type_2(p):
	 'type: BOOL_KW'
	 logger(p, 'Rule13.2: type -> bool')
 
def type_3(p):
	 'type: CHARACTER_KW'
	 logger(p, 'Rule13.3: type -> character')
 
def type_4(p):
	 'type: CHAR_KW'
	 logger(p, 'Rule13.4: type -> char')
 
def type_5(p):
	 'type: INTEGER_KW'
	 logger(p, 'Rule13.5: type -> integer')
 
def type_6(p):
	 'type: INT_KW'
	 logger(p, 'Rule13.6: type -> int')

def p_function(p):
	'''function: VOID_KW numOrletter OPEN_PARANTHESES parameter CLOSE_PARANTHESES OPEN_BEACES statement CLOSE_BRACES
			   | type letter numOrletter OPEN_PARANTHESES parameter CLOSE_PARANTHESES'''
	if len(p) == 8:
		logger(p, 'Rule14.1: function -> void numOrletter ( parameter ) { statement }')
	elif len(p) == 6:
		logger(p, 'Rule14.2: function -> type letter numOrletter ( parameter )') 

def p_parameter(p):
	'''parameter: listOfParameters
					  | empty'''
	if len(p) == 1:
		logger(p, 'Rule15.1: parameter -> listOfParameters')
	elif len(p) == 0:
		logger(p, 'Rule15.2: parameter -> 𝜀')

def p_list_of_parameter(p):
	'''listOfParameter: listOfParameters SEMICOLON paramTypeList
					  | paramTypeList'''
	if len(p) == 3:
		logger(p, 'Rule16.1: listOfParameters -> listOfParameters ; paramTypeList')
	elif len(p) == 1:
		logger(p, 'Rule16.2: listOfParameters -> paramTypeList')

def p_param_type_list(p):
	'paramTypeList: type paramList'
	logger(p, 'Rule17: paramTypeList -> type paramList')

def p_paramList(p):
	'''paramList: paramList COMMA paramID
					  | paramID'''
	if len(p) == 3:
		logger(p, 'Rule18.1: paramList -> paramList , paramID')
	elif len(p) == 1:
		logger(p, 'Rule18.2: paramList -> paramID')

def p_localDec(p):
	'''localDeclarations: localDeclarations ScopedVariableDec
					  | empty'''
	if len(p) == 2:
		logger(p, 'Rule19.1: localDeclarations -> localDeclarations ScopedVariableDec')
	elif len(p) == 0:
		logger(p, 'Rule19.2: localDeclarations -> 𝜀')


def p_factor_expr(p):
	 'factor : LPAREN expression RPAREN'
	 p[0] = p[2]
 
 
 # Error rule for syntax errors
def p_error(p):
	 print("Syntax error in input!")
 
 # Build the parser
#parser = yacc.yacc()
 
# while True:
# 	try:
# 		s = raw_input('a = b')
# 	except EOFError:
# 		break
# 	if not s: continue
# 	result = parser.parse(s)
# 	print(result)

