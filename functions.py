from random import randint

def math_question(difficulty):          #asks a math question to determine success/failure of certain task
    if difficulty < 2:
        operation = randint(1, 2)       #difficulty can be >= 0
    elif difficulty < 4:
        operation = randint(1, 3)
    else:
        operation = randint(1, 4)

    number1 = randint(difficulty, 5*difficulty+2)
    
    if operation == 4:
        number2 = randint(1, difficulty+2)
    elif operation == 3:
        number2 = randint(0, 4*difficulty+2)
    else: 
        number2 = randint(0, 5*difficulty+2)

    if operation == 1:
        awnser = int(input(f"\nKolik je {number1} plus {number2}? "))
        if awnser == number1 + number2:
            print("Správná odpověď!\n")
            return True
        else:
            print("Špatná odpověď!\n")
            return False

    elif operation == 2:
        awnser = int(input(f"\nKolik je {number1} mínus {number2}? "))
        if awnser == number1 - number2:
            print("Správná odpověď!\n")
            return True
        else:
            print("Špatná odpověď!\n")
            return False

    elif operation == 3:
        awnser = int(input(f"\nKolik je {number1} krát {number2}? "))
        if awnser == number1 * number2:
            print("Správná odpověď!\n")
            return True
        else:
            print("Špatná odpověď!\n")
            return False

    elif operation == 4:
        awnser = float(input(f"\nKolik je {number1} děleno {number2} (zaokrouhlujte na tři desetinná místa, použijte tečku jako desetinnou čárku)? "))
        if awnser == round(number1 / number2, 3):
            print("Správná odpověď!\n")
            return True
        else:
            print("Špatná odpověď!\n")
            return False