"""
This is a Tic Tac Toe program here you choose how many positions and wins conditions there are. The code for winning
is put into variables and test to check the win condition.
"""
while True:
    try:
        x = int(input("\nHow many x-by-x do you want?: "))
        if x == 0:
            raise KeyError
        # I made it so 10 is the maximum just so the console doesn't get too cluttered.
        if x > 10:
            raise IndexError
        # I made so you can't put less the a 2 x 2 in because it's impossible for the other player to win.
        if x <= 2:
            raise ArithmeticError
        break
    except ArithmeticError:
        print("\nThat's too low of a number.")
    except (ValueError, NameError):
        print("\nYou must enter a whole number.")
    except KeyError:
        print("\nYou cannot have zero positions.")
    except IndexError:
        print("\nThat's way too many positions.")
while True:
    try:
        y = int(input("\nHow many spaces in a row would you like for the win condition: "))
        # again I a made it so the win condition can't be 2 so that both the players have a chance.
        if y <= 2:
            raise IndexError
        # I made it so there isn't more positions than x^2 so that you can actually win.
        if y > x:
            raise ArithmeticError
        break
    except ArithmeticError:
        print("\nThere can't be more win conditions than their are spaces.")
    except IndexError:
        print("\nThat's too low of a number.")
    except:
        print("\nYou must enter a whole number.")
# These are all the variables needed for the program (plus x and y).
symbol1 = "X"
symbol2 = "O"
index = x**2
board_values = ["-"]*index
recursion = 0
# switch changes who goes first. If switch equals 1, symbol 1 goes first and vice versa.
switch = 1


# This is where I show the board.
def board(index):
    for i in range(index):
        if (i % x) == 0:
            print()
        print(board_values[i], end=" ")


# This function allows the user to put in the position to put their symbol.
def turn():
    while True:
        try:
            position = int(input("\n\nChoose you're position: ")) - 1
            if board_values[position] == symbol1 or board_values[position] == symbol2:
                raise IndexError
            if position <= -1 or position > index:
                raise IndexError
            break
        except NameError:
            print("\nYou must pick a position on the board.")
        except ValueError:
            print("\nYou must pick a postion on the board.")
        except IndexError:
            print("\nYou cannot pick this spot.")
    return position


# This function chooses who's currently playing.
def symbol():
    global switch
    if switch == 2:
        switch = 1
        return symbol2
    else:
        switch = 2
        return symbol1


# This is where the bul of my time went. I made 3 functions for deciding win/. This first one is deciding if X or O
# is directly below each other.
def win1(recursion):
    c = []
    for i in range(x):
        if (board_values[i*x+recursion] != board_values[i*x+recursion-x]) or (board_values[i*x+recursion] == "-"):
            c = []
            c += board_values[(i*x)+recursion]
        else:
            c += board_values[(i*x)+recursion]
        if len(c) == y and "-" not in c:
            if switch == 1:
                board(index)
                print(f"\n{symbol2} wins!")
                quit()
            else:
                board(index)
                print(f"\n{symbol1} wins!")
                quit()
        if i == 2:
            if recursion != x-1:
                # I used recursion in order to find the other verticals in row.
                win1(recursion+1)
            else:
                return


# This function is for deciding if an X or O is at the right of each other.
def win2(recursion):
    c = []
    for i in range(x):
        if (board_values[i+recursion] != board_values[i+recursion-1]) or (board_values[i+recursion] == "-"):
            c = []
            c += board_values[i+recursion]
        else:
            c += board_values[i+recursion]
        if len(c) == y and "-" not in c:
            if switch == 1:
                board(index)
                print(f"\n{symbol2} wins!")
                quit()
            else:
                board(index)
                print(f"\n{symbol1} wins!")
                quit()
        if i + 1 == x:
            if recursion+x != index:
                win2(recursion+x)
            else:
                return


# This function is testing one part the the diagonal.
def win3(recursion):
    c = []
    e = []
    for i in range(x):
        if i == x-1 and recursion > 0:
            return
        if (board_values[(x+1)*i+recursion] != board_values[((x+1)*i)-(x+1)+recursion]) or \
                (board_values[(x+1)*i+recursion] == "-"):
            c = []
            c += board_values[(x+1)*i+recursion]
        else:
            c += board_values[(x+1)*i+recursion]
        if i <= x-2:
            if (board_values[(-x+(x-2))-(x+1)*i-recursion] != board_values[(-x+(x-2))-(x+1)*i+(x+1)-recursion]) or \
                    (board_values[(-x+(x-2))-(x+1)*i-recursion] == "-"):
                e = []
                e += board_values[(-x+(x-2))-(x+1)*i-recursion]
            else:
                e += board_values[(-x+(x-2))-(x+1)*i-recursion]
        if len(e) == y:
            if switch == 1:
                board(index)
                print(f'\n{symbol2} wins!')
                quit()
            else:
                board(index)
                print(f"\n{symbol1} wins!")
                quit()
        if len(c) == y:
            if switch == 1:
                board(index)
                print(f"\n{symbol2} wins!")
                quit()
            else:
                board(index)
                print(f'\n{symbol1} wins!')
                quit()
        if i == x - 2:
            if recursion == x-2:
                return
            else:
                win3(recursion+1)


# This function is for checking the other part of the diagonals.
def win4(recursion):
    d = []
    f = []
    for i in range(x):
        if recursion != x - 1:
            if (board_values[(x-1)+(x-1)*i-recursion] != board_values[((x-1)+(x-1)*i)-(x-1)-recursion]) or \
                    (board_values[(x-1)+(x-1)*i-recursion] == "-"):
                d = []
                d += board_values[(x-1)+(x-1)*i-recursion]
            else:
                if recursion == x -2 and i == 2:
                    pass
                else:
                    d += board_values[(x-1)+(x-1)*i-recursion]
        if recursion != x - 1:
            if (board_values[(-x+1)-(x-1)*i+recursion] != board_values[(-x+1)-(x-1)*i+(x-1)+recursion]) or \
                    (board_values[(-x+1)-(x-1)*i+recursion] == "-"):
                f = []
                f += board_values[(-x+1)-(x-1)*i+recursion]
            else:
                f += board_values[(-x+1)-(x-1)*i+recursion]
                # This function is to make sure 2 symbol's aren't in the same line.
                if (((-x+1)-(x-1)*i+recursion) % x) == 0:
                    f = []
                    f += board_values[(-x + 1) - (x - 1) * i + recursion]
        if len(d) == y and "-" not in d:
            if switch == 1:
                board(index)
                print(f'\n{symbol2} wins!')
                quit()
            else:
                board(index)
                print(f'\n{symbol1} wins!')
                quit()
        if len(f) == y and "-" not in f:
            if switch == 1:
                board(index)
                print(f"\n{symbol2} wins!")
                quit()
            else:
                board(index)
                print(f"\n{symbol1} wins!")
                quit()
        if i == x-1:
            if recursion < y:
                win4(recursion+1)
            else:
                return


# This is my main loop for running the game.
while True:
    board(index)
    try:
        board_values[turn()] = symbol()
    except IndexError:
        print("You must pick a number on the board.")
    win1(recursion)
    win2(recursion)
    win3(recursion)
    win4(recursion)
    if board_values.count("-") == 0:
        board(index)
        print("\nIt's a tie!")
        break
