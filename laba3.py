from random import randint


def proc31():
    slovo = []
    while (word := str(input())) !="stop":
        slovo.append(word)
    print(" ".join(slovo))
proc31()



def proc32():
 slovo = input("введите слово:")
 for i in range(len(slovo)):
    if slovo[i]=="Ф" or slovo[i]=="ф":
        print("Слово редкое")
        break
    else:
        print("Слово обычное")
        break
proc32()



def proc33():
    k = 0
    print("Чтобы завершенить игру, введите stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        if res == "stop":
            break

        res = int(res)
        if a+b == res:
            print("Правильно!")
        else:
            print("Ответ неправильный :(")
            k += 1
        if k == 3:
           print('игра окончена')
           break
proc33()



