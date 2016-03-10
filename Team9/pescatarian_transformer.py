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
poultry = []

def load_lists():
	meat_file = open("meats.txt", "r")
	meat_lines = meat_file.readlines()
	for meat in meat_lines:
		print meat

#print test_rec

def remove_meat(recipe):
	for single_ingredient in recipe['ingredients']:
		print single_ingredient['name']

def remove_fish(recipe):
    fish_list = open("fish.txt").readlines()
    meat_list = open("meats.txt").readlines()
    found_fish = []
    replacement = {}
	for single_ingredient in recipe['ingredients']:
        if single_ingredient["name"] in fish_list:
            meat_replacement = random.choice(meat_list) # TODO: we can be smarter than random
            single_ingredient["name"] = meat_replacement
            found_fish.append(single_ingredient["name"])
            replacement[single_ingredient["name"]] = meat_replacement
    for fish in found_fish:
        for step in recipe["steps"]:
            if fish in step["text"]:
                step["text"] = step["text"].replace(fish, replacement[fish])
    return recipe

load_lists()
remove_meat(test_rec)



