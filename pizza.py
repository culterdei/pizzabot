import sys, re
from ast import literal_eval

# Pizzabot moving function - comparing current coordinates with next and moving accordingly
def move_pizza(input_string:str):
    input_list = input_string.split(' ')
    points = input_list[1:]
    current_point = (0, 0)
    mov_seq = []
    for point in points:
        point = literal_eval(point)
        # X axis
        if current_point[0] > point[0]:
            mov_seq.append('W'*(current_point[0] - point[0]))
        elif current_point[0] < point[0]:
            mov_seq.append('E'*(point[0] - current_point[0]))
        else:
            pass
        # Y axis
        if current_point[1] > point[1]:
            mov_seq.append('S'*(current_point[1] - point[1]))
        elif current_point[1] < point[1]:
            mov_seq.append('N'*(point[1] - current_point[1]))
        else:
            pass
        current_point = point
        mov_seq.append('D')
    return ''.join(mov_seq)

if __name__ == '__main__':
    
    # Mapping to function
    cmd = {'pizzabot': move_pizza}

    # Pizzabot arguments count check
    if len(sys.argv) < 2:
        print('Not enought arguments')
        sys.exit()

    # Pizzabot command check
    if sys.argv[1] != 'pizzabot':
        print(f'It"s {sys.argv[1]}, not an pizzabot')
        sys.exit()

    # Pizzabot arguments validation through regex
    if not re.search('^\d{1,}x\d{1,}([ ]?\(\d{1,},\d{1,}\)[ ]?){1,}$', sys.argv[2]):
        print('Invalid pizzabot arguments - please, provide with following pattern: _x_ (_,_) (_,_) (_,_)...')
        sys.exit()
    
    print(cmd[sys.argv[1]](sys.argv[2]))
