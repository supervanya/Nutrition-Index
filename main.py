from nutri_fetch import *
import getpass
import db
import render

def interractive_get_index(search_term = None, ndbno = None):
    # getting the id of the food of interest
    if search_term == None and ndbno == None:
        ndbnos_list = None
        while ndbnos_list == None and ndbnos_list != 'exit':
            ndbnos_list = fetch_ndbnos_list()
            ndbno = ndbnos_list[0]
            if ndbnos_list == None:
                helper.print_with_line(texts.not_found, ref = False)
            if ndbnos_list == 0:
                return
    if search_term:
        ndbnos_list = fetch_ndbnos_list(search_term)
        ndbno = ndbnos_list[0]

    # getting the nutrition data
    data = fetch_nutrition(ndbno)
    name = str(data['name'])
    index = round(data['health_index'])

    if index > 400:
        emoji = "🤩🤩🤩🌱"
        percent = "|████████|"
    elif index >= 100:
        emoji = "🤩"
        percent = "|██████░░|"
    elif index >= 50:
        emoji = "😋"
        percent = "|████░░░░|"
    elif index >=0:
        emoji = "😐"
        percent = "|██░░░░░░|"
    elif index >= -150:
        emoji = "🤮"
        percent = "|█░░░░░░░|"
    else:
        emoji = "🤢"
        percent = "|░░░░░░░░|"

    helper.print_with_line(texts.hlth_index.format(name,repr(index),percent,emoji), title="Health Index ®", n = 0, ref = True)
    answer = helper.press_any_key(s =texts.after_index, inp = True)

    try:
        # ndbnos_list[1] - list of NDBNOS returned
        answer = int(answer)
        print(answer,"got int:")
        ndbno = ndbnos_list[1][type(answer)-1]
        print(ndbno)
        interractive_get_index(ndbno)
    except:
        # if user enters log - return 1 as first tuple and data as second tuple
        if answer.lower() == "log":
            print(answer,"got log:")
            return data
        # if user enters exit return 0
        elif answer.lower() == 'exit':
            print(answer,"got 'exit':")
            helper.simple_print(texts.bye)
            return None
        else:
            print(answer,"got nothing:")
            # return the search parameter
            interractive_get_index (search_term = answer)

def log_in():
    # returns user name after logging in or creating an account

    user_name = helper.press_any_key(s ="Enter your username: " )
    user_name = user_name[0].upper()+user_name[1:]
    password = db.fetch_password(user_name)

    if password:
        helper.print_with_line(texts.password_existing.format(user_name), 
        title="Log in", n = 0, ref = True)
        real_password = list(password)[0]
        # print(real_password)
        helper.press_any_key(s ="Enter your ", inp = False)
        password_entered = getpass.getpass()
        while password_entered != real_password:
            helper.press_any_key(s ="Wrong pass, try again? ", inp = False)
            password_entered = getpass.getpass()
        helper.print_with_line("{} you are logged in!".format(user_name), 
            title="Success!", n = 0, ref = True)
        helper.pause()
    # if user not in database, will create one
    else:
        helper.print_with_line(texts.password_new.format(user_name), 
        title="Log in", n = 0, ref = True)
        helper.press_any_key("Looks like you are new here! Let's create a password\n",False)
        while True:
            helper.press_any_key(s ="Enter your ", inp = False)
            password_entered1 = getpass.getpass()
            helper.press_any_key(s ="Repeat the ", inp = False)
            password_entered2 = getpass.getpass()
            print("\n")
            if password_entered1 != password_entered2:
                print("The passwords don't match. Try agin!")
                continue
            else:
                gender = helper.press_any_key(s ="Your gender: ", inp = True)
                age     = helper.press_any_key(s ="Your age: ", inp = True)
                password = password_entered1
                db.create_user(user_name, gender, age, password)
                helper.print_with_line("{} your profile is created!".format(user_name), 
                    title="Success!", n = 0, ref = True)
                helper.pause()
                break
    return user_name

def main():
    helper.print_with_line(texts.welcome)
    user_name   = log_in()
    user_id     = db.get_user_id(user_name)
    while True:
        helper.print_with_line(texts.menu, ref=False)
        answer = helper.press_any_key(s ="Enter your choice\n> ", inp = True)
        try:
            if answer == '1':
                data    = interractive_get_index()
                if data:
                    db.log_food(data, user_id)
            elif answer == '2':
                ndbno = input("Enter food's NDBNO or select from Favorites:\n> ")
                data = nutri_fetch.fetch_nutrition(ndbno)
                print(data, user_id)
                db.log_food(data, user_id)
            elif answer == '3':
                helper.print_with_line(texts.vizualization_3)
                sub_choice = helper.press_any_key(s ="Enter your choice > ", inp = True)
                if sub_choice == '1':
                    indexes = db.fetch_nutrient(user_id, nutrients = ['Index']) 
                    render.bar_graph(indexes, name = "Health Index over Time")
                elif sub_choice == '2':
                    sugar   = db.fetch_nutrient(user_id, nutrients = ['269']) 
                    render.bar_graph(sugar, name = "Sugar Graph over Time")
                elif sub_choice == '3':
                    data   = db.fetch_nutrient(user_id, nutrients = ['269', 'Index']) 
                    render.bar_graph(data)
            elif answer == 'exit':
                helper.simple_print(texts.bye)
                break
        except:
            continue

    # show options to chose from (USE Twitter's template)
    # 1. Look up foods
        # while True:
            # if # interractive_get_index():
            
    # 2. Log foods
    # 3. Analyze my diet
        # Index
            # db.fetch_nutrient(user_id, nutrients = ['Index'])
        # Sugar
            # db.fetch_nutrient(user_id, nutrients = ['269'])



    # db.log_food(data, user_id)

main()