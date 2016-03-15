# EECS 337 Recipe Transformer Team 9 2016
### Matthew Heston, Roshun Patel, Rene Romo
## Required Libraries
Beautiful Soup 4

    pip install beautifulsoup4 
Requests

    pip install requests
Natural Language ToolKit(NLTK)

    http://www.nltk.org/install.html

## Running the Recipe Transformer

    python transformer.py
## Parser 
Parses the recipe at the url into the following structure which we then perform transformations on:
#### Ingredients:
      Name
      Quantity
      Measurement
      Descriptor
      Preparation
      Preparation Descriptors
 #### Steps
     Step Ingredients
     Step Tools
     Step Methods
     Step Times
 #### Primary Cooking Method
 #### Cooking Methods
 #### Cooking Tools

## Current Transformations
* To/From Vegetarian
* To/From Pescatarian
* To/From Low Carb
* To/From Low Fat
* To Mediterranean
* To American

