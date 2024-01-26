import random as r

def display(map_list):
    map_displayed = ''
    for yelement in map_list:
        for xelement in yelement:
            map_displayed += str(xelement)
        map_displayed += '\n'
    return map_displayed

def player_movement(input,player_ycoor,player_xcoor, base_ymovement, base_xmovement):
    match (str(input)).lower():
        case 'z':
            player_ycoor -= 1
        case 'q':
            player_xcoor -= 1
        case 's':
            player_ycoor += 1
        case 'd':
            player_xcoor += 1
        case _:
            player_ycoor = player_ycoor + base_ymovement
            player_xcoor = player_xcoor + base_xmovement

    return player_ycoor, player_xcoor
    
def movement_checker(map,desired_entity_ycoor,desired_entity_xcoor):
    if map[desired_entity_ycoor][desired_entity_xcoor] == '*':
        global size, has_been_eaten
        size += 1
        has_been_eaten = True
        return True
    elif map[desired_entity_ycoor][desired_entity_xcoor] == ' ':
        return True
    return False

def move_entity(map,entity_type,desired_entity_ycoor,desired_entity_xcoor,entity_ycoor = None,entity_xcoor = None):
    if entity_ycoor != None and entity_xcoor != None:
        map[entity_ycoor][entity_xcoor] = ' '
    map[desired_entity_ycoor][desired_entity_xcoor] = str(entity_type)

class player():
    def __init__(self,icon):
        self.icon = icon
        

        
while True:

    graphics_map = [['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|'],\
                    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],\
                    ['|',' ','|',' ',' ',' ',' ',' ','|','-','-','-','-','-',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],\
                    ['|',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],\
                    ['|',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','-','-','-','-',' ',' ',' ',' ',' ',' ',' ','|',' ',' ','|',' ','|'],\
                    ['|',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ','|',' ','|'],\
                    ['|',' ','|','-','-','-',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ','|',' ','|'],\
                    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ','-','-','-','-','-',' ','|',' ','|'],\
                    ['|',' ',' ',' ',' ',' ',' ',' ','|','-','-','-','-','|',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],\
                    ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ','|',' ',' ',' ','|'],\
                    ['|',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ','-','-','-','|',' ',' ',' ','|',' ',' ','|',' ',' ',' ','|'],\
                    ['|',' ','-','-','|',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' ',' ',' ','|'],\
                    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],\
                    ['|',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ','|'],\
                    ['|','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','|']]
    
    P1 = player('o')
    P2 = player('°')
    
    base_ymovement = 1
    base_xmovement = 0
    
    turn = 0
    size = 0
    
    desired_player_ycoor = 0
    desired_player_xcoor = 0
    P2_ycoor, P2_xcoor = None, None
    player_ycoor = r.randint(2,12)
    player_xcoor = r.randint(2,27)
    while graphics_map[player_ycoor][player_xcoor] != ' ':
                player_ycoor = r.randint(2,12)
                player_xcoor = r.randint(2,27)
    graphics_map[player_ycoor][player_xcoor] = P1.icon
    
    player_movement_list = [[player_ycoor,player_xcoor]]
    
    food_ypos = r.randint(2,12)
    food_xpos = r.randint(2,27)
    has_been_eaten = False
    while graphics_map[food_ypos][food_xpos] != ' ':
        food_ypos = r.randint(2,12)
        food_xpos = r.randint(2,27)

    graphics_map[food_ypos][food_xpos] = '*'

    Title = 'LE TITRE'
    



    print (f'\n\n\n\n\n\n\n\n\n\n\n{Title}\n\n'+ display(graphics_map) + '\n\n')
    while True:
        if has_been_eaten == True:
            food_ypos = r.randint(2,12)
            food_xpos = r.randint(2,27)
            while graphics_map[food_ypos][food_xpos] != ' ':
                food_ypos = r.randint(2,12)
                food_xpos = r.randint(2,27)
            graphics_map[food_ypos][food_xpos] = '*'
            has_been_eaten = False
        previous_player_ycoor, previous_player_xcoor = player_ycoor, player_xcoor
        player_input = input().lower()
        match player_input:
            case 'r':
                break
            case 'e':
                exit()
            case 'g':
                size += 1
        if turn > 0 and size > 0:
            move_entity (graphics_map, P2.icon,player_movement_list[turn-1][0], player_movement_list[turn-1][1],P2_ycoor, P2_xcoor)
            P2_ycoor, P2_xcoor = player_movement_list[turn-size][0], player_movement_list[turn-size][1]
        
        desired_player_ycoor, desired_player_xcoor = player_movement(player_input,player_ycoor,player_xcoor,base_ymovement,base_xmovement)
        if movement_checker(graphics_map,desired_player_ycoor,desired_player_xcoor):
            move_entity (graphics_map, P1.icon, desired_player_ycoor, desired_player_xcoor,player_ycoor, player_xcoor)
            player_ycoor, player_xcoor = desired_player_ycoor, desired_player_xcoor
        else:
            print ('\n\n\n\n\n\n\n\n\n\n\n\n\n'+ 'YOU ARE DEAD' + '\n\n\n\n\n\n\n\n\n')
            print ('play again ? Y/N')
            match input().lower():
                case 'y':
                    break
                case _ :
                    exit()
        

            
        player_movement_list.append([player_ycoor,player_xcoor])

        base_ymovement = player_ycoor-previous_player_ycoor
        base_xmovement = player_xcoor-previous_player_xcoor
        turn += 1
        
        print ('\n\n\n\n\n\n\n\n\n\n\n' + display(graphics_map) + '\n\n\n')
