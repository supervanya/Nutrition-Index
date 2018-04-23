import getpass
import db
import sys
import traceback
import render
from classes import *




# ---- HELPING HANDS (undocumented)
def log_in():
    # returns user name after logging in or creating an account

    user_name = helper.press_any_key(s ="Enter your username: " )
    user_name = user_name[0].upper()+user_name[1:]

    # get the password returns None if can't find such user_name
    password_encrypted = db.fetch_password(user_name)

    # try to login if user_name exists (password_encrypted == True)
    if password_encrypted:
        helper.print_with_line(texts.password_existing.format(user_name), 
        title="Log in", n = 0, ref = True)
        real_password = db.decrypt(password_encrypted[0])
        helper.press_any_key(s ="Enter your ", inp = False)
        password_entered = getpass.getpass()

        # set the number of tries for the user
        tries = 3
        while password_entered != real_password:
            if tries == 0:
                helper.simple_print("☠ RIP! Sorry, take a break, you might remember it later! ︎")
                helper.pause(2)
                helper.simple_print(texts.bye)
                sys.exit()
            tries -=1
            helper.press_any_key(
                s ="⚠︎ Wrong pass, {} more try(-ies) > ".format(tries+1), 
                inp = False)
            password_entered = getpass.getpass()

        #greet the user with success menu
        helper.print_with_line("{} you are logged in!".format(user_name), 
            title="Success!", n = 0, ref = True)
        helper.pause()

    # if user not in database, will create one
    else:
        # greet the user and invite to create password
        helper.print_with_line(
            texts.password_new.format(user_name),
            title="Log in", n = 0, ref = True)

        # get a new password from the user
        helper.press_any_key(
            "Looks like you are new here! Let's create a password\n",
            inp = False)

        # check that password match
        while True:
            helper.press_any_key(s ="Enter your ", inp = False)
            password_entered1 = getpass.getpass()
            helper.press_any_key(s ="Repeat the ", inp = False)
            password_entered2 = getpass.getpass()
            print("\n")
            if password_entered1 != password_entered2:
                print("The passwords don't match. Try agin!")
                continue
            break
            
        gender = helper.press_any_key(s ="Your gender: ", inp = True)
        age     = helper.press_any_key(s ="Your age: ", inp = True)
        password = password_entered1
        db.create_user(user_name, gender, age, password)
        helper.print_with_line("{} your profile is created!".format(user_name), 
            title="Success!", n = 0, ref = True)
        helper.pause()
        
    return user_name

def close(user_id):
    name = db.get_user_name(user_id)[0]
    text = texts.bye_named.format(name)
    helper.simple_print(text)
    sys.exit()

def error(answer,message=texts.invalid):
    error = message.format(answer)
    title = "Error!"
    helper.print_menu(error, title, response=0)
    helper.press_any_key()
    # helper.pause(1.5)

def menu(text, title):
    answer = helper.print_menu(text, title)
    return (answer)

def run_menu(user_id,menu_text,menu_name,func_map):
    # prints menu and calls sub-menus

    # print menu window
    answer = menu(menu_text, menu_name)

    # call sub-menus based on input or error
    if answer in func_map:
        func_map[answer](user_id)
    elif answer == 'back':
        return
    else:
        error(answer)
        return




# ---- MAIN MENU
def main_menu(user_id):
    run_menu(user_id,texts.menu,"Main menu",main_map)




# ---- SUB MENU HANDLERS
# this is explore menu
def sub_menu_1(user_id):
    run_menu(user_id, texts.sub_menu_1, "Explore foods", sub_menu_1_map)

# this is VIZ menu
def sub_menu_2(user_id):
    run_menu(user_id, texts.sub_menu_2, "Analyze and Vizualize", sub_menu_2_map)

# this is the logging menu
def sub_menu_3(user_id):
    helper.print_menu(texts.sub_menu_3, "History", response = 0)
    helper.press_any_key()
    db.fetch_nutrient(user_id = user_id, nutrients = ['ndbno','name'],limit = 15, printing = True)

    while  True:
        ndbno = helper.press_any_key(texts.sub_menu_3_line_1, inp = True)
        if ndbno == 'back':
            return
        if ndbno == 'logs':
            db.fetch_nutrient(user_id = user_id, nutrients = ['ndbno','name'],limit = 15, printing = True)
        elif ndbno == 'exit':
            close(user_id)
        else:
            try:
                food = Food(ndbno)
                db.log_food(food.data, user_id)
            except:
                error(ndbno)



# ---- FUNCTIONS FROM SUB MENU 1 FOODS LOOKUP
def print_food(user_id):
    print(look_up_foods(user_id))
 
def look_up_foods(user_id):
    # asking for a food name until success or exit:

    # get the list of foods
    ndbnos_list = get_ndbnos_list()

    # print the list of foods
    print_ndbnos_list(ndbnos_list)
    
    # get number from user
    ndbno = choose_food(ndbnos_list)

    food = Food(ndbno)
    return food

def get_ndbnos_list():
    # ask for a choice
    while True:
        search_term = helper.press_any_key(s ="\nEnter food name?\n> ", inp = True)
        ndbnos_list = fetch_ndbnos_list(search_term)
        if ndbnos_list:
            return ndbnos_list
        error(search_term)

def print_ndbnos_list(ndbnos_list):
    for i,food in enumerate(ndbnos_list,1):
        print("[{}] {}".format(i,helper.wrap(food['name'])))
        helper.pause(0.05)

# def choose_food(ndbnos_list): # TODO fix ID
#     # ask for a choice
#     while True:
#         food_number = helper.press_any_key(s ="\nEnter # or 'back')\n> ", inp = True)
#         if food_number <= len(ndbnos_list) + 1:
#             ndbno = ndbnos_list[food_number-1]['ndbno']
#             return ndbno
#         error(food_number)

def choose_food(ndbnos_list): # TODO fix ID
    # ask for a choice
    while True:
        food_number = helper.press_any_key(s ="\nEnter # or 'back')\n> ", inp = True)
        try:
            ndbno = ndbnos_list[int(food_number)-1]['ndbno']
            return ndbno
        except:
            error(food_number)

def compare_foods(user_id):
    print("choose food #1")
    food1 = look_up_foods(user_id)

    print("choose food #2")
    food2 = look_up_foods(user_id)
    
    food1.compare_to(food2)

# ---- FUNCTIONS FROM SUB MENU 2
d = maps.RNP 

def analyze_foods_sugar(user_id):
    sugars = db.fetch_nutrient(user_id, nutrients = [d['Sugars']]) 
    render.bar_graph(sugars, name = "Sugar Graph over Time")

def analyze_foods_protein(user_id):
    proteins = db.fetch_nutrient(user_id, nutrients = [d['Protein']]) 
    render.bar_graph(proteins, name = "Protein Graph over Time")

def analyze_foods_index(user_id):
    indexes   = db.fetch_nutrient(user_id, nutrients = ['Index']) 
    render.bar_graph(indexes, name = "Health Index over Time")

def analyze_foods_sugars_index(user_id):
    indexes   = db.fetch_nutrient(user_id, nutrients = ['Index',d['Sugars']]) 
    render.bar_graph(indexes, name = "Health Index over Time")


# ---- FUNCTIONS FROM SUB MENU 3
def view_hitory_log():
    print("view_hitory_log")
    pass



# ---- HANDLES THE FLOW HERE
def run():
    # greeet
    helper.print_with_line(texts.welcome)
    # log in 
    user_name = log_in()
    # get user id
    user_id   = db.get_user_id(user_name)

    while True:
        main_menu(user_id)




# ---- DICT MAPPING
# dictionaty - map of functions to user input 
# calling them by func[func_name](params)
main_map        = {   
                    '1'     :sub_menu_1,
                    '2'     :sub_menu_2,
                    '3'     :sub_menu_3,
                    'exit'  :close
                }

sub_menu_1_map  = {   
                    '1'     :print_food,
                    '2'     :compare_foods,
                    'exit'  :close
                }

sub_menu_2_map  = {   
                    '1'     :analyze_foods_sugar,
                    '2'     :analyze_foods_protein,
                    '3'     :analyze_foods_index,
                    '4'     :analyze_foods_sugars_index,
                    'exit'  :close
                }


def minitest(ndbno,user_id):
    foo_bar = Food(ndbno)
    db.log_food(foo_bar.data, user_id)

if __name__=="__main__":
    run()
    # while True:
    #     look_up_foods(25)
    

