
from bs4 import BeautifulSoup
import requests
import nltk
import sys
import re
from fractions import Fraction
from collections import Counter
# Import units list
from units import *
from methods import *
from tools import *


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
		text =  single_ingredient.get_text()
		tokens= nltk.word_tokenize(text)

		#TODO Get Ingredient Name
		ingredientname =""
		#######################
		#Quantity             # #######################
		# TODO maybe handle weird cases such as 2 (8 ounce) cans
		quantity= re.search("(-?([0-9]+)\s?(([./0-9]+)?))",text)
		quantity = quantity.group(0)
		quantity = float(sum(Fraction(s) for s in quantity.split()))

		
		#######################
		#Measurement          #
		#######################
		measurement = None
		for token in tokens:
			if(token.lower() in unitslist):
				measurement= token.lower() #check vs hardcoded list of units
		#go from abbreviations to full name
		measurement = abbrToFull(measurement);
		
		#TODO Optional Parsings make list for each
		descriptor = ""
		preparation = ""
		prep_description = ""

		ingredient = {
		# "name": ingredientname,
		"name": text,
		"quantity": quantity,
		"measurement": measurement,
		"descriptor": descriptor,
		"preparation": preparation,
		"prep-description": prep_description
		}
		ingredients.append(ingredient)

	# for ingredient in ingredients:
	#  	print ingredient

	# Steps class "step" -> class "recipe=directions__list--item"
	primaryCookingMethod =[]
	cookingMethods = []
	cookingTools = []
	allsteps = soup.find_all(class_="recipe-directions__list--item")
	for step in allsteps:
		step_ingredients = []
		step_tools =[]
		step_methods = []
		step_times = []
		step_text = step.get_text()
		step_tokens = nltk.word_tokenize(step_text)
		
		# TODO Parse ingredients from step into list
		step_ingredients = [""]
		
		
		for token in step_tokens:
			# Get Tools
			if (token.lower() in toolslist):
				step_tools.append(token.lower())
			# Get Methods and Primary Methods	
			if(token.lower() in methodslist):
				step_methods.append(token.lower())
			if(token.lower() in primary_methods):
				primaryCookingMethod.append(token.lower())

		#If a method is asspcoated with a tool add this tool to the tool list
		for method in step_methods:
			if(method2tool(method)!= None):
				step_tools.append(method2tool(method).lower())

		#add this steps methods to list of methods for recipe
		cookingMethods.extend(step_methods)
		#add this steps tools to list of tools for recipe
		cookingTools.extend(step_tools)
		# TODO Parse Times 
		step_times = [""]


		stepdict = {
			"text": step_text,
			#Optional
			"ingredients": step_ingredients,
			"tools": step_tools,
			"methods":step_methods,
			"times": step_times
		}
		print stepdict
		steps.append(stepdict)

	# TODO Cooking Methods (Primary and additional)
	#primary will be the most commonly referenced primary method
	primaryCookingMethod = Counter(primaryCookingMethod).most_common(1)[0][0]
	print primaryCookingMethod
	#clear out any duplicate methods
	cookingMethods = list(set(cookingMethods))
	#Clear out any duplicate tools
	cookingTools = list(set(cookingTools))
	print cookingTools
	print cookingMethods
	return {"name": name,
			"ingredients": ingredients,
			"primary cooking method": primaryCookingMethod,
			"cooking methods": cookingMethods,
			"cooking tools": cookingTools,
			"steps":steps
			}

if __name__ == '__main__':
	# url = raw_input("Enter a URL of the Recipe: ")
	# url ="http://allrecipes.com/recipe/16066"

	###AutoGrader Recipes
	# url  = "http://allrecipes.com/recipe/easy-meatloaf/"
	url = "http://allrecipes.com/recipe/8714/baked-lemon-chicken-with-mushroom-sauce/"
	# http://allrecipes.com/recipe/80827/easy-garlic-broiled-chicken/
	# http://allrecipes.com/recipe/213742/meatball-nirvana/
	parser(url)

# #Sample Recipe Representation 
# { "name": "Recipe Name",
#   "ingredients": [  
#   		{
#   		"name": ingredient1,
# 		"quantity": quantity,
# 		"measurement": measurement,
# 		"descriptor": descriptor,
# 		"preparation": preparation,
# 		"prep-description": prep_description
# 		},
# 		{
# 		"name": ingredient2,
# 		"quantity": quantity,
# 		"measurement": measurement,
# 		"descriptor": descriptor,
# 		"preparation": preparation,
# 		"prep-description": prep_description
# 		}],
# 	"primary cooking method": "Recipe Primary Cooking Method",
# 	"cooking methods": ["method1","method2","method3"],
# 	"cooking tools": ["tool1","tool2","tool3"],
# 	"steps": [
# 		{
# 			"text": step1_text,
# 			#Optional
# 			"ingredients": ["ingredient1"],
# 			"tools": ["tool1","tool2","tool3"],
# 			"methods"["method1","method2","method3"],
# 			"times": step_times
# 		},
# 		{
# 			"text": step2_text,
# 			#Optional
# 			"ingredients": ["ingredient2"],
# 			"tools": ["tool1","tool2","tool3"],
# 			"methods":["method1","method2","method3"],
# 			"times": step_times
# 		}]
# }