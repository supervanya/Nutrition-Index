'''
Vanya, sounds like a really interesting project and I like that its something you personally care about. For the course project, this is substantial work. Just a reminder that our project structure requires you to use two tables and one relation at a minimum. 

One piece of advice: Complete this project with a future employer in mind, make sure you document well. And, commit and push often, building the project in steps/ iterations. Good luck! 

This makes me think of personal informatics applications and am thinking you could turn this into one. If you're looking to add more to your idea, I'd suggest adding a table that tracks what you eat each day and you could visualize how much calories/nutrients you get on average. I know that you probably won't have working code anytime soon to build this table. You could make notes on paper of what you eat each day and when you have this ready, feed that data in. Or you might just create a text file that you use as input when your code is ready. Its just a random thought I had reading your idea. You are in no way obligated to consider it!
'''

from pprint import pprint
from cache import *
from secrets import *
from maps import *
import time
import helper
import texts

# trurn this off to remove debugginf print statements
DEBUG = True

def fetch_ndbnos_list(search_term = None, n = 0):
	# DESCRIPTION: returns ndbno number, needed by fetch_nutrition()
	# RETURN: 	food ndbno
	# REQUIRES: search term to avoid prompt
	# MODIFIES: print to terminal


	# Here is the api request URL example:
	# 1. Explore in Browser https://ndb.nal.usda.gov/ndb/foods/show/9?fgcd=&manu=&lfacet=&format=&count=&max=50&offset=&sort=default&order=asc&qlookup=01009&ds=&qt=&qp=&qa=&qn=&q=&ing=
	# 2. APIurl				https://api.nal.usda.gov/ndb/search/?format=json&q=butter&sort=n&max=25&offset=0&api_key=DEMO_KEY
	# 3. Documentation		https://ndb.nal.usda.gov/ndb/doc/apilist/API-SEARCH.md


	food_ids_list = False
	while not food_ids_list:
		if search_term == None:
			search_term = helper.press_any_key(s ="\nEnter food name? (or 'back' for main menu)\n> ", inp = True)
			# search_term = input("\nEnter food name? (or 'exit')\n> ") TODO remove
			if search_term.lower() == "back":
				return None

		# making a request with caching to the USDA for a list of products
		base_url = "https://api.nal.usda.gov/ndb/search/"
		p = {
			"format":"json",
			"q":search_term,
			"sort":"r",
			"max":50,
			"ds":"Standard Reference",
			"api_key":DATAGOV_APIKEY
		}
		json_data = cached_reqest(base_url,params = p)
		try: 
			food_ids_list = json_data['list']['item']
			break
		except:	
			helper.print_with_line(texts.not_found, ref = False)
			return None


	# loop while user hasn't made the right choice  (exit, next, correct number)
		# print options
		# ask for asnwer
		# check what that answer does:
			# if exit:
				# exit()
			# elif next set:
				# increment n + continue
			# elif correct number:
				# chose the correct one
			# else:
				# return o

	more = False
	if len(food_ids_list) > 10:
		print_more = True
		n = 10
	else:
		print_more = False
		n = len(food_ids_list)

	# this while loop is complicated but it just makes sure
	# that user enters the correct integer from the list
	while True:
		try:
			for i,food in enumerate(food_ids_list[:n],1):
				# print options
				print("[{}] {}".format(i,helper.wrap(food['name'])))
				time.sleep(0.05)
			# add an option to show more
			if print_more:
				print("[...] For more")

			food_number = helper.press_any_key(s ="\nWhich one? (enter # or 'exit')\n> ", inp = True)
			# food_number = input("\nWhich one? (enter # or 'exit')\n> ") TODO remove
			
			if food_number.lower() == 'exit':
				return 0
			elif food_number == '...':
				more = True
				break
			else:
				chosen_food = food_ids_list[int(food_number) - 1]
				break
		except:
			helper.print_with_line(texts.invalid.format(food_number), ref = None)
	if more:
		while True:
			try:
				for i,food in enumerate(food_ids_list,1):
					print("[{}] {}".format(i,helper.wrap(food['name'])))
					time.sleep(0.05)

				food_number = input("\nWhich one? (enter # or exit)\n> ")

				if food_number.lower() == 'exit':
					return 0
				else:
					chosen_food = food_ids_list[int(food_number) - 1]
					break
			except:
				helper.print_with_line(texts.invalid.format(food_number), ref = None)


	# if user enters exit - return 'exit' 
	if food_number.lower() == 'exit':
		return 0

	# selecting the correct one and extracting name and number
	chosen_food_name 	= chosen_food['name']
	chosen_food_ndbno 	= chosen_food['ndbno']
	

	# returning just the ndbno
	return chosen_food_ndbno,food_ids_list #,chosen_food_name

def fetch_nutrition(ndbno):
	# DESCRIPTION:  gets nutrition data about given food item
	# 				ndbno number can be recieved from fetch_ndbno
	# RETURN: 	dictionary with food item nutrition (id is key)
	# REQUIRES: ndbno food item
	# MODIFIES: nothing

	# URL: https://api.nal.usda.gov/ndb/reports/V2?ndbno=01009&ndbno=01009&ndbno=45202763&ndbno=35193&type=b&format=json&api_key=DEMO_KEY
	# PARAMETERS:
	# api_key	y			n/a	Must be a data.gov registered API key
	# ndbno	y	n/a			A list of up to 50 NDB numbers
	# type	n	b 			Report type: [b]asic or [f]ull or [s]tats
	# format1	n 			Report format: xml or json

	# TODO, switch 'type' to f if needed full report
	base_url = "https://api.nal.usda.gov/ndb/V2/reports"
	p = {
		"format":"json",
		"ndbno":ndbno,
		"type":"b",
		"api_key":DATAGOV_APIKEY
	}
	json_data = cached_reqest(base_url,params = p)

	# blank dictonary to hold values of interest
	data = blank_nutri_map
	print(json_data)


	# saving nutri name and ndbno into the dict
	data['name'] = json_data['foods'][0]['food']['desc']['name']
	data['kcal'] = float(json_data['foods'][0]['food']['nutrients'][1]['value'])
	data['ndbno'] = ndbno

	# extracting the values of interest from the JSON data
	for nutrient in json_data['foods'][0]['food']['nutrients']:
		nutri_id = int(nutrient['nutrient_id'])
		data[nutri_id] = {
			"name": nutrient['name'],
			"unit": nutrient['unit'],
			"value": float(nutrient['value']),
			# TODO: this one is measures for common serving, not needed yet
			# "measures": nutrient['measures']
		}

	# calculating food's ®Health Index'
	idx = nutri_index(data)
	# adding it to the data
	data['health_index'] = idx

	# for debugging purposes
	# if DEBUG == True:
	# 	pprint(data)

	return(data)

def nutri_index(data):
	# DESCR:	calculates health index of a food item
	# 			data can be recieved from fetch_nutrition
	# RETURN: 	health index value
	# REQUIRES: nutrition data dictionary
	# MODIFIES: nothing

	# extracting necessary data for calculating HLTH_IDX
	name 	= data['name'].split(" ")[0].replace(",","")
	# kcal 	= data['kcal']

	kcal	= data[208]['value'] if data[208]['value'] else 0.101
	protein	= data[203]['value']
	carbs	= data[205]['value']
	fiber	= data[291]['value']
	fiber	= data[291]['value']
	sugar	= data[269]['value']
	sat_f	= data[606]['value']
	trans_f = data[605]['value']
	pol_f 	= data[646]['value']
	mon_f 	= data[645]['value']
	vit_c	= data[401]['value']
	vit_a	= data[318]['value']
	vit_k	= data[430]['value']
	vit_d	= data[324]['value']
	sodium	= data[307]['value']

	# GOOD STUFF
	good_fats		= (pol_f*8 + mon_f*4)
	good_vitamins	= vit_k/7 + vit_a/800 + vit_c + vit_d
	good_protein	= protein*4

	# BAD STUFF
	bad_fats		= (sat_f*16 + trans_f*400)
	bad_sodium 		= (sodium-2)/2
	bad_sugar 		= (sugar*10 - fiber*100)


	# my proprietary formula for calculating HLTH IDX
	hlth_idx = (kcal 
		+ good_fats 
		+ good_vitamins
		+ good_protein
		- bad_fats
		- bad_sodium 
		- bad_sugar)/kcal/2

	# if food had 
	if kcal == 0.101:
		hlth_idx = hlth_idx - 0.5

	# baseline - Water's IDX = 0 %
	hlth_idx_water	= 0

	# test outputs
	if DEBUG == True:
		carbs_unit		= data[205]['unit']
		fiber_unit		= data[291]['unit']
		sugar_unit		= data[269]['unit']
		sat_f_unit		= data[606]['unit']
		trans_f_unit	= data[605]['unit']
		pol_f_unit		= data[646]['unit']
		mon_f_unit		= data[645]['unit']
		vit_a_unit		= data[318]['unit']
		vit_c_unit		= data[401]['unit']
		vit_d_unit		= data[324]['unit']
		vit_k_unit		= data[430]['unit']
		sodium_unit		= data[307]['unit']

		print('''
			"name":		{}
			"protein":	{}
			"kcal":		{}
			"carbs":	{}
			"fiber":	{}
			"sugar":	{}
			"sat_f":	{}
			"trans_f":	{}
			"pol_f":	{}
			"mon_f":	{}
			"vit_c":	{}
			"vit_a":	{}
			"vit_d":	{}
			"vit_k":	{}
			"sodium":	{}
			'''.format(		name,
							protein,
							kcal,
							str(carbs) + carbs_unit,
							str(fiber) + fiber_unit ,
							str(sugar) + sugar_unit ,
							str(sat_f) + sat_f_unit ,
							str(trans_f) + trans_f_unit ,
							str(pol_f) + pol_f_unit ,
							str(mon_f) + mon_f_unit ,
							str(vit_c) + vit_c_unit ,
							str(vit_a) + vit_a_unit ,
							str(vit_d) + vit_d_unit ,
							str(vit_k) + vit_k_unit ,
							str(sodium) + sodium_unit) 
			)

		print('''
		hlth_idx_good_fats:	{}
		hlth_idx_good_prot:	{}
		hlth_idx_good_vit:	{}
		hlth_idx_bad_fats:	{}
		hlth_idx_bad_sodiu:	{}
		hlth_idx_bad_sugar:	{}
			'''.format(	good_fats,
						good_protein,
						good_vitamins,
						bad_fats,
						bad_sodium,
						bad_sugar) 
			)

	# returning the health index in percent
	return hlth_idx * 100

