'''Version 0.1'''
from recipe_parser import *

def autograder(url):
    '''Accepts the URL for a recipe, and returns a dictionary of the
    parsed results in the correct format. See project sheet for
    details on correct format.'''
    # your code here
    results=parser(url)

    return results