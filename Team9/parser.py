
from bs4 import BeautifulSoup
import requests
import sys




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
	for ingredient in all_ingredients:
		ingredients.append(ingredient.get_text())
	# for ingredient in ingredients:
	# 	print ingredient

	# Steps class "step" -> class "recipe=directions__list--item"
	allsteps = soup.find_all(class_="recipe-directions__list--item")
	for step in allsteps:
		steps.append(step.get_text())

	print name
	for ingredient in ingredients:
		print ingredient
	for step in steps:
		print step
	return name,ingredients,steps

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	# url = raw_input("Enter a URL of the Recipe: ")
	url ="http://allrecipes.com/recipe/16066"
	parser(url)

	