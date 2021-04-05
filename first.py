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
#sozdau pole
field = [1,2,3,4,5,6,7,8,9]
def print_field(field):
    print (".............")
    for i in range(3):
        print("|", field[0 + i*3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print (".............")

print_field(field)





