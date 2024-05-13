# SANTIAGO, MARC STEPHEN R. CS-1202 ----- MIDTERM LAB EXAM ------ VIDEO GAME RENTAL SYSTEM  
import sys

game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    "GTA Vice City": {"quantity": 4, "cost": 4},
    "NFS Most Wanted": {"quantity": 4, "cost":5}
}

user_accounts = {}
admin_username = "admin"
admin_password = "adminpass"


def display_games():
    print("---------------------------------------------------")
    print("Available Games:\n")
    for index, game in enumerate(game_library, start=1):
        quantity = game_library[game]["quantity"]
        cost = game_library[game]["cost"]
        print(f"{index}. {game} - Copies available: {quantity} - Cost: ${cost}")
    print("---------------------------------------------------\n")
    
def register():
    while True:
        print("\n-----------REGISTER NEW USER-----------")
        print("Please input your username and password: \n")
        username = str(input("Enter a username: "))
        password = str(input("Password (must be 8 characters long): "))
        if len(username) < 4:
            print("\n*******************************************")
            print("Username must be at least 4 characters long.")
            print("********************************************")
            break

        while len(password) < 8:
            print("\n*******************************************")
            print("Password must be at least 8 characters long.")
            print("*******************************************\n")
            password = input("Password (must be 8 characters long): ")
            break

        if username in user_accounts:
            print("\n------------------------------------------------------------")
            print("Username already exists. Please choose a different username.")
            print("------------------------------------------------------------\n")
            break
        else:
            print("\n-------------------------------")
            print("Account registered successfully")
            print("-------------------------------\n")
            user_bal = 0
            user_pts = 0

            user_accounts[username] = {
                "username": username,
                "password": password,
                "Balance": user_bal,
                "Points": user_pts,
                "games_rented": {}
            }
            menu()  
            break


def userlogin():
    while True:
        print("----------LOGIN PAGE----------\n")
        username = str(input("Username: "))
        password = str(input("Password: "))
        if username in user_accounts and user_accounts[username]["password"] == password:
            print("\n----------------")
            print("Login Successful")
            print("----------------\n")
            user_menu(username)
        else:
            print("\n****************************")
            print("Invalid username or password")
            print("****************************\n")
            break
        
def user_menu(username):
    while True:
        try: 
            print(f"Logged in as {username} ---- Balance: ${user_accounts[username]['Balance']}")
            print("1. Rent a game")
            print("2. Return a game")
            print("3. Top-up Account")
            print("4. Display inventory")
            print("5. Redeem free game rental")
            print("6. Check Credentials")
            print("7. Log out\n\n")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                rent_game(username)
            elif choice == 2:
                return_game(username)
            elif choice == 3:
                top_up(username)
            elif choice == 4:
                inventory(username)
            elif choice == 5:
                redeem(username)
            elif choice == 6:
                check_credentials(username)
            elif choice == 7:
                print("\n----------------------------------")
                print(f"  User: '{username}' has logged out!")
                print("----------------------------------\n")
                menu()
                break
            else:
                print("\n***************************")
                print("Please input a valid choice")
                print("***************************\n")
        except ValueError:
            print("\n***************************")
            print("Please input a valid number")
            print("***************************\n")
            user_menu(username)

def adminlogin():
    while True:
        print("------------------")
        print("ADMIN LOGIN PAGE")
        print("------------------\n")
        admin_user = input("Username: ")
        admin_pass = input("Password: ")

        if admin_user == admin_username and admin_pass == admin_password:
            print("\n-----------------")
            print("Login Successful!")
            print("-----------------\n")
            admin_menu()
             
        else:
            print("\n******************************")
            print("Incorrect username or password")
            print("******************************\n")
            break


def admin_menu():
    while True:
        try:
            print("Admin Menu") 
            print("1. Update Game Details")
            print("2. Log out\n")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                admin_update_game()
            elif choice == 2:
                print("ADMIN LOGGED OUT!")
                menu()
                break
            else:
                print("\n***************************")
                print("Please input a valid choice")
                print("***************************\n")
                admin_menu()
                break
                
        except ValueError:
            print("\n***************************")
            print("Please input a valid number")
            print("***************************\n")
            admin_menu()

def admin_update_game():
            print("Update Game ")
            print("1. Update Game Copies")
            print("2. Update Game Price")
            print("3. Log out\n\n")
            
            try: 
                choice = int(input("Enter your choice: ")) 
                
                if choice == 1:
                    display_games()
                    game_index = int(input("Select the number of the game to be updated: "))
                    for index, game in enumerate(game_library, start=1):
                        index = int(index)
                        if game_index == index:
                            game_name = game
                            if game_name in game_library:
                                updated_copies = int(input(f"Enter the updated copies for {game_name}: "))
                                game_library[game_name]["quantity"] = updated_copies
                                print(f"\nUpdated {game_name}'s copies to {updated_copies}\n")
                                break
                                
                    else:  
                        print("\n***************************")
                        print("Please enter a valid number")
                        print("***************************\n")
                        admin_update_game()

                        
                elif choice == 2:
                    display_games()
                    game_index = int(input("Select the number of the game to be updated: "))
                    for index, game in enumerate(game_library, start=1):
                        index = int(index)
                        if game_index == index:
                            game_name = game
                            if game_name in game_library:
                                updated_price = int(input(f"Enter the updated price for {game_name}: "))
                                game_library[game_name]["cost"] = updated_price
                                print(f"\nUpdated {game_name}'s price to {updated_price}\n")
                                break
                    else:
                        print("\n***************************")
                        print("Please enter a valid number")
                        print("***************************\n")
                        admin_update_game()
                        
                elif choice == 3:
                    print("\n------------------")
                    print("ADMIN LOGGED OUT!")
                    print("------------------\n")
                    menu()
                else:
                    print("\n***************************")
                    print("Please input a valid choice")
                    print("***************************\n")
                    admin_update_game()              
            except ValueError:
                print("\n***************************")
                print("Please input a valid number")
                print("***************************\n")
                admin_update_game()

def top_up(username):
    try:
        print("\n-----Top-up Account-----\n")
        amount = input("Enter the amount to top up (leave blank to cancel transcation): ")
        if amount == "" or amount == " ":
            print("\n--------------------------------------------------------")
            print("                TRANSACTION CANCELLED")
            print("--------------------------------------------------------\n")
            return
        else:
            amount = float(amount)
            if amount > 0:
                user_accounts[username]["Balance"] += amount
                print("\n------------------------------------------------------")
                print(f"      Top-up successful. New balance: ${user_accounts[username]['Balance']}")
                print("------------------------------------------------------\n")
            else:
                print("\nInvalid amount. Please enter a positive value.\n")
                return
    except ValueError:
        print("\nInvalid input. Please enter a valid amount.\n")

def inventory(username):
    print("\n-------------------------------------------")
    print(f"       Inventory for User: {username}\n")
    if user_accounts[username]["games_rented"] == {}:
        print("\n!!! You haven't rented any games yet !!!")
        print("-------------------------------------------\n")
    else:
        for game_name, quantity in user_accounts[username]["games_rented"].items():
            print(f"{game_name} - Copies rented: {quantity}")
        print("-------------------------------------------\n")

def redeem(username):
    if user_accounts[username]["Points"] >= 3:
        display_games()
        try:
            game_index = input("Select the number of the game you want to redeem for free: ")
            if game_index == "" or game_index == " ":
                    print("\n--------------------------------------------------------")
                    print("                TRANSACTION CANCELLED")
                    print("--------------------------------------------------------\n")
                    return
            else:
                game_index = int(game_index)
                for index, game in enumerate(game_library, start=1):
                    if game_index == index:
                        game_name = game
                        if game_library[game_name]["quantity"] > 0:
                            user_accounts[username]["Points"] -= 3
                            game_library[game_name]["quantity"] -=1
                            if game_name in user_accounts[username]["games_rented"]:
                                user_accounts[username]["games_rented"][game_name] += 1
                            else:
                                user_accounts[username]["games_rented"][game_name] = 1
                            print("\n-----------------------------------------------------------------")
                            print(f"Successfully redeemed {game_name} for free. Remaining points: {user_accounts[username]['Points']}")
                            print("-----------------------------------------------------------------\n")
                            return
                        else:
                            print("\n!!! Sorry, no copies available for renting !!!\n")
                else:
                    print("\n!!! Input a valid number !!!\n")
        except ValueError:
            print("\n***************************")
            print("Please enter a valid number")
            print("***************************\n")
            redeem(username)
    else:
        print("\n****************************************************************")
        print("You need at least 3 points in order to avail the free game rental.")
        print("****************************************************************\n")
        
            
def rent_game(username):
    display_games()
    try:
        game_index = input("Please select the number of the game to rent (leave blank to cancel): ")
        if game_index == "" or game_index == " ":
            print("\n--------------------------------------------------------")
            print("                TRANSACTION CANCELLED")
            print("--------------------------------------------------------\n")
            return
        else:
            game_index = int(game_index)
            for index, game in enumerate(game_library, start=1):
                if game_index == index:
                    game_name = game     

                    if game_library[game_name]["quantity"] > 0:
                        cost = game_library[game_name]["cost"]

                        if user_accounts[username]["Balance"] >= cost:
                            print("\n-----------------------------------------------------------")
                            print(f"{game_name} rented successfully.")
                            game_library[game_name]["quantity"] -= 1
                            user_accounts[username]["Balance"] -= cost
                            
                            gained_points = cost // 2 
                            user_accounts[username]["Points"] += gained_points
                            print(f"Gained {gained_points} point(s).")
                            
                            if game_name in user_accounts[username]["games_rented"]:
                                user_accounts[username]["games_rented"][game_name] += 1
                            else:
                                user_accounts[username]["games_rented"][game_name] = 1
                            print("-----------------------------------------------------------\n")
                        else:
                            print("\n**************************************")
                            print("Insufficient balance to rent the game.")
                            print("**************************************\n")
                    else:
                        print("\n***********************************")
                        print("The selected game is not available.")
                        print("***********************************\n")
                    break 
            else:
                print("\n*******************************************************")
                print("Please enter a valid game choice from the game library.")
                print("*******************************************************\n")
    except ValueError:
        print("\n************************************************")
        print("Invalid input. Please enter a valid game number.")
        print("************************************************\n")
        rent_game(username)


def return_game(username):
    if "games_rented" in user_accounts[username] and user_accounts[username]["games_rented"]:
        print("\n--------------------------------------------------")
        print("                  Games Rented:\n")
        for index, (game, quantity) in enumerate(user_accounts[username]["games_rented"].items(), start=1):
            print(f"{index}. {game} -- Rented Copies: {quantity}")  
        print("--------------------------------------------------\n")  
        
        try:
            game_index = input("Please select the number of the game that you want to return (leave blank to cancel): ")
            if game_index == "" or game_index == " ":
                print("\n--------------------------------------------------------")
                print("                TRANSACTION CANCELLED")
                print("--------------------------------------------------------\n")
                return
            else:
                game_index = int(game_index)
                for index, (game, quantity) in enumerate(user_accounts[username]["games_rented"].items(), start=1):
                    index = int(index)
                    if game_index == index:
                        game_name = game
                        if game_name in user_accounts[username]["games_rented"]:
                            game_library[game_name]["quantity"] += 1
                            user_accounts[username]["games_rented"][game_name] -= 1
                            
                            if user_accounts[username]["games_rented"][game_name] == 0:
                                del user_accounts[username]["games_rented"][game_name]     
                            if user_accounts[username]["games_rented"] == {}:
                                user_accounts[username]["games_rented"] = {}
                            
                            print("\n-------------------------------------------------------")
                            print(f"You returned {game_name} successfully.")
                            print("-------------------------------------------------------\n")
                            break  
                else:
                    print("\n********************")
                    print("Invalid game choice.")
                    print("********************\n")
                    return_game(username)
        except ValueError:
            print("\n************************************************")
            print("Invalid input. Please enter a valid choice.")
            print("************************************************\n")
            return_game(username)
    else:
        print("\n-------------------------------------------")
        print("\n!!! You haven't rented any games yet !!!\n")
        print("-------------------------------------------\n")
            
            
def check_credentials(username):
            print("\n------------------- User Credentials -------------------")
            print(f"Username: {username}")
            print(f"Password: {user_accounts[username]["password"]}")
            
            if user_accounts[username]["games_rented"] == {}:
                print("Game Inventory: You haven't rented any games yet!")
            else:
                print("Game Inventory: ")
                for game_name, quantity in user_accounts[username]["games_rented"].items():
                    print(f"--------{game_name} - Quantity: {quantity}")
                
            print(f"Balance: $ {user_accounts[username]['Balance']}")
            print(f"Points: {user_accounts[username]['Points']} point(s)")
            print("-------------------------------------------------------\n")
            
def menu():
    while True:
        try:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("           Welcome to the Video Game Rental System!")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("1. Display Available Games")
            print("2. Register User")
            print("3. Log in")
            print("4. Admin Log in")
            print("5. Exit Program\n")

            choice = int(input("Enter your choice: "))
            print("\n")

            if choice == 1:
                display_games()
            elif choice == 2:
                register()
            elif choice == 3:
                userlogin()
            elif choice == 4:
                adminlogin()
            elif choice == 5:
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("      Thank you for using this video game rental system!")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                sys.exit()
            else:
                print("\n***************************")
                print("Please input a valid number")
                print("***************************\n")
        except ValueError:
            print("\n***************************")
            print("Please input a valid choice")
            print("***************************\n")

menu()