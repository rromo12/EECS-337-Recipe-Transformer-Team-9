unitslist = ["tsp",
         "tbsp",
         "Tbl",
         "fl oz",
         "c.",
         "pt",
         "qt",
         "gal",
         "g",
         "oz",
         "lb",
         "l",
         #plural abbreviations
         "tsps",
         "tbsps",
         "Tbl",
         "fl oz",
         "pts",
         "qts",
         "gal",
         "g",
         "oz",
         "lbs",
         "teaspoon",
         "teaspoons",
         "tablespoon",
         "tablespoons",
         "fluid ounce",
         "fluid ounces",
         "cup",
         "cups",
         "pint",
         "pints",
         "quart",
         "quarts",
         "gallon",
         "gallons",
         "gram",
         "grams",
         "ounce",
         "ounces",
         "pound",
         "pounds",
         "liters",
         #odd cases
         "needed",
         "taste",
         "pinch",
         "dash",
         "pkg.",
         "package",
         "can",
         "cans"
]

abbreviations = {
         "tsp":  "teaspoon",
         "tbsp": "tablespoon",
         "tbl":  "tablespoon",
         "fl oz": "fluid ounce",
         "c.": "cup",
         "pt": "pint",
         "qt": "quart",
         "gal": "gallon",
         "g": "gram",
         "oz": "ounce",
         "lb": "pound",
         "l": "liter",
         #plural abbreviations
         "tsps": "teaspoons",
         "tbsps": "tablespoons",
         "tbls": "tablespoons",
         "pts": "pints",
         "qts": "quarts",
         "gals": "gallons",
         "lbs": "pounds",
         # Odd cases
         "taste" : "to taste",
         "needed": "as needed"
}

def abbrToFull(token):
   if token in abbreviations:
      return abbreviations[token]
   else:
      return token