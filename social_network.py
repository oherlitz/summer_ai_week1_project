#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui
import random



#Create instance of main social network object
ai_social_network = SocialNetwork()
Personn = Person()
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    people = {}

    while True: 
        if choice == "1":
            print("1. Create Account")
            print("2. Log In")
            user_choice = input("Pick a number. ")
            

            if user_choice == "1":
                print("\nYou are now in the create account menu")
                n , a = ai_social_network.create_account()
                
                y = len(people)

                people[y] = n + " and " + a
                
            if user_choice == "2":
                print("You are now in the log in menu")
                na = input('Type your name. ')
                ag = input('Type your age. ')
                info = na + " and " + ag
                x = 0
                for i in people:
                    if people[x] == info:
                        print("Logged in")
                        n = na
                        a = ag
                        break
                    x += 1
        elif choice == "2":
            while True:
                inner_menu_choice = social_network_ui.manageAccountMenu()
                #Handle inner menu here

                if inner_menu_choice == "1":
                    print(f"Your current name is {n} and you are {a} years old.")
                    print("1. To change name")
                    print("2. To change age")
                    print("Anything else. To exit")
                    user_choice = input("What would you like to change? ")
                    if user_choice == "1":
                        n = input("What would you like your new name to be? ")
                        break

                    elif user_choice == "2":
                        a = input("What would you like your new age to be? ")
                        break

                    else:
                        break

                elif inner_menu_choice == "2":
                    
                    Personn.add_friend(input("What is the name of the friend that you would like to add? "))

                elif inner_menu_choice == "3":
                    Personn.displayfriends()

                elif inner_menu_choice == "4":
                    print("1. To send a message. ")
                    print("2. To view messages. ")
                    choice = input("Pick a number. ")
                    if choice == "1":
                        Personn.displayfriends()
                        z = 0
                        receiver = input("Who would you like to send your message to (enter their info in the format 'name and age'? ")
                        message = n + " sent " + input("What message would you like to send ")

                        for i in people[z]:
                            if i == receiver:
                                print("Message sent.")
                                break
                            z += 1

                    if choice == "2":
                        if receiver == n + " and " + a:
                            print(message)
                        else:
                            print("No messages")
                elif inner_menu_choice == "5":
                    print(people)
                else:
                    break

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
