rows, cols = (6, 7)
arr = [[" " for i in range(cols)] for j in range(rows)]
end = False
#checks if someone wins in the whole board
def gameovercheck(arr, ch):
    #check horizontal  for win
    for c in range(cols - 3):
        for r in range(rows):
            if arr[r][c] == ch and arr[r][c + 1] == ch and arr[r][
                    c + 2] == ch and arr[r][c + 3] == ch:
                return True

    #check vertical for win
    for c in range(cols):
        for r in range(rows - 3):
            if arr[r][c] == ch and arr[r + 1][c] == ch and arr[
                    r + 2][c] == ch and arr[r + 3][c] == ch:
                return True

    #check pos sloped diaganols
    for c in range(cols - 3):
        for r in range(rows - 3):
            if arr[r][c] == ch and arr[r + 1][c + 1] == ch and arr[r + 2][
                    c + 2] == ch and arr[r + 3][c + 3] == ch:
                return True

    #check neg sloped diaganols
    for c in range(cols - 3):
        for r in range(3, rows):
            if arr[r][c] == ch and arr[r - 1][c + 1] == ch and arr[r - 2][
                    c + 2] == ch and arr[r - 3][c + 3] == ch:
                return True

#print the board
def printb():

    #array to string
    for i in range(6):
        listToStr = ' '.join(map(str, arr[i]))
        print("[" + listToStr + "]")
    print("===============")
    print(" A B C D E F G ")

# get input and place the piece
def player(ch, player):
    col = ((input("What column do you want " + player + ": ")))
    x = 5
    if col == "a" or col == "A": col = 0
    if col == "b" or col == "B": col = 1
    if col == "c" or col == "C": col = 2
    if col == "d" or col == "D": col = 3
    if col == "e" or col == "E": col = 4
    if col == "f" or col == "F": col = 5
    if col == "g" or col == "G": col = 6
    while arr[x][col] != " " and x >= 0:
        x = x - 1
    if arr[x][col] == " ":
        arr[x][col] = ch
    printb()
    if (gameovercheck(arr,ch)):
      print("Congrats " +player + " you WIN!!!")
      quit()
        

print("")
print(
    "Welcome to CONNECT 4! Enter the letter (doesn't need to be capital) that corresponds with the column you want to place your piece "
)
print("")
printb()
p1 = input("Enter your name player 1: ")
p2 = input("Enter your name player 2: ")
print("Let the game begin!")

turns = 1
while (turns <= 42):
    if turns % 2 != 0:
        player("o", p1)

    else:
        player("x", p2)
    turns = turns + 1
if turns > 42:
    print("DRAW!")
