import random
bullets = (1, 2, 3, 4, 5, 6)
print("""Welcome To Roulette!""")
roundnum = 0
bulletlocation = random.choice(bullets)
choice = input("""Select Mode
1. SinglePlayer (IN PROGRESS (NOT WORKING))
2. Multiplayer""")
shoot1 = input('1st Shot')
if choice == '2':
    if shoot1 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()
    shoot2 = input('2nd Shot')
    if shoot2 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

    shoot3 = input('3rd Shot')
    if shoot3 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

    shoot4 = input('4th Shot')
    if shoot4 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

    shoot5 = input('5th Shot')
    if shoot5 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

    shoot6 = input('6th Shot')
    if shoot6 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

#SECOND SECTION

if choice == '1':
    if shoot1 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()
    if shoot1 == '.':
        shoot2 == '.'
    if shoot2 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You Survived!")
        quit()

    shoot3 = input('3rd Shot')
    if shoot3 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()
    if shoot3 == '.':
        shoot4 == '.'
    if shoot4 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You Survived!")
        quit()

    shoot5 = input('5th Shot')
    if shoot5 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You got Shot!")
        quit()

    shoot6 = input('6th Shot')
    if shoot6 == ('.'):
        roundnum = roundnum + 1
    if roundnum == bulletlocation:
        print("You Survived!")
        quit()