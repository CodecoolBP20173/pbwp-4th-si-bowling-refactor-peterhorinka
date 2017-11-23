def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for turn in range(len(game)):
        if game[turn] == '/':
            result += 10 - last
        else:
            result += get_value(game[turn])
       
        if frame < 10  and get_value(game[turn]) == 10:
            if game[turn] == '/':
                result += get_value(game[turn + 1])
            elif game[turn].lower() == 'x' :
                result += get_value(game[turn + 1])
                if game[turn + 2] == '/':
                    result += 10 - get_value(game[turn + 1])
                else:
                    result += get_value(game[turn + 2])
        
        last = get_value(game[turn])
        
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[turn].lower() == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    nums = ["1","2","3","4","5","6","7","8","9"]
    
    if char in nums:
        return int(char)
    elif char.lower() == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
