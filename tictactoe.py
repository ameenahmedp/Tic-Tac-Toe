def displayboard(nums):
    print('\n'*100)
    print('  '+ '(1)' +' | '+ '(2)' +' | '+ '(3)')
    print('      |     | ')
    print("--------------------")
    print('  '+ '(4)' +' | '+ '(5)' +' | '+ '(6)')
    print('      |     | ')
    print("--------------------")
    print('  '+ '(7)' +' | '+ '(8)' +' | '+ '(9)')
    print('      |     | ')
    print('\n'*2)

    print('  '+ nums[0]+'   |  '+ nums[1]+'  |   '+ nums[2])
    print('      |     |   ')
    print("--------------------")
    print('  '+ nums[3]+'   |  '+ nums[4]+'  |   '+ nums[5])
    print('      |     |   ')
    print("--------------------")
    print('  '+ nums[6]+'   |  '+ nums[7]+'  |   '+ nums[8])
    print('      |     |   ')
    return nums

def player_input_marker():
    player1 = ''
    while player1 != 'X' or player1 != 'O':
        player1 = input("Choose your option ('X' or 'O'): ").upper()
        if player1 == 'X':
            player2='O'
            break
        elif player1 == 'O':
            player2='X'
            break
        else:
            print("Wrong choice, select 'X' or 'O': ")
            print('\n')
    return (player1,player2)  

def player_input_position(marker,i):
    point = 10
    while point not in range(1,10):
        if i % 2 == 0:
            print('\n')
            point = input(f"Player1 ({marker}), Choose your position [1,9]: ")
            if point.isdigit() and int(point) in range(1,10):
                break
            else:
                print("Wrong choice, select from range (1,9): ")
        else:
            print('\n')
            point = input(f"Player2 ({marker}), Choose your position [1,9]: ")
            if point.isdigit() and int(point) in range(1,10):
                break
            else:
                print("Wrong choice, select from range [1,9]: ")
    return int(point)

def place_marker(nums, player, point):
    nums[point-1]=player
    return nums

def check_win(nums,marker):
    if  nums[0] == marker and nums[1] == marker and nums[2] == marker:
        return True
    if  nums[3] == marker and nums[4] == marker and nums[5] == marker:
        return True
    if  nums[6] == marker and nums[7] == marker and nums[8] == marker:
        return True

    if  nums[0] == marker and nums[3] == marker and nums[6] == marker:
        return True
    if  nums[1] == marker and nums[4] == marker and nums[7] == marker:
        return True
    if  nums[2] == marker and nums[5] == marker and nums[8] == marker:
        return True

    if  nums[0] == marker and nums[4] == marker and nums[8] == marker:
        return True
    if  nums[2] == marker and nums[4] == marker and nums[6] == marker:
        return True
    else:
        return False

def player_input_newgame():
    newgame = ''
    while newgame != 'Y' or newgame != 'N':
        print('\n')
        newgame = input("Do you want to play ('Y' or 'N'): ").upper()
        print('\n')
        if newgame == 'Y':
           tictactoe()
        elif newgame == 'N':
            exit()
        else:
            print("Wrong choice, select 'Y' or 'N': ")
    return newgame 

def tictactoe():
    board = [' '] * 9
    position=[]
    marker1, marker2 = player_input_marker()
    print('\n')
    print('  '+ '(1)' +' | '+ '(2)' +' | '+ '(3)')
    print('      |     | ')
    print("--------------------")
    print('  '+ '(4)' +' | '+ '(5)' +' | '+ '(6)')
    print('      |     | ')
    print("--------------------")
    print('  '+ '(7)' +' | '+ '(8)' +' | '+ '(9)')
    print('      |     | ')

    for i in range(0,9):
        if i % 2 == 0:
            pos = player_input_position(marker1,i)
            while pos in position:
                print("Position already chosen, choose other one")
                pos = player_input_position(marker1,i)
            position.append(pos)
            board = displayboard(place_marker(board,marker1,position[i]))
            result = check_win(board,marker1)
            if result:
                print('\n')
                print(f"PLAYER1 ({marker1}) WON !!!!")
                player_input_newgame()
        else:
            pos = player_input_position(marker2,i)
            while pos in position:
                print("Position already chosen, choose other one")
                pos=player_input_position(marker2,i)
            position.append(pos)
            board=displayboard(place_marker(board,marker2,position[i]))
            result = check_win(board,marker2)
            if result:
                print('\n')
                print(f"PLAYER2 ({marker2}) WON !!!!")
                player_input_newgame()
    print('\n')   
    print("It was a DRAW !!!")
    player_input_newgame()


player_input_newgame()

