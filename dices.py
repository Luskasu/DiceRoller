import random
import os

class DiceRoller():
    def defrand(self):
        seed = int.from_bytes(os.urandom(4), byteorder='big') #semente de numeros aleatorios de uma fonte de entropia do so
        random.seed(seed)
        self.listHistory = [] #Lista com o historico de rolagens
        self.arquivo = open("rollhistory.txt", "a") #arquivo para armazenar a lista
    
    def dice(self, sides):
        self.defrand()
        Roll = random.randint(1, sides)
        return Roll
