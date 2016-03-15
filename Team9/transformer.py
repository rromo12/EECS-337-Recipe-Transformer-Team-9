from bs4 import BeautifulSoup
import requests
import sys
import nltk
import random
from carbsubs import *
from fatsubs import *
from parser import *

#given a recipe dictionary of lists of dictionaries / lists -> transform to new object of same format

# #Sample Recipe Representation 
# Sources Used:
# http://naturalhealthtechniques.com/
# https://www.nhlbi.nih.gov/health/educational/lose_wt/eat/shop_lcal_fat.htm

test_rec = { "name": "Testing Recipe",
  "ingredients": [  
  		{
  		"name": "wheat bread",
		"quantity": 0.25,
		"measurement": "pounds",
		"descriptor": "descriptor",
		"preparation": "chopped",
		"prep-description": "finely"
		},
		{
		"name": "beef",
		"quantity": 2.50,
		"measurement": "pounds",
		"descriptor": "descriptor",
		"preparation": "minced",
		"prep-description": "coarsely"
		},
		{
  		"name": "chicken",
		"quantity": 0.25,
		"measurement": "pounds",
		"descriptor": "descriptor",
		"preparation": "chopped",
		"prep-description": "finely"
		}],
	"primary cooking method": "fry",
	"cooking methods": ["fry","stir", "spread"],
	"cooking tools": ["pan","pot","spatula"],
	"steps": [
		{
			"text": "place wheat bread, chicken and beef in pot and spread along sides with spatula",
			#Optional
			"ingredients": ["wheat bread", "beef", 'chicken'],
			"tools": ["pot","spatula"],
			"methods": ["stir","spread"],
			"times": 5.0
		},
		{
			"text": "add muenster cheese to mixture and stir in",
			#Optional
			"ingredients": ["muenster cheese"],
			"tools": ["pot"],
			"methods": ["stir"],
			"times": 2.0
		},
		{
			"text": "fry mixture in pot for 10 hours",
			#Optional
			"ingredients": ["corn bread", "beef"],
			"tools": ["pot"],
			"methods": ["fry"],
			"times": 600.0
		}]
}

meats = []
poultrys = []
vegetables = []
fishes = []
fruits = []
breads = []
cheeses = []
allmeat = []

#load txt files into python list objects
def load_lists():
	meat_file = open("meats.txt", "r")
	meat_lines = meat_file.readlines()
	for meat in meat_lines:
		curr = meat.rstrip('\n')
		meats.append(str(curr.lower()))

	poultry_file = open("poultry.txt", "r")
	poultry_lines = poultry_file.readlines()
	for poultry in poultry_lines:
		curr = poultry.rstrip('\n')
		poultrys.append(str(curr.lower()))

	vegetable_file = open("vegetables.txt", "r")
	veg_lines = vegetable_file.readlines()
	for veg in veg_lines:
		curr = veg.rstrip('\n')
		vegetables.append(str(curr.lower()))

	fish_list = open("fish.txt", 'r').readlines()
	for pheesh in fish_list:
		curr = pheesh.rstrip('\n')
		fishes.append(str(curr.lower()))

	fruit_list = open("fruits.txt", 'r').readlines()
	for fruit in fruit_list:
		curr = fruit.rstrip('\n')
		fruits.append(str(curr.lower()))

	bread_list = open("breads.txt", 'r').readlines()
	for bread in bread_list:
		curr = bread.rstrip('\n')
		breads.append(str(curr.lower()))

	dairy_list = open("cheeses.txt", 'r').readlines()
	for dairy in dairy_list:
		curr = dairy.rstrip('\n')
		cheeses.append(str(curr.lower()))

	for meat in meats:
		allmeat.append(meat)
	for pol in poultrys:
		allmeat.append(pol)

#replaces all meat with vegetables
def remove_meat(recipe):
	found_meat = []
	replacement = {}
	for single_ingredient in recipe['ingredients']:
		if single_ingredient["name"] in allmeat:
			meat_replacement = random.choice(vegetables) # TODO: we can be smarter than random
			found_meat.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = meat_replacement
			single_ingredient["name"] = meat_replacement
	for meat in found_meat:
		for step in recipe["steps"]:
			if meat in step["text"]:
				step["text"] = step["text"].replace(meat, replacement[meat])

	return recipe

#replaces all meats with vegetables
def add_meat(recipe):
	found_veg = []
	replacement = {}
	for single_ingredient in recipe['ingredients']:
		if single_ingredient["name"] in vegetables:
			veg_replacement = random.choice(allmeat) # TODO: we can be smarter than random
			found_veg.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = veg_replacement
			single_ingredient["name"] = veg_replacement
	for veg in found_veg:
		for step in recipe["steps"]:
			if veg in step["text"]:
				step["text"] = step["text"].replace(veg, replacement[veg])
	return recipe


#replaces all fish with meat
def remove_fish(recipe):
	found_fish = []
	replacement = {}
	for single_ingredient in recipe['ingredients']:
		if single_ingredient["name"] in fishes:
			meat_replacement = random.choice(meats) # TODO: we can be smarter than random
			found_fish.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = meat_replacement
			single_ingredient["name"] = meat_replacement
	for fish in found_fish:
		for step in recipe["steps"]:
			if fish in step["text"]:
				step["text"] = step["text"].replace(fish, replacement[fish])
	return recipe

#replaces all meats with fish
def add_fish(recipe):
	found_meat = []
	replacement = {}
	for single_ingredient in recipe['ingredients']:
		if single_ingredient["name"] in allmeat:
			fish_replacement = random.choice(fishes) # TODO: we can be smarter than random
			found_meat.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = fish_replacement
			single_ingredient["name"] = fish_replacement
	for meat in found_meat:
		for step in recipe["steps"]:
			if meat in step["text"]:
				step["text"] = step["text"].replace(meat, replacement[meat])
	return recipe

#Convert to mediterranean cuisine
def to_Mediterranean(recipe):
	new_rec = add_fish(recipe)
	found_veg = []
	found_bread = [] 
	replacement = {}
	replacement_bread = {}
	pitacount = 0
	bread_replacement = 'pita bread' 
	#add ingredients we know for sure we will ba dding
	new_rec['ingredients'].append({ #add in logic for if recipe already had feta, hummus, olive oil
  		"name": "olive oil",
		"quantity": 0.25,
		"measurement": "teaspoons",
		"descriptor": "extra virgin",
		"preparation": "none",
		"prep-description": "none"
		})
	new_rec['ingredients'].append({
  		"name": "feta cheese",
		"quantity": 0.25,
		"measurement": "pounds",
		"descriptor": "none",
		"preparation": "crumbled",
		"prep-description": "none"
		})
	new_rec['ingredients'].append({
  		"name": "hummus",
		"quantity": 0.25,
		"measurement": "pounds",
		"descriptor": "none",
		"preparation": "none",
		"prep-description": "none"
		})
	for single_ingredient in new_rec['ingredients']:
		if single_ingredient["name"] in vegetables:
			veg_replacement = random.choice(fruits) # TODO: we can be smarter than random
			found_veg.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = veg_replacement
			single_ingredient["name"] = veg_replacement
		if single_ingredient["name"] in breads:
			if pitacount <= 3:
				found_bread.append(single_ingredient["name"])
				replacement_bread[single_ingredient["name"]] = bread_replacement
				single_ingredient["name"] = bread_replacement
				pitacount += 1
	for veg in found_veg:
		for step in new_rec["steps"]:
			if veg in step["text"]:
				step["text"] = step["text"].replace(veg, replacement[veg])
	for bread in found_bread:
		for step in new_rec["steps"]:
			if bread in step["text"]:
				step["text"] = step["text"].replace(bread, replacement_bread[bread])
	new_rec['steps'].append({
			"text": "drizzle olive oil and crumbled feta cheese over finished product, serve with hummus",
			#Optional
			"ingredients": ['olive oil', 'feta cheese', 'hummus'],
			"tools": [],
			"methods": ["drizzle"],
			"times": 1.0
		})
	if pitacount == 0:
		new_rec['steps'].append({
			"text": "Cut pita bread into little triangles and serve on the side in a plate",
			#Optional
			"ingredients": ['pita bread'],
			"tools": [],
			"methods": ["cut"],
			"times": 1.0
		})
		new_rec['ingredients'].append({
  		"name": "pita bread",
		"quantity": 0.25,
		"measurement": "pounds",
		"descriptor": "none",
		"preparation": "none",
		"prep-description": "none"
		})

	return new_rec

#transforms recipe to american cuisine
#version 1.0 -> add meat, replace all cheeses with american cheese
def to_American(recipe):
	new_rec = add_meat(recipe)
	found_cheese = []
	replacement = {}
	cheese_replacement = 'american cheese'
	for single_ingredient in new_rec['ingredients']:
		if single_ingredient["name"] in cheeses:
			found_cheese.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = cheese_replacement
			single_ingredient["name"] = cheese_replacement
	for cheese in found_cheese:
		for step in new_rec["steps"]:
			if cheese in step["text"]:
				step["text"] = step["text"].replace(cheese, replacement[cheese])

	return new_rec

def to_lowCarb(recipe):
	found_highcarbs = []
	for single_ingredient in recipe['ingredients']:
		if single_ingredient['name'] in carb_subs:
			found_highcarbs.append(single_ingredient['name'])
			single_ingredient['name'] = carb_subs[single_ingredient['name']]
	for badcarbs in found_highcarbs:
		for step in recipe["steps"]:
			if badcarbs in step["text"]:
				step["text"] = step["text"].replace(badcarbs, carb_subs[badcarbs])

	return recipe

def to_highCarb(recipe):
	inv_subs = {v: k for k, v in carb_subs.items()}
	found_lowcarbs = []
	for single_ingredient in recipe['ingredients']:
		if single_ingredient['name'] in inv_subs:
			found_lowcarbs.append(single_ingredient['name'])
			single_ingredient['name'] = inv_subs[single_ingredient['name']]
	for goodcarb in found_lowcarbs:
		for step in recipe["steps"]:
			if goodcarb in step["text"]:
				step["text"] = step["text"].replace(goodcarb, inv_subs[goodcarb])

	return recipe

def to_lowFat(recipe):
	found_highfats = []
	for single_ingredient in recipe['ingredients']:
		if single_ingredient['name'] in fat_subs:
			found_highfats.append(single_ingredient['name'])
			single_ingredient['name'] = fat_subs[single_ingredient['name']]
	for badfats in found_highfats:
		for step in recipe["steps"]:
			if badfats in step["text"]:
				step["text"] = step["text"].replace(badfats, fat_subs[badfats])

	return recipe


#nicely displays in terminal output
def displayRecipe(recipe):
	print '____________________________________________________________________________'
	print "Name: " + recipe['name']
	print "Ingredients: "
	for single_ingredient in recipe['ingredients']:
		print ' ' + single_ingredient['name']
		print '  ' + str(single_ingredient['quantity']) + ' ' + (single_ingredient['measurement'])
		print '  ' + str(single_ingredient['descriptor'])
		print '  ' + str(single_ingredient['preparation']) #+ ' prep-description: ' + str(single_ingredient['prep-description'])
	print "Primary Cooking Method: " + recipe['primary cooking method']
	print "Cooking Methods: "
	for single_method in recipe['cooking methods']:
		print ' ' + single_method
	print "Cooking Tools: "
	for single_tool in recipe['cooking tools']:
		print ' ' + single_tool
	print "Steps: "
	for single_step in recipe['steps']:
		print ' ' + single_step['text']
		#print 'Ingredients: '
		#for single_ingredient in single_step['ingredients']:
		#	print single_ingredient
		#print 'Tools: '
		#for single_tool in single_step['tools']:
		#	print single_tool
		#print 'Methods: '
		#for single_method in single_step['methods']:
		#	print single_method
		#print 'Time: ' + str(single_step['times'])
		#print ''

def displayRecipe_preparse(recipe):
	print '____________________________________________________________________________'
	print "Name: " + recipe['name']
	print "Ingredients: "
	for single_ingredient in recipe['ingredients']:
		print ' ' + single_ingredient['name']
		print '  ' + str(single_ingredient['quantity']) + ' ' + (single_ingredient['measurement'])
		print '  ' + str(single_ingredient['descriptor'])
		print '  ' + str(single_ingredient['preparation']) #+ ' prep-description: ' + str(single_ingredient['prep-description'])
	print "Primary Cooking Method: " + recipe['primary cooking method']
	print "Cooking Methods: "
	for single_method in recipe['cooking methods']:
		print ' ' + single_method
	print "Cooking Tools: "
	for single_tool in recipe['cooking tools']:
		print ' ' + single_tool
	print "Steps: "
	for single_step in recipe['steps']:
		print ' ' + single_step['text']
		print 'Ingredients: '
		for single_ingredient in single_step['ingredients']:
			print single_ingredient
		print 'Tools: '
		for single_tool in single_step['tools']:
			print single_tool
		print 'Methods: '
		for single_method in single_step['methods']:
			print single_method
		print 'Time: ' + str(single_step['times'])
		print ''

def main():
	print "Main Function initiated"
	print "Loading Lists..."
	load_lists()
	print "Lists Loaded..."
	print "Fetching Recipes..."
	url_01 = "http://allrecipes.com/recipe/213742/meatball-nirvana/"
	url_02 = "http://allrecipes.com/recipe/easy-meatloaf/"
	url_03 = "http://allrecipes.com/recipe/8714/baked-lemon-chicken-with-mushroom-sauce/"
	url_04 = "http://allrecipes.com/recipe/80827/easy-garlic-broiled-chicken/"

	#rec_01 = parser(url_01)
	#print "Sample Recipe 1 Parsed!"
	#rec_02 = parser(url_02)
	#print "Sample Recipe 2 Parsed!"
	#rec_03 = parser(url_03)
	#print "Sample Recipe 3 Parsed!"
	#rec_04 = parser(url_04)
	#print "Sample Recipe 4 Parsed!"

	while True:
		print "Press 1 to enter URL, 2 to select from loaded recipes: "
		usr_input = input()
		if usr_input == 1:
			user_url = str(raw_input("enter recipe url: "))
		elif usr_input == 2:
			print "Press 1 to test meatball-nirvana"
			print "Press 2 to test easy-meatloaf"
			print "Press 3 to test baked-lemon-chicken-with-mushroom-sauce"
			print "Press 4 to test easy-garlic-broiled-chicken"
			usr_input = input()
			if usr_input == 1:
				user_url = url_01
			elif usr_input == 2:
				user_url = url_02
			elif usr_input == 3:
				user_url = url_03
			elif usr_input == 4:
				user_url = url_04
			else:
				print "Please enter 1, 2, 3, or 4"
		else:
			print "Please enter 1 or 2..."

		orig_rec = parser(user_url)
		displayRecipe_preparse(orig_rec)

	return


if __name__ == '__main__':
    main() 
#displayRecipe(to_lowCarb(test_rec))



