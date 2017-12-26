import ply.lex as lex
import ply.yacc as yacc
import window.window as window
import sys

reserved = {
   'create' : 'CREATE',
   'destroy' : 'DESTROY',
}

tokens = [

    'NAME'

] + list(reserved.values())

t_ignore = ' '

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME') #checks for reserved words
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


def p_grids(p):
    '''
    grids : create
    | destroy
    | empty
    '''
    print(run(p[1]))

def p_object(p):
    '''
    object : NAME
    '''
    p[0] = p[1] #Here we know what type of object is created. Modify later.

def p_create(p):
    '''
    create : CREATE object NAME
    '''
    p[0] = (p[1], p[2], p[3])

def p_destroy(p):
    '''
    destroy : DESTROY object NAME
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
env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == 'create':
            env[p[2]] = p[1]
            print(env)
            return window.create()
        elif p[0] == 'destroy':
            if p[0] not in env:
                return 'Undeclared variable found!'
            else:
                env.pop(p[2])
                print(env)
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)