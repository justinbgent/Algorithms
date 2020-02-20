#!/usr/bin/python

import math

# i will be the 'key' of iterated items
    #recipe[i] # access value of item
    #for i in ingredients:
      #if (i == i):
        #pass

def recipe_batches(recipe, ingredients):
  quantities = [0] * len(recipe)
  counter = 0
  for i in recipe:
    if i in ingredients:
      quantities[counter] = int(ingredients[i] / recipe[i])
    counter += 1
  return min(quantities)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))