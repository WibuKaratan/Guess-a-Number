import random
import os
import time
os.system('clear')
#Tittle
z=1
while z==1:
 z-=1
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
    print(f'Kamu Kalah angkanya adalah {number}')
 except:
   print("Input Number!")
   time.sleep(1)
   os.system("clear")
   z+=1
