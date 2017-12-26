import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
   'create' : 'CREATE',
   'destroy' : 'DESTROY'
}

tokens = [

    'NAME'

] + list(reserved.values())

t_ignore = ' '

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


def p_grids(p):
    '''
    grids : expression
    | empty
    '''
    print(p[1])

def p_object(p):
    '''
    object : NAME
    '''
    p[0] = p[1]

def p_create(p):
    '''
    expression : CREATE object NAME
    | DESTROY object NAME
    '''
    p[0] = (p[1], p[2], p[3])

def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)