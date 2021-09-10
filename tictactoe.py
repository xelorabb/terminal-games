#!/usr/bin/env python

import os
from yatts import *

# Clears the terminal
def _cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Styles the tooltip numbers
def _tt(n):
    return style(' ' + str(n) + ' ', 236, bgc, italic=True)

# Styles the player symbols
def _ps(s):
    color = xc if s == ' x ' else oc
    return style(s, color, bgc)

def _empty_field():
    return [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

# Creates a game rows
def _create_row(n):
    row = ''

    for i in n:
        row += vline
        if type(i) == int:
            row += _tt(i)
        elif type(i) == str:
            row += _ps(i)

    row += vline + '\n'

    return row

# Prints the game field
def _show_field():
    n1 = _create_row(field[0])
    n2 = _create_row(field[1])
    n3 = _create_row(field[2])

    return f_top + n1 + f_middle + n2 + f_middle + n3 + f_bottom

# Places a x or a o to the field
def _place_symbol(n, m):
    err = ''
    if not field[n][m] == ' x ' and not field[n][m] == ' o ':
        field[n][m] = ' x ' if player == 1 else ' o '
    else:
        err = 'Field occupied'
    return err

# Checks if a player wins
def _check_victory():
    v1 = all(n==field[0][0] for n in field[0]) # 1. row
    v2 = all(n==field[1][0] for n in field[1]) # 2. row
    v3 = all(n==field[2][0] for n in field[2]) # 3. row

    v4 = all(m==field[0][0] for m in [n[0] for n in field]) # 1. col
    v5 = all(m==field[0][1] for m in [n[1] for n in field]) # 2. col
    v6 = all(m==field[0][2] for m in [n[2] for n in field]) # 3. col

    # top left to bottom right
    v7 = field[0][0] == field[1][1] and field[1][1] == field[2][2]

    # top right to bottom left
    v8 = field[0][2] == field[1][1] and field[1][1] == field[2][0]

    return v1 or v2 or v3 or v4 or v5 or v6 or v7 or v8

# Checks if a possible move is available
def _check_stalemate():
    stalemate = True
    for i in range(0,3):
        for j in range(0,3):
            if stalemate:
                stalemate = (field[i][j] == ' x ' or field[i][j] == ' o ')
    return stalemate

error = ''
c = 'yellow'
bgc = 'black'
xc = 'green'
oc = 'red'
player = 2
field = _empty_field()

f_top = style('┌───┬───┬───┐', c, bgc, bold=True) + '\n'
f_bottom = style('└───┴───┴───┘', c, bgc, bold=True) + '\n'
f_middle = style('├───┼───┼───┤', c, bgc, bold=True) + '\n'
vline = style('│', c, bgc, bold=True)

# Game loop
while True:
    _cls()
    print(style(' Tic Tac Toe ', decorations=['bold', 'underline', 'overline']))
    print(_show_field())

    vic = _check_victory()
    stalemate = _check_stalemate()

    if vic or stalemate:
        msg = 'Player ' + str(player)
        if stalemate:
            msg = 'Nobody'

        pi = input('\n' + msg + ' wins! continue? (y/n): ')
        if pi == 'y':
            field = _empty_field()
            continue
        else:
            break
    else:
        if error == '':
            player = 2 if player == 1 else 1

        print(error)
        error = ''

        pi = input('Player ' + str(player) + ' (1-9): ')

        if pi == '1':
            error = _place_symbol(0,0)
        elif pi == '2':
            error = _place_symbol(0,1)
        elif pi == '3':
            error = _place_symbol(0,2)
        elif pi == '4':
            error = _place_symbol(1,0)
        elif pi == '5':
            error = _place_symbol(1,1)
        elif pi == '6':
            error = _place_symbol(1,2)
        elif pi == '7':
            error = _place_symbol(2,0)
        elif pi == '8':
            error = _place_symbol(2,1)
        elif pi == '9':
            error = _place_symbol(2,2)
        elif pi == 'q':
            break
        else:
            error = 'Wrong input'
            continue
