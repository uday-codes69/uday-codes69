import random
computer = random.choice([1,2,0])
print(computer)
youstr = input("enter your choice: ")
reverseDict = {1:"Snake", 2:"Water", 0:"Gun"}

youDict = {"s":1, "w": 2 ,"g":0}

you= youDict[youstr]

print(f"You choose: {reverseDict[you]}\nComputer choose:{reverseDict[computer]}]")

if(computer == you):
    print("Its a Draw")
    
else:
    
    if(computer ==0 and you==1):
        print("You  Lose")
        
    elif(computer ==0 and you==2):
        print("You  Win")
        
    elif(computer ==1 and you==0):
        print("You Win")
        
    elif(computer==1 and you==2):
        print("You Lose")

    elif(computer == 2 and you==1):
        print("You Win")
        
    elif(computer == 2 and you==0):
        print("You Lose")
        


    else:
        print("Something went wrong")
