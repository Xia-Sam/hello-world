import random

rand_str=""
list=['0','1','2','3','4','5','6','7','8','9']
random.shuffle(list)
for i in range(4):
  rand_str=rand_str+list[i]
#print(rand_str)
def getinput():
  user_input=input("please input four digits:  ")
  while user_input.isdigit()==False or len(user_input)!=4:
    user_input=input("Wrong! Pls input four digits.")
  return user_input

count=0

while True:
  Bulls,Cows=0,0
  user_input=getinput()
  count=count+1
  for i in range(4):
    if user_input[i] in rand_str:
      Bulls=Bulls+1
      if user_input[i]!=rand_str[i]:
        Cows=Cows+1

  print(Bulls,"A",Cows,"B")

  if Bulls==4 and Cows==0:
    print("You win. Attempts:",count)
    break
