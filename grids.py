import ply.lex as lex
import ply.yacc as yacc
import handlers.window as Window
import handlers.draw as Draw
import handlers.sprite as Sprite
import handlers.grid as Grid
import handlers.controller as Controller
import handlers
import sys
import traceback as tb

reserved = {
    'Create' : 'CREATE',
    'Destroy' : 'DESTROY',
    'Window' : 'WINDOW',
    'Grid' : 'GRID',
    'Sprite' : 'SPRITE',
    'Draw' : 'DRAW',
    'Start' : 'START',
    'Add' : 'ADD',
    'WinPos' : 'WINPOS',
    'Controller' : 'CONTROLLER'
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
    | start
    | append
    | empty
    '''
    print(run(p[1]))

def p_object(p):
    '''
    object : WINDOW
    | GRID
    | SPRITE
    | CONTROLLER
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

# def p_draw(p):
#     '''
#     draw : DRAW parameters
#     '''
#     p[0] = (p[1], p[2])

def p_start(p):
    '''
    start : START
    '''
    p[0] = p[1],

def p_append(p):
    '''
    append : ADD WINPOS parameters
    '''
    p[0] = (p[1], p[2], p[3])

def p_parameters(p):
    '''
    parameters : LP parameter RP
    | LP parameter COMMA parameter RP
    | LP parameter COMMA parameter COMMA parameter RP
    | LP parameter COMMA parameter COMMA parameter COMMA parameter RP
    | empty
    '''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 6:
        p[0] = (p[2], p[4])
    elif len(p) == 8:
        p[0] = (p[2], p[4], p[6])
    elif len(p) == 10:
        p[0] = (p[2], p[4], p[6], p[8])
    else:
        p[0] = None

def p_parameter(p):
    '''
    parameter : INT
    | FLOAT
    | STRING
    | LP parameter COMMA parameter RP
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 6:
        p[0] = (p[2] , p[4])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()
env = {}
gb = {}
winPos = []

def run(p):
    global env
    global gb
    global winPos
    if type(p) == tuple:
        if p[0] == 'Create':
            if p[1] == 'Window':
                 window = Window.Window("w1", p[2][0], p[2][1])
                 env['Window'] = window

            if p[1] == 'Grid':
                grid = Grid.Grid(p[2][0], p[2][1])
                grid.create()
                env['Grid'] = grid
                for x in range(p[2][0]):
                    for y in range(p[2][1]):
                        gb[str(x) + ',' + str(y)] = 'empty'

            if p[1] == 'Sprite':
                sprite = Sprite.Sprite(p[2][0], p[2][1], p[2][2], 'center')
                sprite.create()
                env[p[2][0]] = sprite

            if p[1] == 'Controller':
                controller = Controller.Controller(env['Window'], env['Grid'], gb, winPos)
                controller.draw.drawGrid()
                env['Controller'] = controller

            if p[1] == 'Draw':
                controller = env['Controller']
                controller.drawIfLeftMouseClickedAndNoOverlapping2(env[p[2][0]], env[p[2][1]])

        # elif p[0] == 'Draw':
        #     window = env['Window']
        #     draw = Draw.Draw(window, env['Grid'])
        #     draw.draw(env[p[1][0]], p[1][1], p[1][2])

        elif p[0] == 'Add':
            if len(p[2]) == 2:
                winPos.append((str(p[2][0][0]) + ',' + str(p[2][0][1]), str(p[2][1][0]) + ',' + str(p[2][1][1])))
                print(winPos)
            elif len(p[2]) == 3:
                winPos.append((str(p[2][0][0]) + ',' + str(p[2][0][1]), str(p[2][1][0]) + ',' + str(p[2][1][1]),
                               str(p[2][2][0]) + ',' + str(p[2][2][1])))
                print(winPos)
            elif len(p[2]) == 4:
                winPos.append((str(p[2][0][0]) + ',' + str(p[2][0][1]), str(p[2][1][0]) + ',' + str(p[2][1][1]),
                               str(p[2][2][0]) + ',' + str(p[2][2][1]), str(p[2][3][0]) + ',' + str(p[2][3][1])))

        elif p[0] == 'Start':
            env['Controller'].start()

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
    try:
        parser.parse(s)
    except Exception:
        tb.print_exc()
        #print('TypeError: some command was incorrectly typed.')