import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as ply
from maps import *

def covert_to_macro_dict(data):
	# DESCRIPTION: 	converts full dictionaty into just macros : prot, fat, carb
	# REQUIRES: 	dictionary returned from USDA API
	# RETURN: 		dictonary with just macro nutrient

	macro_dict = {
		"carbs": 	data[RNP["Carbohydrate, by difference"]]["value"],
		"proteins": data[RNP["Protein"]]["value"],
		"fats": 	data[RNP["Total lipid (fat)"]]["value"]
	}
	return macro_dict

def pie_chart(dictonary):

	labels = list(dictonary.keys())
	values = list(dictonary.values())

	trace = go.Pie(labels=labels, values=values)
	py.plot([trace], filename='basic_pie_chart')

	# fig = go.Figure(data=data, layout=layout)
	# py.plot(fig, filename='grouped-bar')

def bar_graph(data, name = "Vizualization of Health"):
	trace1 = go.Bar(
	    y=[ a[0] for a in data ],
	    x=[ a[1][1]+str(a[0]) for a in enumerate(data) ],
	    name='Health Index',
	    marker=dict(
	        color='green',
	    )
	)
	
	layout = go.Layout(
	    title=name,
	    height=600,
	    width=1080,
	    dragmode="pan",

	    bargap=0.15,
	    bargroupgap=0.1
	)
	fig = go.Figure(data=[trace1], layout=layout)
	ply.plot(fig, filename='Vizualization.html')

# def bar_graph_multiple():
# 	for data in 


d = {'203': {'name': 'Protein', 'unit': 'g', 'value': 2.92},
 '204': {'name': 'Total lipid (fat)', 'unit': 'g', 'value': 1.49},
 '205': {'name': 'Carbohydrate, by difference', 'unit': 'g', 'value': 4.42},
 '207': {'name': ' ', 'unit': 'None', 'value': 0},
 '208': {'name': 'Energy', 'unit': 'kcal', 'value': 35.0},
 '209': {'name': ' ', 'unit': 'None', 'value': 0},
 '210': {'name': ' ', 'unit': 'None', 'value': 0},
 '211': {'name': ' ', 'unit': 'None', 'value': 0},
 '212': {'name': ' ', 'unit': 'None', 'value': 0},
 '213': {'name': ' ', 'unit': 'None', 'value': 0},
 '214': {'name': ' ', 'unit': 'None', 'value': 0},
 '221': {'name': ' ', 'unit': 'None', 'value': 0},
 '255': {'name': 'Water', 'unit': 'g', 'value': 89.63},
 '257': {'name': ' ', 'unit': 'None', 'value': 0},
 '262': {'name': 'Caffeine', 'unit': 'mg', 'value': 0.0},
 '263': {'name': ' ', 'unit': 'None', 'value': 0},
 '268': {'name': ' ', 'unit': 'None', 'value': 0},
 '269': {'name': 'Sugars, total', 'unit': 'g', 'value': 0.99},
 '287': {'name': ' ', 'unit': 'None', 'value': 0},
 '291': {'name': 'Fiber, total dietary', 'unit': 'g', 'value': 4.1},
 '301': {'name': 'Calcium, Ca', 'unit': 'mg', 'value': 254.0},
 '303': {'name': 'Iron, Fe', 'unit': 'mg', 'value': 1.6},
 '304': {'name': 'Magnesium, Mg', 'unit': 'mg', 'value': 33.0},
 '305': {'name': 'Phosphorus, P', 'unit': 'mg', 'value': 55.0},
 '306': {'name': 'Potassium, K', 'unit': 'mg', 'value': 348.0},
 '307': {'name': 'Sodium, Na', 'unit': 'mg', 'value': 53.0},
 '309': {'name': 'Zinc, Zn', 'unit': 'mg', 'value': 0.39},
 '312': {'name': ' ', 'unit': 'None', 'value': 0},
 '313': {'name': ' ', 'unit': 'None', 'value': 0},
 '315': {'name': ' ', 'unit': 'None', 'value': 0},
 '317': {'name': ' ', 'unit': 'None', 'value': 0},
 '318': {'name': 'Vitamin A, IU', 'unit': 'IU', 'value': 4812.0},
 '319': {'name': ' ', 'unit': 'None', 'value': 0},
 '320': {'name': 'Vitamin A, RAE', 'unit': 'µg', 'value': 241.0},
 '321': {'name': ' ', 'unit': 'None', 'value': 0},
 '322': {'name': ' ', 'unit': 'None', 'value': 0},
 '323': {'name': 'Vitamin E (alpha-tocopherol)', 'unit': 'mg', 'value': 0.66},
 '324': {'name': 'Vitamin D', 'unit': 'IU', 'value': 0.0},
 '325': {'name': ' ', 'unit': 'None', 'value': 0},
 '326': {'name': ' ', 'unit': 'None', 'value': 0},
 '328': {'name': 'Vitamin D (D2 + D3)', 'unit': 'µg', 'value': 0.0},
 '334': {'name': ' ', 'unit': 'None', 'value': 0},
 '337': {'name': ' ', 'unit': 'None', 'value': 0},
 '338': {'name': ' ', 'unit': 'None', 'value': 0},
 '341': {'name': ' ', 'unit': 'None', 'value': 0},
 '342': {'name': ' ', 'unit': 'None', 'value': 0},
 '343': {'name': ' ', 'unit': 'None', 'value': 0},
 '401': {'name': 'Vitamin C, total ascorbic acid', 'unit': 'mg', 'value': 93.4},
 '404': {'name': 'Thiamin', 'unit': 'mg', 'value': 0.113},
 '405': {'name': 'Riboflavin', 'unit': 'mg', 'value': 0.347},
 '406': {'name': 'Niacin', 'unit': 'mg', 'value': 1.18},
 '410': {'name': ' ', 'unit': 'None', 'value': 0},
 '415': {'name': 'Vitamin B-6', 'unit': 'mg', 'value': 0.147},
 '417': {'name': ' ', 'unit': 'None', 'value': 0},
 '418': {'name': 'Vitamin B-12', 'unit': 'µg', 'value': 0.0},
 '421': {'name': ' ', 'unit': 'None', 'value': 0},
 '430': {'name': 'Vitamin K (phylloquinone)', 'unit': 'µg', 'value': 389.6},
 '431': {'name': ' ', 'unit': 'None', 'value': 0},
 '432': {'name': ' ', 'unit': 'None', 'value': 0},
 '435': {'name': 'Folate, DFE', 'unit': 'µg', 'value': 62.0},
 '454': {'name': ' ', 'unit': 'None', 'value': 0},
 '501': {'name': ' ', 'unit': 'None', 'value': 0},
 '502': {'name': ' ', 'unit': 'None', 'value': 0},
 '503': {'name': ' ', 'unit': 'None', 'value': 0},
 '504': {'name': ' ', 'unit': 'None', 'value': 0},
 '505': {'name': ' ', 'unit': 'None', 'value': 0},
 '506': {'name': ' ', 'unit': 'None', 'value': 0},
 '507': {'name': ' ', 'unit': 'None', 'value': 0},
 '508': {'name': ' ', 'unit': 'None', 'value': 0},
 '509': {'name': ' ', 'unit': 'None', 'value': 0},
 '510': {'name': ' ', 'unit': 'None', 'value': 0},
 '511': {'name': ' ', 'unit': 'None', 'value': 0},
 '512': {'name': ' ', 'unit': 'None', 'value': 0},
 '513': {'name': ' ', 'unit': 'None', 'value': 0},
 '514': {'name': ' ', 'unit': 'None', 'value': 0},
 '515': {'name': ' ', 'unit': 'None', 'value': 0},
 '516': {'name': ' ', 'unit': 'None', 'value': 0},
 '517': {'name': ' ', 'unit': 'None', 'value': 0},
 '518': {'name': ' ', 'unit': 'None', 'value': 0},
 '521': {'name': ' ', 'unit': 'None', 'value': 0},
 '573': {'name': ' ', 'unit': 'None', 'value': 0},
 '578': {'name': ' ', 'unit': 'None', 'value': 0},
 '601': {'name': 'Cholesterol', 'unit': 'mg', 'value': 0.0},
 '605': {'name': 'Fatty acids, total trans', 'unit': 'g', 'value': 0.0},
 '606': {'name': 'Fatty acids, total saturated', 'unit': 'g', 'value': 0.178},
 '607': {'name': ' ', 'unit': 'None', 'value': 0},
 '608': {'name': ' ', 'unit': 'None', 'value': 0},
 '609': {'name': ' ', 'unit': 'None', 'value': 0},
 '610': {'name': ' ', 'unit': 'None', 'value': 0},
 '611': {'name': ' ', 'unit': 'None', 'value': 0},
 '612': {'name': ' ', 'unit': 'None', 'value': 0},
 '613': {'name': ' ', 'unit': 'None', 'value': 0},
 '614': {'name': ' ', 'unit': 'None', 'value': 0},
 '615': {'name': ' ', 'unit': 'None', 'value': 0},
 '617': {'name': ' ', 'unit': 'None', 'value': 0},
 '618': {'name': ' ', 'unit': 'None', 'value': 0},
 '619': {'name': ' ', 'unit': 'None', 'value': 0},
 '620': {'name': ' ', 'unit': 'None', 'value': 0},
 '621': {'name': ' ', 'unit': 'None', 'value': 0},
 '624': {'name': ' ', 'unit': 'None', 'value': 0},
 '625': {'name': ' ', 'unit': 'None', 'value': 0},
 '626': {'name': ' ', 'unit': 'None', 'value': 0},
 '627': {'name': ' ', 'unit': 'None', 'value': 0},
 '628': {'name': ' ', 'unit': 'None', 'value': 0},
 '629': {'name': ' ', 'unit': 'None', 'value': 0},
 '630': {'name': ' ', 'unit': 'None', 'value': 0},
 '631': {'name': ' ', 'unit': 'None', 'value': 0},
 '636': {'name': ' ', 'unit': 'None', 'value': 0},
 '638': {'name': ' ', 'unit': 'None', 'value': 0},
 '639': {'name': ' ', 'unit': 'None', 'value': 0},
 '641': {'name': ' ', 'unit': 'None', 'value': 0},
 '645': {'name': 'Fatty acids, total monounsaturated',
         'unit': 'g',
         'value': 0.104},
 '646': {'name': 'Fatty acids, total polyunsaturated',
         'unit': 'g',
         'value': 0.673},
 '652': {'name': ' ', 'unit': 'None', 'value': 0},
 '653': {'name': ' ', 'unit': 'None', 'value': 0},
 '654': {'name': ' ', 'unit': 'None', 'value': 0},
 '662': {'name': ' ', 'unit': 'None', 'value': 0},
 '663': {'name': ' ', 'unit': 'None', 'value': 0},
 '664': {'name': ' ', 'unit': 'None', 'value': 0},
 '665': {'name': ' ', 'unit': 'None', 'value': 0},
 '666': {'name': ' ', 'unit': 'None', 'value': 0},
 '669': {'name': ' ', 'unit': 'None', 'value': 0},
 '670': {'name': ' ', 'unit': 'None', 'value': 0},
 '671': {'name': ' ', 'unit': 'None', 'value': 0},
 '672': {'name': ' ', 'unit': 'None', 'value': 0},
 '673': {'name': ' ', 'unit': 'None', 'value': 0},
 '674': {'name': ' ', 'unit': 'None', 'value': 0},
 '675': {'name': ' ', 'unit': 'None', 'value': 0},
 '676': {'name': ' ', 'unit': 'None', 'value': 0},
 '685': {'name': ' ', 'unit': 'None', 'value': 0},
 '687': {'name': ' ', 'unit': 'None', 'value': 0},
 '689': {'name': ' ', 'unit': 'None', 'value': 0},
 '693': {'name': ' ', 'unit': 'None', 'value': 0},
 '696': {'name': ' ', 'unit': 'None', 'value': 0},
 '697': {'name': ' ', 'unit': 'None', 'value': 0},
 '710': {'name': ' ', 'unit': 'None', 'value': 0},
 '711': {'name': ' ', 'unit': 'None', 'value': 0},
 '712': {'name': ' ', 'unit': 'None', 'value': 0},
 '713': {'name': ' ', 'unit': 'None', 'value': 0},
 '714': {'name': ' ', 'unit': 'None', 'value': 0},
 '715': {'name': ' ', 'unit': 'None', 'value': 0},
 '716': {'name': ' ', 'unit': 'None', 'value': 0},
 '731': {'name': ' ', 'unit': 'None', 'value': 0},
 '734': {'name': ' ', 'unit': 'None', 'value': 0},
 '735': {'name': ' ', 'unit': 'None', 'value': 0},
 '736': {'name': ' ', 'unit': 'None', 'value': 0},
 '737': {'name': ' ', 'unit': 'None', 'value': 0},
 '738': {'name': ' ', 'unit': 'None', 'value': 0},
 '740': {'name': ' ', 'unit': 'None', 'value': 0},
 '741': {'name': ' ', 'unit': 'None', 'value': 0},
 '742': {'name': ' ', 'unit': 'None', 'value': 0},
 '743': {'name': ' ', 'unit': 'None', 'value': 0},
 '745': {'name': ' ', 'unit': 'None', 'value': 0},
 '749': {'name': ' ', 'unit': 'None', 'value': 0},
 '750': {'name': ' ', 'unit': 'None', 'value': 0},
 '751': {'name': ' ', 'unit': 'None', 'value': 0},
 '752': {'name': ' ', 'unit': 'None', 'value': 0},
 '753': {'name': ' ', 'unit': 'None', 'value': 0},
 '758': {'name': ' ', 'unit': 'None', 'value': 0},
 '759': {'name': ' ', 'unit': 'None', 'value': 0},
 '762': {'name': ' ', 'unit': 'None', 'value': 0},
 '770': {'name': ' ', 'unit': 'None', 'value': 0},
 '773': {'name': ' ', 'unit': 'None', 'value': 0},
 '785': {'name': ' ', 'unit': 'None', 'value': 0},
 '786': {'name': ' ', 'unit': 'None', 'value': 0},
 '788': {'name': ' ', 'unit': 'None', 'value': 0},
 '789': {'name': ' ', 'unit': 'None', 'value': 0},
 '794': {'name': ' ', 'unit': 'None', 'value': 0},
 '851': {'name': ' ', 'unit': 'None', 'value': 0},
 '853': {'name': ' ', 'unit': 'None', 'value': 0},
 '855': {'name': ' ', 'unit': 'None', 'value': 0},
 '856': {'name': ' ', 'unit': 'None', 'value': 0},
 '857': {'name': ' ', 'unit': 'None', 'value': 0},
 '858': {'name': ' ', 'unit': 'None', 'value': 0},
 'kcal': 35.0,
 'name': 'Kale, raw',
 'ndbno': '11233'}

# macro = covert_to_macro_dict(d)
# render_pie_chart(macro)
