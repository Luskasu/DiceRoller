import os, time
from dices import DiceRoller

class Table():
    def __init__(self):
        self.rollerins = DiceRoller()
        
    def readDice(self, die: str):
        self.numDices = ""
        self.numSides = ""
        jafoiod = False
        hasmod = False
        self.typemod = 0
        mod = ""
        
        #exceptions conhecidas
        self.noDieSet = False #o usuário não informou o dado
        self.poolOverRange = False #o usuário pediu mais de 100 rolagens
        self.invalidSyntax = False #o usuário não escreveu no formato xdy (e/ou escreveu alguma atrocidade no lugar)
        
        for i in die:
            if i == "d":
                jafoiod = True
            
            #vai ser arrumado ainda, a ideia é verificar se o usuário informou algo
            # diferente de um numero ou de vazio antes do "d" pra ficar padronizado com os outros erros
            '''if not jafoiod and not i.isdigit() and not i == "d":
                print("error, invalid die")
                return 0, 0, 0 
            
            '''
            if not jafoiod and i.isdigit(): #adiciona o char do numero de dados na string
                self.numDices += i
            if jafoiod and i.isdigit() and not hasmod: #adiciona o char do numero de lados na string
                self.numSides += i
            if jafoiod and len(self.numSides) > 0: #verifica se há modificador
                if i == "+" or i == "-":
                    hasmod = True
                    if i == "+": self.typemod = 1
                    if i == "-": self.typemod = -1

            if hasmod and i.isdigit():
                mod += i
            
        

        
        if hasmod: modInt = int(mod)
        else: modInt = 0
        
        #se o numero de rolagens não for informado, transforma em 1
        if self.numDices == "":
            numDicesInt = 1
        else:
            numDicesInt = int(self.numDices)
        
        #se o numero de lados estiver vazio identifica o erro
        if not jafoiod:
            self.invalidSintax = True
            
        if self.numSides == "":
            self.noDieSet = True
            numSidesInt = 0
        else:
            numSidesInt = int(self.numSides)
        
        #se o numero fo maior que 100
        if numDicesInt > 100 or numDicesInt < 1:
            self.poolOverRange = True
            

        
        return numDicesInt, numSidesInt, modInt
    
    def roller(self, selectedDie):
        som = 0
        j=0
        numDicesInt, numSidesInt, modInt = self.readDice(selectedDie)
        
        #Verifica se tem erro 
        if not self.noDieSet and not self.poolOverRange and not self.invalidSyntax:
            print("\nrolling {}\n".format(option))
        
            #fazendo as rolagens em si
            while j < numDicesInt:
                lastRoll = self.rollerins.dice(numSidesInt)
                print("  *{}".format(lastRoll))
                som += lastRoll
                j += 1
            som += modInt * self.typemod
            #verifica se tiver mais de uma rolagem ou se tem mod. 
            # se for o caso, soma tudo
            if j > 1 or modInt != 0:
                if self.typemod > 0: print("Modfier: +{}".format(modInt))
                if self.typemod < 0: print("Modfier: -{}".format(modInt))
                print("\n{} in total\n".format(som))
            print("")
        
        #caso de rolagem inválida
        if self.noDieSet:
            print("\nERROR: There's no die set for {}! select a valid one (ex d6, d8...).".format(option))
        if self.poolOverRange:
            print("\nERROR:{} is out of range! Select a valid amount (max 100 dice).".format(numDicesInt))
        if self.invalidSyntax:
            print("\nERROR: invalid syntax! What does {} purport to mean? Use the format below!.".format(numDicesInt))
            


#chamadas:
print("\n\n\n\n\n-----------------------------------------------------------------------------")
print("|  _                    _      ___  _          ___     _ _           _   __  |")
print("| | |  _  _ ___ __ __ _( )___ |   \(_)__ ___  | _ \___| | |___ _ _  / | /  \ |")
print("| | |_| || (_-</ _/ _` |/(_-< | |) | / _/ -_) |   / _ \ | / -_) '_| | || () ||")
print("| |____\_,_/__/\__\__,_| /__/ |___/|_\__\___| |_|_\___/_|_\___|_|   |_(_)__/ |")
print("|                                                                            |")
print("-----------------------------------------------------------------------------\n")

table1 = Table()

while True:
    print("Enter your die roll (format ex: 3d6), Max 100d100 or type 'help' to an explication")
    
    option = input().lower().strip()
    
    if option == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nWelcome to the dice roller! Here you can roll virtual rpg dice\n")
        print("To do a die roll just type xdy where x is the amount of dice and y is the number of faces\nfor example, 1d20 to roll one twenty sided die (at a maximum 100d100)\n You can also include an modfier to your dice throw by typing '+' or '-' following by a int number\nEX 6d6+6 if you want to roll 6d6 and add 6 to result or 1d20-10 to roll one twenty sided die and subtract 10 to final result\n\n\n") 
    
    elif option == "exit":
        print("\n\n\n\n\n--------------------------------------------------------")
        print("|   _____                           /\//\/|            |")
        print("|  / ____|                         |/\//\/             |")
        print("| | (___   ___  ___   _   _  __ _                      |")
        print("|  \___ \ / _ \/ _ \ | | | |/ _` |                     |")
        print("|  ____) |  __/  __/ | |_| | (_| |                     |")
        print("| |_____/ \___|\___|  \__, |\__,_|                     |")
        print("|                      __/ |                           |")
        print("                     |___ /                            |")
        print("--------------------------------------------------------\n")
        break
    
    else:
        table1.roller(option)
    