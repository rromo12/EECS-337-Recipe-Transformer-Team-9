
from bs4 import BeautifulSoup
import requests
import sys
import nltk




#For Testing
# http://allrecipes.com/recipe/16066


def parser(url):
	"""Take url and parse into db"""

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
		#split text into unigrams


		# use regexp to splut into name,quantity, measurement,descriptor,preparation(if any), prep-description(optional/if any)
		# quantity  = regexp "-?[0-9]+[/.]?([0-9]+)?" or A(n), dozen, 
		name =""
		quantity=""
		measurement= "" #check vs hardcoded list of units
		
		# Optional
		descriptor = ""
		preparation = ""
		prep-description = ""

		ingredient = {
		"name": name,
		"quantity": quantity,
		"measurement": measurement,
		"descriptor": descriptor,
		"preparation": preparation,
		"prep-description": prep-description
		}
		ingredients.append(ingredient)
	# for ingredient in ingredients:
	# 	print ingredient

	# Steps class "step" -> class "recipe=directions__list--item"
	allsteps = soup.find_all(class_="recipe-directions__list--item")
	for step in allsteps:
		steps.append(step.get_text())

	# print name
	# for ingredient in ingredients:
	# 	print ingredient
	# for step in steps:
	# 	print step
	return {"name": name,
			"ingredients": ingredients,
			"steps":steps}

if __name__ == '__main__':
	# url = raw_input("Enter a URL of the Recipe: ")
	url ="http://allrecipes.com/recipe/16066"

	###AutoGrader Recipes
	# http://allrecipes.com/recipe/easy-meatloaf/
	# http://allrecipes.com/recipe/8714/baked-lemon-chicken-with-mushroom-sauce/
	# http://allrecipes.com/recipe/80827/easy-garlic-broiled-chicken/
	# http://allrecipes.com/recipe/213742/meatball-nirvana/
	print parser(url)

	