n = int(input("What Size Game GoPy?"))
numbers = [number for number in range(n**2)]  # value of board


def choose_number():  # display to board
    for i in range(n):  # number of rows of board
        for x in numbers[i*n:i*n+n]:  # number of column board
            if numbers.index(x) < 10:
                print("", x, end=" ")
            else:
                print(x, end=" ")
        print()  # new line


def control_area(position):
    temp_matrix = []
    for i in range(n):
        position_matrix = []
        if position == 1:
            for x in numbers[i*n:i*n+n]:  # create list with horizontal areas
                position_matrix.append(x)
        elif position == 2:
            for x in numbers[i:n**2:n]:  # create list with vertical areas
                position_matrix.append(x)
        elif position == 3:
            for x in numbers[i:n**2:n+1]:  # create list with left_diagonal areas
                position_matrix.append(x)
        elif position == 4:
            for x in numbers[n-1:n**2-1:n-1]:  # create list with right_diagonal areas
                position_matrix.append(x)
        temp_matrix.append(position_matrix)
    for j in temp_matrix:
        if j.count('X') == n:
            print("winner: X")
            return True
        elif j.count('O') == n:
            print("winner: O")
            return True


def control_board():
    if control_area(1):  # 1 is value of horizontal areas
        return True
    elif control_area(2):  # 2 is value of vertical areas
        return True
    elif control_area(3):  # 3 is value of left_diagonal areas
        return True
    elif control_area(4):  # 4 is value of right_diagonal areas
        return True
    elif numbers.count('X') + numbers.count('O') == n**2:
        print("No winner")
        return True


choose_number()  # start game
while True:
    k = int(input("Player 1 turn--> "))  # Player1 select one cell
    Q = ['X']
    if k < 0 or k >= n**2:
        print("Please enter a valid number")
        pass
    elif numbers[k:k+1] == ['X']:
        print("You have made this choice before")
        pass
    elif numbers[k:k+1] == ['O']:
        print("The other player select this cell before")
        pass
    else:
        numbers[k:k+1] = Q  # update board
        choose_number()  # display new board
        if control_board():  # end of the loop
            break
    m = int(input("Player 2 turn--> "))  # Player2 select one cell
    P = ['O']
    if m < 0 or m >= n**2:
        print("Please enter a valid number")
        pass
    elif numbers[m:m+1] == ['O']:
        print("You have made this choice before")
        pass
    elif numbers[m:m+1] == ['X']:
        print("The other player select this cell before")
        pass
    else:
        numbers[m:m+1] = P  # update board
        choose_number()  # display new board
        if control_board():  # end of the loop
            break
