	# hlth_idx_hoot = 	(kcal + fiber*4 + pol_f*9 + mon_f*9 + vitamins - sugar*4 - trans_f*9 - sat_f*9 - sodium)/(kcal+0.001)*100
	# hlth_idx_vanya = 	(kcal + fiber*40 + pol_f*40 + mon_f*8 + vitamins - sugar*10 - trans_f*20 - sat_f*8 - sodium)/(kcal+0.001)*100
	# hlth_idx2 = 	kcal - carb_evil - sugar_evil - sugar_evil2 - fats_evil
	# hlth_idx3 = 	(kcal - (sugar + trans_f) + fiber) / (kcal+0.001) * 100
	# print("Vanya's Health Index of {}: {} % 💪".format(name, round(hlth_idx)) )

	# print("\nvitals\n", "kcal: ",kcal, "\ncarbs: ",carbs,"\nfiber: ",fiber,"\nsugar: ",sugar,"\nsat_f: ",sat_f,"\ntrans_f: ",trans_f)
	# print(data['name'])
	# print("\nvalues\n","carb_evil:" ,carb_evil,"\nsugar_evil:" ,sugar_evil,"\nsugar_evil2:" ,sugar_evil2,"\nfats_evil:" ,fats_evil)
	# print("index1 {} %  index2  {}%  index3  {}% for {} 💪".format(round(hlth_idx1), round(hlth_idx2), round(hlth_idx3), name ) )
	# helper.print_with_line("{} is {} % 💪 healthy | Vanya's HEALTH.Index".format(name, round(hlth_idx1)))
	# print("{} is {} % 💪 hootIDX".format(name, round(hlth_idx_hoot))+"\n{} is {} % 💪 vanyaIDX".format(name, round(hlth_idx_vanya)))


	# testing if records exist
    if not nbdno_exists: # if nbdno doesn't exist
        print('5): {} exists'.format(id_exists))
    else:
        print(id_exists)
        print('5): {} does not exist'.format(ndbno))



# for i in ["11124","11333","09003","08013","19359","14434","14433","14433","14145","11258","19150"]:
# 	data = fetch_nutrition(i)
# 	nutri_index(data)





# with open('ndbnos.txt', "w") as f:
# 	while True:
# 		s = str(fetch_ndbno())+"\n"
# 		f.write(s)
# f.close


'''
apple 131 %
kale 653 %
beef 80 %

11124', 'Carrots
11333', 'Peppers
09003', "Apples
09129', 'Grapes
08013', 'Cereals
19359', 'Candies
14434', 'Beverages
14433', 'Beverages
14433', 'Beverages
14145', 'Beverages
11258', 'Mountain
19150', "Candies
'''
