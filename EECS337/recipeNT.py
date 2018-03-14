from . import recipegenerator as recipe
from . import SL as sl
url = input("Please input URL(type a space in the end then enter): ")
print("You want to transform recipe url is :"+ url)
url=url.strip()
if(url==""):
    print("You did not enter anything, using the default link...")
    url="https://www.allrecipes.com/recipe/220125/slow-cooker-beef-pot-roast/?clickId=right%20rail0&internalSource=rr_feed_recipe_sb&referringId=237320%20referringContentType%3Drecipe"
myrecipe=recipe.returnRecipe(url)
sl.savingsingle(myrecipe)
