import random
import os
import time
os.system('clear')
#Tittle
game=1
while game==1:
 game-=1
 try:
  print("==================")
  print("==Guess A Number==")
  print("==================")
#Maximum,minimum number and max round
  x = int(input("Silahkan input Angka Minimum: "))
  y = int(input("Silahkan input Angka Maksimum: "))
  round = int(input("Silahkan input maksimal Tebakan: "))

  number = random.randint(x , y)#System pick  number
  ronde = 1
  os.system("clear")
  while ronde <= round :
   try : 
    print("===================")
    print(f'======Ronde {ronde}======')
    print("===================")
    print(f'Angka Minimum: {x}')
    print(f'Angka Maksimum: {y}')
    guess = int(input("Tebak Angka: "))
    if guess == number :
     print("===============")
     print("==Kamu Menang==")
     print("===============")
     break
    else :
      if guess > number :
       print("Terlalu Besar")
       ronde += 1
       time.sleep(1)
       os.system("clear")
      else:
       print("Terlalu Kecil")
       ronde += 1
       time.sleep(1)
       os.system("clear")
   
   except :
    print("Input Number!")
    if True: 
     time.sleep(1)
     os.system("clear")
     
   if ronde > round:
    print("======================================")
    print(f'Kamu Kalah angkanya adalah {number}')
    print("======================================")
 except:
   print("Input Number!")
   time.sleep(1)
   os.system("clear")
   game+=1






 
