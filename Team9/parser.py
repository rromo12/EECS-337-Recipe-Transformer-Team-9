
from bs4 import BeautifulSoup
import requests
import sys
import nltk




#For Testing
# http://allrecipes.com/recipe/16066


def parser(url):
	"""Take url and parse into proper format"""
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	ingredients =[]
	steps = []
	# recipe name class = recipe-summary__h1
	name = soup.find_all(class_="recipe-summary__h1")
	name = name[0].get_text()
	

	# Ingredients under class recipe-ingred_txt added
	all_ingredients = soup.find_all(class_ = "recipe-ingred_txt", itemprop="ingredients")
	for single_ingredient in all_ingredients:
		text = single_ingredient.get_text()
		#TODO Get Ingredient Name
		name =""
		# TODO Get Quantity # quantity  = regexp "-?[0-9]+[/.]?([0-9]+)?" or A(n), dozen, 
		quantity=""
		#TODO Get Measurement
		measurement= "" #check vs hardcoded list of units
		
		#TODO Optional Parsing
		descriptor = ""
		preparation = ""
		prep_description = ""

		ingredient = {
		"name": name,
		"quantity": quantity,
		"measurement": measurement,
		"descriptor": descriptor,
		"preparation": preparation,
		"prep-description": prep_description
		}
		ingredients.append(ingredient)
	# for ingredient in ingredients:
	# 	print ingredient

	#TODO Get Tools 
	tools =[""]
	#TODO Get Methods
	primaryMethod = ""
	methods = [""]

	# Steps class "step" -> class "recipe=directions__list--item"
	allsteps = soup.find_all(class_="recipe-directions__list--item")
	for step in allsteps:
		step_text = step.get_text()
		# TODO Parse ingredients from step into list
		step_ingredients = [""]
		# TODO Parse Tools
		step_tools = [""]
		# TODO Parse Methods
		step_methods = [""]
		# TODO Parse Times 
		step_times = [""]


		stepdict = {
			"text": step_text,
			"ingredients": step_ingredients,
			"tools": step_tools,
			"methods":step_methods,
			"times": step_times
		}
		steps.append(stepdict)


	return {"name": name,
			"ingredients": ingredients,
			"primary cooking method": primaryMethod,
			"cooking methods": methods,
			"cooking tools": tools,

			"steps":steps
			}

if __name__ == '__main__':
	# url = raw_input("Enter a URL of the Recipe: ")
	url ="http://allrecipes.com/recipe/16066"

	###AutoGrader Recipes
	# http://allrecipes.com/recipe/easy-meatloaf/
	# http://allrecipes.com/recipe/8714/baked-lemon-chicken-with-mushroom-sauce/
	# http://allrecipes.com/recipe/80827/easy-garlic-broiled-chicken/
	# http://allrecipes.com/recipe/213742/meatball-nirvana/
	print parser(url)

	