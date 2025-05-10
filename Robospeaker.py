import os 


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Harry")
    while True:
        x = input("Enter What you want me to speak: ")
        if x == "q":
            os.system("say 'Bye Bye freind'")
            break
        command = f"say {x}"
        os.system(command)