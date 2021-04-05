#название игры в терминале
pres = """ 
           x    x   ooo        ggg      aa      m       m     eee
            x  x   o   o      g        a  a     m m   m m    e   
             xx    o   o      g  gg   aaaaaa    m  m m  m    eeeee
            x  x   o   o      g   g   aaaaaa    m   m   m    e   
           x    x   ooo        ggg    a    a    m       m     eee   
                                                                    """

print(pres)
#Приглашаем пользователя  погирать
print("Lets play in XXX & OOO")
print("Игрок1 играет Х Игрок2 О")
#sozdau pole
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_field(field):
    print (".............")
    for i in range(3):
        print("|", field[0 + i*3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print (".............")
# vrianty vvoda

# obrabotka vvoda
def player_input(player_tok):
    valid = False
    while not valid:
        player_move = input("Where to move" + player_tok + "?")
        try:
            player_move = int(player_move)
        except:
            print ("Are you sure you entered the number?")
            continue
        if player_move >=1 and player_move <=9:
            if (str(field[player_move - 1]) not in "XO"):
                field[player_move - 1] = player_tok  
                valid = True
            else:
                print("This cell is not empty!")
        else:
            print("Incorrect input! Please enter a number from 1 to 9.")

# proverka gobedy
def check_win(field):
    win_variant = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for variant in win_variant:
        if field[variant[0] == variant[1] == variant[2]]:
            return field[variant[0]]
    return False

#funktsiya igry
def main(field):
    counter = 0
    win = False
    while not win:
        print_field(field)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print (tmp, "YOU WIN!!!")
                win = True
                break
        if counter == 9:
            print("DRAW!!!")
            break
    print_field(field)

main(field)

input("Press ENTER for exit")
















