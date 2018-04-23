from nutri_fetch import *
import getpass
import db
import sys
import traceback
import render


def interractive_get_index(search_term = None, ndbno = None, user_id=0):
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
    db.save_food(data)

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
    answer = helper.press_any_key(s =texts.after_index, inp = True, n = 0.004)

    try:
        answer = int(answer)
        while True:
            # ndbnos_list[1] - list of NDBNOS returned
            print("got int:", answer)
            print(ndbnos_list)
            print(ndbnos_list[1])
            print(ndbnos_list[1][int(answer)-1])
            ndbno = ndbnos_list[1][int(answer)-1]['ndbno']
            print(ndbno)
            interractive_get_index(ndbno=ndbno)
    except:
        # if user enters log - return data as second tuple
        if answer.lower() == "log":
            print(answer,"got log:") ########
            db.log_food(data, user_id)
            return data
        # if user enters exit return 0
        elif answer.lower() == 'back':
            print(answer,"got 'back':") ########
            return None
        elif answer.lower() == 'exit':
            print(answer,"got 'exit':") ########
            helper.simple_print(texts.bye)
            sys.exit()
        else:
            print("got search term:", answer) ########
            # return the search parameter
            interractive_get_index (search_term = answer)


def log_in():
    # returns user name after logging in or creating an account

    user_name = helper.press_any_key(s ="Enter your username: " )
    user_name = user_name[0].upper()+user_name[1:]
    password_encrypted = db.fetch_password(user_name)

    if password_encrypted:
        helper.print_with_line(texts.password_existing.format(user_name), 
        title="Log in", n = 0, ref = True)
        real_password = db.decrypt(password_encrypted[0])
        # print(real_password)
        helper.press_any_key(s ="Enter your ", inp = False)
        password_entered = getpass.getpass()
        n = 3
        while password_entered != real_password:
            if n == 0:
                helper.simple_print("☠ RIP! Sorry, take a break, you might remember it later! ︎")
                helper.pause(2)
                helper.simple_print(texts.bye)
                sys.exit()
            n-=1
            helper.press_any_key(s ="⚠︎ Wrong pass, {} more try(-ies) > ".format(n+1), inp = False)
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
        helper.print_with_line(texts.menu, ref=True, n=0, title="Main menu")
        answer = helper.press_any_key(s ="Enter your choice\n> ", inp = True)
        try:
            if answer == '1':
                data    = interractive_get_index()
                print(data)

            elif answer == '2':
                db.fetch_nutrient(user_id = user_id, nutrients = ['ndbno','name'],limit = 15, printing = True)
                print("here is your most recent 15 entrees")
                ndbno = input("Enter food's NDBNO if you know or look it up in main menu:\n> ")
                data = fetch_nutrition(ndbno)
                db.log_food(data, user_id)

            elif answer == '3':
                helper.print_with_line(texts.vizualization_3, ref=True, n=30, title="Vizualization")
                sub_choice = helper.press_any_key(s ="Enter your choice > ", inp = True)
                if sub_choice == '1':
                    indexes = db.fetch_nutrient(user_id, nutrients = ['269']) 
                    render.bar_graph(indexes, name = "Health Index over Time")
                elif sub_choice == '2':
                    sugar   = db.fetch_nutrient(user_id, nutrients = ['Index']) 
                    render.bar_graph(sugar, name = "Sugar Graph over Time")
                elif sub_choice == '3':
                    data   = db.fetch_nutrient(user_id, nutrients = ['269', 'Index'])
                    print(data)
                    render.bar_graph(data)

            elif answer == 'exit':
                helper.simple_print(texts.bye)
                break
            else:
                print("error #3")
                helper.print_with_line(texts.error.format(answer), ref = False)
                helper.pause(3)

        except Exception as err:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)
            del exc_info

            print(err)
            print("error #4")
            helper.print_with_line(texts.fatal_error, ref = False)
            helper.pause(3)    
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