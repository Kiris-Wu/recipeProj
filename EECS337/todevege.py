import recipeProj.EECS337.recipegenerator as recipe
import recipeProj.EECS337.SL as sl
import copy
def isInclude(namelist,target):
    flag=0
    for i in namelist:
        if(i.find(target)!=-1):
            flag=1
    if(flag==1):
        return True
    else:
        return False
general_meat=[
    "beef","cod fish","flounder","haddock","halibut","mahi","salmon","snapper","tilapia","trout",
    "tuna","walleye","clam","crab","lobster","mussel","octopus","squid","oyster","scallop","shrimp",
    "poultry","rib","hamburger","chicken","hen","duck","goose","rabbit","veal","venison",
    "lamb","pork","bacon","sausage","bratwurst","chorizo","kielbasa","turkey"
]
general_vege=[
    "bean","pea","lentil","apple","apricot","avocado","banana","berries","cherries","citrus","grapefruit",
    "lemon","lime","orange","coconut","date","fig","grape","kiwi","mango","melon","nectarine",
    "papaya","peach","pear","persimmon","pineapple","plum","pomegranate","raisin","mushroom",
    "artichoke","ratatouille","asparagus","beet","bell pepper","bok choy","broccoli","brussel sprout",
    "cabbage","carrot","cauliflower","celery root","chile pepper","corn","cucumber","eggplant","fennel",
    "garlic","green","arugula","chard","kale","lettuce","spinach","jicama","leek","nopales","okra",
    "olive","onion","parsnip","potatoe","radish","rhubarb","rhutabaga","shallot","squash","tomatillo",
    "tomato","turnip","water chestnut","yam"
]

url="https://www.allrecipes.com/recipe/34613/roquefort-pear-salad/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%205"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
print(myrecipe)
oldrecipe=copy.deepcopy(myrecipe)
ingred=myrecipe['ingredients']
#direct=myrecipe['step']

flag=0
###########################if has meat, it is not vege, return
for i in range(len(ingred)):
    tempname=ingred[i]['name']
    if(flag==1):
        break
    for j in general_meat:
        if(tempname.find(j)!=-1):
            flag=1
            break
if(flag==1):
    print("---------after transform")
    print(myrecipe)
else:
    for i in range(len(ingred)):
        if(flag==1):
            break
        tempname = ingred[i]['name']
        for j in general_vege:
            if (tempname.find(j) != -1):
                ingred[i]['name'] = "beef"
                ingred[i]['measurement'] = "pound"
                ingred[i]['descriptor'] = "none"
                ingred[i]['preparation'] = "none"
                flag = 1
                break





    myrecipe['ingredients']=ingred
    myrecipe["title"]+="(to devegetarian)"
    print("---------after transform")
    print(myrecipe)

sl.file_name+="(to devegetarian style)"
sl.saving(oldrecipe,myrecipe)

