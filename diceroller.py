import random
import math
def  diceroller():
  return math.floor(random.random()*6)+1
c='y'
print("Welcome to the dice roller :)")
while c== 'y' or c=='Y':
  print("The dice rolled a : ",diceroller())
  c=input('Do you want to roll again? (y/n)')