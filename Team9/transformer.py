from bs4 import BeautifulSoup
import requests
import sys
import nltk
import random

#given a recipe dictionary of lists of dictionaries / lists -> transform to new object of same format

# #Sample Recipe Representation 

test_rec = { "name": "Testing Recipe",
  "ingredients": [  
  		{
  		"name": "corn bread",
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
		}],
	"primary cooking method": "fry",
	"cooking methods": ["fry","stir", "spread"],
	"cooking tools": ["pan","pot","spatula"],
	"steps": [
		{
			"text": "place corn bread and beef in pot and spread along sides with spatula",
			#Optional
			"ingredients": ["corn bread", "beef"],
			"tools": ["pot","spatula"],
			"methods": ["stir","spread"],
			"times": 5.0
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

#replaces all vegetables with meat
def remove_meat(recipe):
	found_meat = []
	replacement = {}
	for single_ingredient in recipe['ingredients']:
		if single_ingredient["name"] in meats:
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
			veg_replacement = random.choice(meats) # TODO: we can be smarter than random
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
		if single_ingredient["name"] in meats:
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
	new_rec['ingredients'].append({
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

	return new_rec

#nicely displays in terminal output
def displayRecipe(recipe):
	print '____________________________________________________________________________'
	print "Name: " + recipe['name']
	print "Ingredients: "
	for single_ingredient in recipe['ingredients']:
		print single_ingredient['name']
		print str(single_ingredient['quantity']) + ' ' + (single_ingredient['measurement'])
		print single_ingredient['descriptor']
		print single_ingredient['preparation'] + ' prep-description: ' + single_ingredient['prep-description']
	print "Primary Cooking Method: " + recipe['primary cooking method']
	print "Cooking Methods: "
	for single_method in recipe['cooking methods']:
		print single_method
	print "Cooking Tools: "
	for single_tool in recipe['cooking tools']:
		print single_tool
	print "Steps: "
	for single_step in recipe['steps']:
		print single_step['text']
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


load_lists()
displayRecipe(to_Mediterranean(test_rec))



