import ply.lex as lex

tokens = ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
          'IDENT', 'STRING', 'NUMBER') 

#####
#

# Token definition rules here. 
def t_PLUS(t):
    r'\+'
    return t
def t_MINUS(t):
    r'\-'
    return t
def t_TIMES(t):
    r'\*'
    return t
def t_DIVIDE(t):
    r'\/'
    return t
def t_IDENT(t):
    r'[a-zA-Z][a-zA-Z_]*'
    return t
def t_STRING_single(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    t.type = "STRING"
    return t
def t_STRING_double(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    t.type = "STRING"
    return t
def t_NUMBER(t):
    r'[0-9][_?0-9]*'
    temp = ""
    for i in range(len(t.value)):
        if t.value[i] != '_':
            temp += t.value[i]
    t.value = int(temp)
    return t

#
#####

t_ignore = ' \t\v\r'

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1) 

# test code for lexer
lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [(tok.type,tok.value)]
  return result

question1 = " +   -   /   * " 
answer1 = [('PLUS', '+'), ('MINUS', '-'), ('DIVIDE', '/'), ('TIMES', '*')]

print test_lexer(question1) == answer1 

question2 = """ 'string "nested" \' "inverse 'nested'" """
answer2 = [('STRING', 'string "nested" '), ('STRING', "inverse 'nested'")]
print test_lexer(question2) == answer2 

question3 = """ 12_34 5_6_7_8 0______1 1234 """
answer3 = [('NUMBER', 1234), ('NUMBER', 5678), ('NUMBER', 1), ('NUMBER', 1234)]
print test_lexer(question3) == answer3

question4 = """ 'he'llo w0rld 33k """
answer4 = [('STRING', 'he'), ('IDENT', 'llo'), ('IDENT', 'w'), ('NUMBER',
0), ('IDENT', 'rld'), ('NUMBER', 33), ('IDENT', 'k')]
print test_lexer(question4) == answer4
