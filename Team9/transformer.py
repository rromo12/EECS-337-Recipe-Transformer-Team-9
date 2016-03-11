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
  		"name": "bear",
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
			"text": "place bear and beef in pot and spread along sides with spatula",
			#Optional
			"ingredients": ["bear", "beef"],
			"tools": ["pot","spatula"],
			"methods": ["stir","spread"],
			"times": 5.0
		},
		{
			"text": "fry mixture in pot for 10 hours",
			#Optional
			"ingredients": ["bear", "beef"],
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

	fish_list = open("fish.txt").readlines()
	for pheesh in fish_list:
		curr = pheesh.rstrip('\n')
		fishes.append(str(curr.lower()))

	fruit_list = open("fruits.txt").readlines()
	for fruit in fruit_list:
		curr = pheesh.rstrip('\n')
		fruits.append(str(curr.lower()))


#print test_rec

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

def to_Mediterranean(recipe):
	new_rec = add_fish(recipe)
	found_veg = []
	replacement = {}
	for single_ingredient in new_rec['ingredients']:
		if single_ingredient["name"] in vegetables:
			veg_replacement = random.choice(fruits) # TODO: we can be smarter than random
			found_veg.append(single_ingredient["name"])
			replacement[single_ingredient["name"]] = veg_replacement
			single_ingredient["name"] = veg_replacement
	for veg in found_veg:
		for step in new_rec["steps"]:
			if veg in step["text"]:
				step["text"] = step["text"].replace(veg, replacement[veg])
	new_rec['steps'].append({
			"text": "drizzle olive oil over finished product, serve with feta cheese on the side",
			#Optional
			"ingredients": ['olive oil', 'feta cheese'],
			"tools": [],
			"methods": ["drizzle"],
			"times": 1.0
		})

	return new_rec

#nicely displays in terminal output
def displayRecipe(recipe):
	print "Name: " + recipe['name']
	print "Ingredients: "
	for single_ingredient in recipe['ingredients']:
		print '--------'
		print single_ingredient['name']
		print str(single_ingredient['quantity']) + ' ' + (single_ingredient['measurement'])
		print single_ingredient['descriptor']
		print single_ingredient['preparation'] + 'prep-description: ' + single_ingredient['prep-description']
	print "Primary Cooking Method: "

load_lists()
displayRecipe(to_Mediterranean(test_rec))



