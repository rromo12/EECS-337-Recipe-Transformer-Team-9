
from bs4 import BeautifulSoup
import requests
import nltk
import sys
import re
from fractions import Fraction
from collections import Counter
from decimal import *
# Import units list
from units import unitslist, abbreviations, abbrToFull
from methods import methodslist, primary_methods
from tools import methodToTools, toolslist, method2tool
from optionallists import descriptorlist, preparationlist, prep_descriptionlist
from nltk.stem.lancaster import LancasterStemmer

def parser(url):
	"""Take url and parse into proper format"""
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	ingredients =[]
	recipe_ingredients=[]
	steps = []
	primaryCookingMethod =[]
	cookingMethods = []
	cookingTools = []
	# recipe name class = recipe-summary__h1
	name = soup.find_all(class_="recipe-summary__h1")
	name = name[0].get_text()
	stoplist = [",","!","?","(",")","of","or","more","less", "as","needed","to","such", "Frank", "'s","taste"]
	
	# Ingredients under class recipe-ingred_txt added
	all_ingredients = soup.find_all(class_ = "recipe-ingred_txt", itemprop="ingredients")
	st = LancasterStemmer()
	for single_ingredient in all_ingredients:
		ingredientname =""
		quantity = 0;
		measurement = None
		descriptors = []
		preparations =[]
		prep_descriptions = []
		bigram_tokens =[]
		used_tokens = []
		used_bigrams =[]
		text =  single_ingredient.get_text().encode('ascii','backslashreplace')
		tokens= nltk.word_tokenize(text)
		

		#######################
		#Quantity             # 
		#######################
		quantity= re.search("(-?([0-9]+)\s?(([./0-9]+)?))",text)
		if(quantity != None):
			quantity = quantity.group(0).strip()
			if (" " in quantity):
				 quantitytoken = quantity.split(" ")
				 used_tokens.extend(quantitytoken)
			else:
				quantitytoken = quantity
				used_tokens.append(quantitytoken)
			quantity = float(sum(Fraction(s) for s in quantity.split()))
			if("/" in quantitytoken):
				quantity= round(quantity,2)
			else:
				quantity = Decimal(quantity)
			
		else:
			quantity = 1


			
		
		#################################################################
		#Measurement,  Descriptors,Preparations and Prep descriptors    #
		#################################################################
		for token in tokens:
			if(token.lower() in unitslist and measurement == None):
				measurement= token.lower() #check vs hardcoded list of units
				used_tokens.append(token)
			if(token.lower() in descriptorlist):
				#TODO Optional Parsings make list for each
				descriptors.append(token.lower())
				used_tokens.append(token)
			if(token.lower() in preparationlist):
				preparations.append(token.lower())
				used_tokens.append(token)
			if(token.lower() in prep_descriptionlist):
				prep_descriptions.append(token.lower())
				used_tokens.append(token)



		#go from abbreviations to full name
		measurement = abbrToFull(measurement);
		
		#######################
		#Name                 #
		#######################
		# Whatever was not identified as  something and is not punctuation or stoplist words
		for token in used_tokens:
			if(token in tokens):
				tokens.remove(token)
		for token in stoplist:
			if(token in tokens):
				tokens.remove(token)
		name = " ".join(tokens).strip()
		if measurement == None:
			measurement ="units"

		if len(descriptors) !=0:
			descriptors = descriptors[0]
		if len(preparations) !=0:
			preparations = preparations[0]
			# Add any tools required for preparation
			if(method2tool(preparations)!= None):
				cookingTools.append(method2tool(preparations).lower())
		if len(prep_descriptions) !=0:
			prep_descriptions = prep_descriptions[0]

		#create list of ingredients for use when finding ingredients in steps
		recipe_ingredients.append(tokens[0])
		ingredient = {
		# "name": ingredientname,
		"name": name,
		"quantity": quantity,
		"measurement": measurement,
		"descriptor": descriptors,
		"preparation": preparations,
		"prep-description": prep_descriptions
		}
		ingredients.append(ingredient)

	recipe_ingreidients = list(set(recipe_ingredients))
	# Steps class "step" -> class "recipe=directions__list--item"

	allsteps = soup.find_all(class_="recipe-directions__list--item")
	for step in allsteps:
		step_ingredients = []
		step_tools =[]
		step_methods = []
		step_time = ""
		step_text = step.get_text()
		if(step_text ==""):
			continue
		step_tokens = nltk.word_tokenize(step_text)
		step_bigrams = nltk.bigrams(step_tokens)
		step_bigram_tokens = []
		for gram in step_bigrams:
			step_bigram_tokens.append(" ".join(gram))
			
		# Grams
		for token in step_tokens:
			# Get Tools
			if (token.lower() in toolslist):
				step_tools.append(token.lower())
			# Get Methods and Primary Methods	
			if(token.lower() in methodslist):
				step_methods.append(token.lower())
			elif(st.stem(token.lower()) in methodslist):
				step_methods.append(token.lower())
			if(token.lower() in primary_methods):
				primaryCookingMethod.append(token.lower())
			# TODO Parse ingredients from step into list (not the best method currently)
			if(token.lower() in recipe_ingredients):
				# Check all ingredients
				for ingredient in ingredients:
					# if first word matches then add this to step ingredients
					if(token.lower() == ingredient["name"].split()[0]):
						step_ingredients.append(ingredient["name"])
					else:
						 step_ingredients.append(token.lower())


		# Bigrams
		for token in step_bigram_tokens:
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
		step_methods = list(set(step_methods))
		cookingMethods.extend(step_methods)
		#add this steps tools to list of tools for recipe
		step_tools = list(set(step_tools))
		step_ingredients = list(set(step_ingredients))
		cookingTools.extend(step_tools)
		
		#Parse Times 
		# regexp for times ((([0-9]+)\s?(([.\-/0-9to ]+)?))\s(min(?:(?:utes?)?|.?)?|sec(?:(?:onds?)?|.?)?|h(?:(?:ours?|rs?.?)?)))
		# test cases 
		# 20, 20-30, 20 to 30 20.5 1/2
		#minutes/seconds/hours/min./min/sec./sec/hr/hrs
		# add a list of words to check for e.g. overnight
		# 
		# Maybe switch to find all to cover case of multiple times in one step
		times=re.search("((([0-9]+)\s?(([.\-/0-9to ]+)?))\s(min(?:(?:utes?)?|.?)?|sec(?:(?:onds?)?|.?)?|h(?:(?:ours?|rs?.?)?)))",step_text)
		if (times != None):
			step_time = times.group(0).strip()
		elif("overnight" in step_tokens):
			step_time = "overnight"
		else:
			step_time = ""
		stepdict = {
			"text": step_text,
			#Optional
			"ingredients": step_ingredients,
			"tools": step_tools,
			"methods":step_methods,
			"times": step_time
		}
		steps.append(stepdict)

	#Cooking Methods (Primary and additional)
	#primary will be the most commonly referenced primary method
	primaryCookingMethod = Counter(primaryCookingMethod).most_common(1)[0][0]
	#clear out any duplicate methods
	cookingMethods = list(set(cookingMethods))
	#Clear out any duplicate tools
	cookingTools = list(set(cookingTools))
	print cookingTools
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
	
	url = "http://allrecipes.com/recipe/80827/easy-garlic-broiled-chicken/"
	url  = "http://allrecipes.com/recipe/easy-meatloaf/"
	url = "http://allrecipes.com/recipe/8714/baked-lemon-chicken-with-mushroom-sauce/"
	url = "http://allrecipes.com/recipe/213742/meatball-nirvana/"
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