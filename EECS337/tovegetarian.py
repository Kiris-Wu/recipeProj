import EECS337.recipegenerator as recipe
import EECS337.SL as sl
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
    "cod","flounder","haddock","halibut","mahi","salmon","snapper","tilapia","trout",
    "tuna","walleye","clam","crab","lobster","mussel","octopus","squid","oyster","scallop","shrimp",
    "meat","poultry","beef","rib","hamburger","chicken","hen","duck","goose","rabbit","veal","venison",
    "lamb","pork","bacon","sausage","bratwurst","chorizo","kielbasa","turkey"
]
vege_ingre_mapping_to=[
    "tempeh", "tofu", "seitan", "gardein", "eggplant", "mushroom", "bean", "bok choy", "broccoli", "brussel sprout",
    "lettuce", "spinach", "onion", "carrot", "corn",
    "cucumber", "potato", "tomato", "cabbage", "cauliflower", "celery root", "chile pepper", "artichoke", "ratatouille",
    "asparagus", "beet"]

url="https://www.allrecipes.com/recipe/242405/orange-and-milk-braised-pork-carnitas/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%209"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
print(myrecipe)
oldrecipe=copy.deepcopy(myrecipe)
ingred=myrecipe['ingredients']
#direct=myrecipe['step']
namelist=[]
for i in range(len(ingred)):
    namelist.append(ingred[i]['name'])
for i in range(len(ingred)):
    tempname=ingred[i]['name']
    flag=0
    for j in general_meat:
        if(flag==1):
            break
        if(tempname.find(j)!=-1):
            for k in vege_ingre_mapping_to:
                if(not isInclude(namelist,k)):
                    ingred[i]['name']=k
                    ingred[i]['measurement']="ounce"
                    ingred[i]['descriptor']="none"
                    ingred[i]['preparation']="none"
                    namelist[i]=k
                    flag=1
                    break
myrecipe['ingredients']=ingred
myrecipe["title"]+="(to vegetarian)"
print("---------after transform")
print(myrecipe)

sl.file_name+="(to vegetarian style)"
sl.saving(oldrecipe,myrecipe)

