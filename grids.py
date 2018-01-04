import ply.lex as lex
import ply.yacc as yacc
import handlers.window as Window
import sys

reserved = {
   'create' : 'CREATE',
   'destroy' : 'DESTROY',
    'handlers' : 'WINDOW',
    'grid' : 'GRID',
    'sprite' : 'SPRITE'
}

tokens = [

    'NAME',
    'LEFTPAR',
    'RIGHTPAR',
    'COMMA',
    'INT',
    'FLOAT'

] + list(reserved.values())

t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_COMMA = r'\,'

t_ignore = ' '

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

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
    object : WINDOW
    | GRID
    | SPRITE
    '''
    p[0] = p[1] #Here we know what type of object is created. Modify later.

def p_create(p):
    '''
    create : CREATE object NAME parameters
    '''
    p[0] = (p[1], p[2], p[3])

def p_destroy(p):
    '''
    destroy : DESTROY object NAME
    '''
    p[0] = (p[1], p[2], p[3])

def p_parameters(p):
    '''
    parameters : LEFTPAR parameter RIGHTPAR
    | LEFTPAR parameter COMMA parameter RIGHTPAR
    | LEFTPAR parameter COMMA parameter COMMA parameter RIGHTPAR
    | empty
    '''
    if len(p) == 3:
        p[0] = p[1]
    elif len(p) == 6:
        p[0] = (p[2], p[4])
    elif len(p) == 8:
        p[0] = (p[2], p[4], p[6])
    else:
        p[0] = None

def p_parameter(p):
    '''
    parameter : INT
    | FLOAT
    | NAME
    '''
    p[0] = p[1]

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
            window = Window.Window('Grids', 500, 500)
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