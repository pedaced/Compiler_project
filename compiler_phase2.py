import ply.lex as lex
import ply.yacc as yacc
import pickle

 
def p_num(p):
	 'num : NUM'
	 # logger(p, 'Rule1: num -> NUM')
 
def p_letter(p):
	 'letter : LETTER'
	 # logger(p, 'Rule2.1: letter -> letter')
 
def p_letter_letter(p):
	 'letter : letterletter'
	 logger(p, 'Rule2.2: letter -> letter letter')

def p_numOrLetter1(p):
	 'numOrletter : num'
	 logger(p, 'Rule3.1: numOrletter -> num')

def p_numOrLetter2(p):
	 'numOrletter : letter'
	 logger(p, 'Rule3.2: numOrletter -> letter')

def p_numOrLetter2(p):
	 'numOrletter : empty'
	 logger(p, 'Rule3.3: numOrletter -> 𝜀')

def p_numOrLetter4(p):
	 'numOrletter : letter letter'
	 logger(p, 'Rule2.2: numOrletter -> letter letter') 

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

def p_paramID(p):
	'''paramID: letter numOrletter
					  | letter numOrletter OPEN_BRACES CLOSE_BRACES'''
	if len(p) == 2:
		logger(p, 'Rule20.1: paramID -> letter numOrletter')
	elif len(p) == 4:
		logger(p, 'Rule20.2: paramID -> letter numOrletter []')

def p_statement(p):
	'''statement: phrase 
				| compoundPhrase
				| selectPhrase
				| iterationPhrase
				| returnPhrase
				| continue'''
	if p[1] == 'phrase':
		logger(p, 'Rule21.1: statement -> phrase')
	elif p[1] == 'compoundPhrase':
		logger(p, 'Rule21.2: statement -> compoundPhrase')
	elif p[1] == 'selectPhrase':
		logger(p, 'Rule21.3: statement -> selectPhrase')
	elif p[1] == 'iterationPhrase':
		logger(p, 'Rule21.4: statement -> iterationPhrase')
	elif p[1] == 'returnPhrase':
		logger(p, 'Rule21.5: statement -> returnPhrase')
	elif p[1] == 'continue':
		logger(p, 'Rule21.6: statement -> continue')

def p_compoundPhrase(p):
	'compoundPhrase: OPEN_BRACES localDeclarations statementList CLOSE_BRACES'
	logger(p, 'Rule22.1: compoundPhrase -> {localDeclarations statementList}')

def p_statementList(p):
	'''statementList: statementList statement
					  | empty'''
	if len(p) == 2:
		logger(p, 'Rule23.1: statementList -> statementList statement')
	elif len(p) == 0:
		logger(p, 'Rule23.2: statementList -> 𝜀')
 
def p_phrase(p):
	'''phrase: allExpression SEMICOLON
					  | SEMICOLON'''
	if len(p) == 2:
		logger(p, 'Rule24.1: phrase -> allExpression ;')
	elif len(p) == 1:
		logger(p, 'Rule24.2: phrase -> ;')

def p_selectPhrase(p):
	'''selectPhrase: IF_KW OPEN_PARANTHESES eachExpression CLOSE_PARANTHESES ifBody
					  | IF_KW OPEN_PARANTHESES eachExpression CLOSE_PARANTHESES OPEN_BRACES ifBody ifBody CLOSE_BRACES'''
	if len(p) == 5:
		logger(p, 'Rule25.1: selectPhrase -> if ( eachExpression ) ifBody')
	elif len(p) == 8:
		logger(p, 'Rule25.2: selectPhrase -> if ( eachExpression ) { ifBody ifBody }')

def p_ifBody(p):
	'''ifBody: statement
	         | statement OTHER_KW statement
	         | SEMICOLON'''
	if len(p) == '3':
		logger(p, 'Rule26.2: ifBody -> statement other statement')
	elif p[1] == ';':
		logger(p, 'Rule26.3: ifBody -> ;')
	elif p[1] == 'statement':
		logger(p, 'Rule26.1: ifBody -> statement')

def p_iterationPhrase(p):
	'iterationPhrase: TILL_KW OPEN_PARANTHESES eachExpression CLOSE_PARANTHESES statement'
	logger(p, 'Rule27: iterationPhrase -> till ( eachExpression )')


def p_returnPhrase1(p):
	'returnPhrase: COMEBACK_KW SEMICOLON'
	logger(p, 'Rule28.1: returnPhrase -> comeback ;')

	
def p_returnPhrase2(p):
	'returnPhrase: GIVEBACK_KW allExpression SEMICOLON'
	logger(p, 'Rule28.2: returnPhrase -> giveback allExpression ;')

	
def p_returnPhrase3(p):
	'returnPhrase: GIVEBACK_KW numOrletter SEMICOLON'
	logger(p, 'Rule28.3: returnPhrase -> giveback numOrletter ;')


def p_continue(p):
	'continue: CONTINUE_KW SEMICOLON'
	logger(p, 'Rule29: continue -> continue ;')


def p_allExpression1(p):
	'allExpression: alterable mathOp allExpression'
	logger(p, 'Rule30.1: allExpression -> alterable mathOp allExpression')

def p_allExpression2(p):
	'allExpression: alterable PLUS_PLUS'
	logger(p, 'Rule30.2: allExpression -> alterable ++')

def p_allExpression3(p):
	'allExpression: alterable MINUS_MINUS'
	logger(p, 'Rule30.3: allExpression -> alterable --')

def p_allExpression4(p):
	'allExpression: alterable mathOp alterable'
	logger(p, 'Rule30.5: allExpression -> alterable mathOp alterable')

def p_allExpression5(p):
	'allExpression: eachExpression'
	logger(p, 'Rule30.4: allExpression -> eachExpression')

def p_mathOp1(p):
	'mathOp: EQ'
	logger(p, 'Rule31.1: mathOp -> =')

def p_mathOp2(p):
	'mathOp: INC_VAL'
	logger(p, 'Rule31.2: mathOp -> +=')

def p_mathOp3(p):
	'mathOp: DEC_VAL'
	logger(p, 'Rule31.3: mathOp -> -=')

def p_mathOp4(p):
	'mathOp: TIMES_VAL'
	logger(p, 'Rule31.4: mathOp -> *=')

def p_mathOp5(p):
	'mathOp: DIVIDE_VAL'
	logger(p, 'Rule31.5: mathOp -> \=')

def p_eachExpression1(p):
	'eachExpression: eachExpression logicOp eachExpression'
	logger(p, 'Rule32.1: eachExpression -> eachExpression logicOp eachExpression')
	
def p_eachExpression2(p):
	'eachExpression: eachExpression logicOp THEN_KW eachExpression'
	logger(p, 'Rule32.2: eachExpression -> eachExpression logicOp then eachExpression')

def p_eachExpression3(p):
	'eachExpression: logicOp eachExpression'
	logger(p, 'Rule32.3: eachExpression -> logicOp eachExpression')

def p_eachExpression4(p):
	'eachExpression: realExpression'
	logger(p, 'Rule32.4: eachExpression -> realExpression')

def p_eachExpression5(p):
	'eachExpression: realExpression logicOp ELSE_KW'
	logger(p, 'Rule32.5: eachExpression -> realExpression logicOp else')

def p_realExpression1(p):
	'realExpression: mathExpression compareType mathExpression'
	logger(p, 'Rule33.1: realExpression -> mathExpression compareType mathExpression')

def p_realExpression2(p):
	'realExpression: mathExpression compareType mathExpression'
	logger(p, 'Rule33.2: realExpression -> mathExpression')

def p_cimpareType1(p):
	'compareType: equal'
	logger(p, 'Rule34.1: compareType -> equal')
	
def p_compareType2(p):
	'compareType: nonEqual'
	logger(p, 'Rule34.2: compareType -> nonEqual')

def p_equal1(p):
	'equal: LT_EQ'
	logger(p, 'Rule35.1: equal -> <=')
	
def p_equal2(p):
	'equal: GT_EQ'
	logger(p, 'Rule35.2: equal -> >=')
	
def p_equal3(p):
	'equal: IS_EQ'
	logger(p, 'Rule35.3: equal -> ==')

def p_nonEqual1(p):
	'equal: LT'
	logger(p, 'Rule36.1: equal -> <')
	
def p_nonEqual2(p):
	'equal: GT'
	logger(p, 'Rule36.2: equal -> >')
	
def p_nonEqual3(p):
	'equal: NOT_EQ'
	logger(p, 'Rule36.3: equal -> !=')

def p_mathExp1(p):
	'mathExp: mathExp op mathExp'
	logger(p, 'Rule37.1: mathExp -> mathExp op mathExp')

def p_mathExp2(p):
	'mathExp: unaryExpression'
	logger(p, 'Rule37.2: mathExp -> unaryExpression')
		
def p_op1(p):
	'op: PLUS'
	logger(p, 'Rule38.1: op -> +')
		
def p_op2(p):
	'op: MINUS'
	logger(p, 'Rule38.2: op -> -')
		
def p_op3(p):
	'op: TIMES'
	logger(p, 'Rule38.3: op -> *')
		
def p_op4(p):
	'op: DIVIDE'
	logger(p, 'Rule38.4: op -> /')

def p_op5(p):
	'op: REMINDER'
	logger(p, 'Rule38.5: op -> %')

def p_unaryExpression1(p):
	'unaryExpression: unaryop unaryExpression'
	logger(p, 'Rule39.1: unaryExpression -> unaryop unaryExpression')

def p_unaryExpression2(p):
	'unaryExpression: factor'
	logger(p, 'Rule39.2: unaryExpression -> factor')

def p_unaryop1(p):
	'unaryop: MINUS'
	logger(p, 'Rule40.1: unaryop -> -')
	
def p_unaryop2(p):
	'unaryop: PLUS'
	logger(p, 'Rule40.1: unaryop -> +')

def p_unaryop3(p):
	'unaryop: QM'
	logger(p, 'Rule40.1: unaryop -> ?')

def p_factor1(p):
	'factor: inalterable'
	logger(p, 'Rule41.1: factor -> inalterable')

def p_factor2(p):
	'factor: alterable'
	logger(p, 'Rule41.2: factor -> alterable')

def p_alterable1(p):
	'alterable: letter numOrletter'
	logger(p, 'Rule42.1: alterable -> letter numOrletter')

def p_alterable2(p):
	'alterable: alterable OPEN_BRACKETS allExpression CLOSE_BRACKETS'
	logger(p, 'Rule42.2: alterable -> alterable [ allExpression ]')

def p_alterable3(p):
	'alterable: alterable DOT letter numOrletter'
	logger(p, 'Rule42.3: alterable -> alterable . letter numOrletter')

def p_inalterable1(p):
	'inalterable: OPEN_PARANTHESES allExpression CLOSE_PARANTHESES'
	logger(p, 'Rule43.1: inalterable -> ( allExpression )')

def p_inalterable2(p):
	'inalterable: constant'
	logger(p, 'Rule43.2: inalterable -> constant')

def p_inalterable3(p):
	'inalterable: letter numOrletter OPEN_PARANTHESES args CLOSE_PARANTHESES'
	logger(p, 'Rule43.3: inalterable -> letter ( args )')

def p_args(p):
	'''args: arguments
					  | empty'''
	if len(p) == 1:
		logger(p, 'Rule44.1: args -> argunments')
	elif len(p) == 0:
		logger(p, 'Rule44.2: args -> 𝜀')

def p_arguments1(p):
	'argunments: argunments COMMA allExpression'
	logger(p, 'Rule45.1: argunments -> argunments , allExpression')

def p_arguments2(p):
	'argunments: allExpression'
	logger(p, 'Rule45.2: argunments -> allExpression')

def p_constant1(p):
	'constant: CONST_KW'
	logger(p, 'Rule46.1: constant -> CONST')

def p_constant2(p):
	'constant: TRUE_KW'
	logger(p, 'Rule46.2: constant -> TRUE')

def p_constant3(p):
	'constant: FALSE_KW'
	logger(p, 'Rule46.3: constant -> FALSE')

def p_logicOp1(p):
	'logicOp: AND_AND'
	logger(p, 'Rule47.1: constant -> &&')

def p_logicOp2(p):
	'logicOp: OR_OR'
	logger(p, 'Rule47.2: constant -> ||')

def p_logicOp3(p):
	'logicOp: NOT'
	logger(p, 'Rule47.3: constant -> ~')

def p_logicOp4(p):
	'logicOp: AND_KW'
	logger(p, 'Rule47.4: constant -> and')

def p_logicOp5(p):
	'logicOp: OR_KW'
	logger(p, 'Rule47.5: constant -> or')

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

