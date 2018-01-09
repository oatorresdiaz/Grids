import ply.lex as lex
import ply.yacc as yacc
import handlers.window as Window
import handlers.draw as Draw
import handlers.sprite as Sprite
import handlers.grid as Grid
import sys

reserved = {
    'Create' : 'CREATE',
    'Destroy' : 'DESTROY',
    'Window' : 'WINDOW',
    'Grid' : 'GRID',
    'Sprite' : 'SPRITE',
    'Draw' : 'DRAW'
}

tokens = [

    'LP',
    'RP',
    'COMMA',
    'INT',
    'FLOAT',
    'STRING'

] + list(reserved.values())

t_LP = r'\('
t_RP = r'\)'
t_COMMA = r'\,'

t_ignore = ' '

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'[a-z]+\.[a-z]+'
    return t

def t_ID(t):
    r'[A-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


#------------------------------------------------------------------


def p_error(p):
    print(p)
    print("Syntax error found!")

def p_execute(p):
    '''
    execute : create
    | destroy
    | empty
    '''
    print(run(p[1]))

def p_object(p):
    '''
    object : WINDOW
    | GRID
    | SPRITE
    | DRAW
    '''
    p[0] = p[1] #Here we know what type of object is created. Modify later.

def p_create(p):
    '''
    create : CREATE object parameters
    '''
    p[0] = (p[1], p[2], p[3])

def p_destroy(p):
    '''
    destroy : DESTROY object
    '''
    p[0] = (p[1], p[2])

def p_parameters(p):
    '''
    parameters : LP parameter RP
    | LP parameter COMMA parameter RP
    | LP parameter COMMA parameter COMMA parameter RP
    | empty
    '''
    if len(p) == 4:
        p[0] = p[2]
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
    | STRING
    '''
    p[0] = p[1]

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
        if p[0] == 'Create':
            if p[1] == 'Window':
                 window = Window.Window("w1", p[2][0], p[2][1])
                 env['Window'] = window

            if p[1] == 'Grid':
                grid = Grid.Grid(p[2][0], p[2][1])
                grid.create()
                env['Grid'] = grid

            if p[1] == 'Sprite':
                sprite = Sprite.Sprite(p[2][0], p[2][1], p[2][2])
                sprite.create()
                env['Sprite'] = sprite

            if p[1] == 'Draw':
                window = env['Window']
                draw = Draw.Draw(window, env['Grid'])
                draw.draw(env['Sprite'], p[2][1], p[2][0])
                window.create()

        elif p[0] == 'Destroy':
            pass
            # if p[0] not in env:
            #     return 'Undeclared variable found!'
            # else:
            #     env.pop(p[2])
            #     print(env)
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)