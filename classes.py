import helper
import texts
import maps
import db
from pprint     import pprint
from maps       import *
from secrets    import *
from cache      import *

DEBUG = False



# here are all the classes for the FOOD HEALTH ESTIMATOR

# class food
class Food():
    def __init__(self, ndbno):
        self.data  = fetch_nutrition(ndbno)

        # this are redundant but for ease of access
        self.ndbno  = ndbno
        self.name   = self.data['name']
        self.kcal   = self.data['kcal']
        self.index  = nutri_index(self.data)

        # for conveniece aliasing the map as d
        d = maps.RNP 
        self.protein    = self.data[ d['Protein'] ]['value']
        self.carbs      = self.data[ d['Carbs'  ] ]['value']
        self.fats       = self.data[ d['Fats'   ] ]['value']
        self.fiber      = self.data[ d['Fiber'  ] ]['value']
        self.sugars     = self.data[ d['Sugars' ] ]['value']

        # saving the food to the database
        # TODO activate
        db.save_food(self.data)

    def compare_to(self,food):
        print(self)
        print(food)
    def compare_to_many(self,food_list):
        print(self)
        for food in food_list:
            print(food)

    def pie_chart(self):
        render.pie_chart(self.data)


    def __str__(self):
        index = round(self.index)

        if index >  400:
            emoji = "🤩🤩🤩🌱"
            percent = "|████████|"
        elif index >= 100:
            emoji = "🤩"
            percent = "|██████░░|"
        elif index >= 50:
            emoji = "😋"
            percent = "|█████░░░|"
        elif index >=0:
            emoji = "😐"
            percent = "|████░░░░|"
        elif index >= -50:
            emoji = "😖"
            percent = "|███░░░░░|"
        elif index >= -150:
            emoji = "🤢"
            percent = "|██░░░░░░|"
        elif index >= -250:
            emoji = "🤮"
            percent = "|█░░░░░░░|"
        else:
            emoji = "🤢🤢🤮🤢🤢"
            percent = "|░░░░░░░░|"

        helper.print_with_line(
                texts.hlth_index.format(self.name,
                    repr(index),
                    percent,
                    emoji,
                    self.protein,
                    self.carbs,
                    self.fats,
                    self.fiber,
                    self.sugars,
                    self.ndbno), 
                title="Health Index ®", 
                ref = True,
                n = 0 
                )
        answer = helper.press_any_key()
        return ''

def fetch_ndbnos_list(search_term, offset=0):
    '''
    DESCR:    returns food name&ndbno numbers, used by fetch_nutrition()
    RETURN:   list of ndbno numbers
    REQUIRES: 'search term' (required), 
              'offset'      (optional)
    MODIFIES: Nothing
    '''

    # Documentation      https://ndb.nal.usda.gov/ndb/doc/apilist/API-SEARCH.md
    # TODO try using 'Branded Food Products' for 'ds'
    # TODO IDEA: you can use 
    base_url = "https://api.nal.usda.gov/ndb/search/"
    p = {
        "format":"json",
        "q":search_term,
        "sort":"r",
        "max":11,           # return first 11 results
                            # lets paging possible

        "offset":offset,    # this will return starting at a certain number, 
                            # helpful if user wants to see more
        "ds":"Standard Reference", # or 'Branded Food Products'
        "api_key":DATAGOV_APIKEY
    }

    # making a request with caching to the USDA
    json_data = cached_reqest(base_url,params = p)

    ndbnos_list = None
    try: 
        ndbnos_list = json_data['list']['item']
        return ndbnos_list
    except: 
        return None

def fetch_nutrition(ndbno):
    '''
    DESCR:     gets nutrition data about given food item
               ndbno numbers can be recieved from fetch_ndbno_list
    RETURN:    dictionary with food item nutrition (id is key)
               data = {
                    "203": {'name':' ', 'unit': 'None', 'value':0},
                    "204": {'name':' ', 'unit': 'None', 'value':0},
                    ...
                    "name":         "",
                    "kcal":         0,
                    "ndbno":        0,
                    "health_index": 0
               }
               see maps.py for complete documentation
    REQUIRES:  ndbno of food
    MODIFIES:  nothing
    '''

    # URL: https://ndb.nal.usda.gov/ndb/doc/apilist/API-FOOD-REPORTV2.md
    # PARAMETERS:
    #   api_key   y   n/a         Must be a data.gov registered API key
    #   ndbno     y   n/a         A list of up to 50 NDB numbers
    #   type      n   b(basic)    Report type: [b]asic or [f]ull or [s]tats
    #   format1   n   JSON        Report format: xml or json

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

    # saving nutri name and ndbno into the dict
    data['name']= json_data['foods'][0]['food']['desc']['name']
    data['kcal']=float(json_data['foods'][0]['food']['nutrients'][1]['value'])
    data['ndbno']= ndbno

    # extracting the values from the JSON data
    for nutrient in json_data['foods'][0]['food']['nutrients']:
        nutrient_id    = int(nutrient['nutrient_id'])
        data[nutrient_id] = {
            "name": nutrient['name'],
            "unit": nutrient['unit'],
            "value": float(nutrient['value']),
            # TODO: this one is measures for common serving, not needed yet
            # implement it if you'd like to give people calculating options
            # "measures": nutrient['measures']
        }

    # calculating food's ®Health Index'
    idx = nutri_index(data)

    # adding it to the data
    data['health_index'] = idx

    # for debugging purposes
    if DEBUG == True:
      pprint(data)

    return(data)

def nutri_index(data):
    # DESCR:    calculates health index of a food item
    #           data can be recieved from fetch_nutrition
    # RETURN:   health index value
    # REQUIRES: nutrition data dictionary
    # MODIFIES: nothing

    # extracting necessary data for calculating HLTH_IDX
    name    = data['name'].split(" ")[0].replace(",","")

    kcal    = data[208]['value'] if data[208]['value'] else 1
    protein = data[203]['value']
    carbs   = data[205]['value']
    fiber   = data[291]['value']
    fiber   = data[291]['value']
    sugar   = data[269]['value']
    sat_f   = data[606]['value']
    trans_f = data[605]['value']
    pol_f   = data[646]['value']
    mon_f   = data[645]['value']
    vit_c   = data[401]['value']
    vit_a   = data[318]['value']
    vit_k   = data[430]['value']
    vit_d   = data[324]['value']
    sodium  = data[307]['value']

    # GOOD STUFF
    good_fats       = (pol_f*8 + mon_f*4)
    good_vitamins   = (vit_k/7 + vit_a/800 + vit_c + vit_d)
    good_protein    = protein*4

    # BAD STUFF
    bad_fats        = (sat_f*16 + trans_f*400)
    bad_sodium      = sodium
    bad_sugar       = (sugar*10 - fiber*100)


    # my proprietary formula for calculating HLTH IDX
    hlth_idx = (kcal 
        + good_fats 
        + good_vitamins
        + good_protein
        - bad_fats
        - bad_sodium 
        - bad_sugar)/kcal/2

    # test outputs
    if DEBUG == True:
        carbs_unit      = data[205]['unit']
        fiber_unit      = data[291]['unit']
        sugar_unit      = data[269]['unit']
        sat_f_unit      = data[606]['unit']
        trans_f_unit    = data[605]['unit']
        pol_f_unit      = data[646]['unit']
        mon_f_unit      = data[645]['unit']
        vit_a_unit      = data[318]['unit']
        vit_c_unit      = data[401]['unit']
        vit_d_unit      = data[324]['unit']
        vit_k_unit      = data[430]['unit']
        sodium_unit     = data[307]['unit']

        print('''
            "name":     {}
            "protein":  {}
            "kcal":     {}
            "carbs":    {}
            "fiber":    {}
            "sugar":    {}
            "sat_f":    {}
            "trans_f":  {}
            "pol_f":    {}
            "mon_f":    {}
            "vit_c":    {}
            "vit_a":    {}
            "vit_d":    {}
            "vit_k":    {}
            "sodium":   {}
            '''.format(     name,
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
        hlth_idx_good_fats: {}
        hlth_idx_good_prot: {}
        hlth_idx_good_vit:  {}
        hlth_idx_bad_fats:  {}
        hlth_idx_bad_sodiu: {}
        hlth_idx_bad_sugar: {}
            '''.format( good_fats,
                        good_protein,
                        good_vitamins,
                        bad_fats,
                        bad_sodium,
                        bad_sugar) 
            )


    # baseline - Water's IDX = 0 %
    hlth_idx_water  = 0

    # returning the health index in percent
    return hlth_idx * 100

if __name__=="__main__":

    kale     = Food(11233)
    kale.compare_to(Food(14555))
    kale.compare_to_many([Food(19375),Food(14156)])

    # Food(14555) - water
    # food_list = [Food(19375),Food(14156)] - kale and redbull



# data-base
# cache
# test cases show
# run them
# interractive