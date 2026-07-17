import random

num=random.randint(1,10)
tries=0

while True:
    guess=int(input("pleass guess your number :"))
    if guess==num:
        tries+=1
        print(f"you are right your  guessed the number is {tries} tries")
        break
    
    elif num < guess:
        tries+=1
        print("lower number")

    elif num > guess:
        tries+=1
        print("higher number")
        
    else:
        tries+=1
        print("sorry your number wrong")
print("adil")