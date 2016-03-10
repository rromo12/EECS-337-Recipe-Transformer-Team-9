from bs4 import BeautifulSoup
import requests
import sys
import nltk

#given a recipe dictionary of lists of dictionaries / lists -> transform to new object of same format

# #Sample Recipe Representation 
{ "name": "Testing Recipe",
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

