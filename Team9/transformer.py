from bs4 import BeautifulSoup
import requests
import sys
import nltk

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

#print test_rec

def remove_meat(recipe):
	for single_ingredient in recipe['ingredients']:
		print single_ingredient['name']

load_lists()
remove_meat(test_rec)



