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
def islistInclude(targetlist,name):
    flag=0
    for i in targetlist:
        if(name.find(i)!=-1):
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
general_dairy=["milk","butter","cheese","margarine","cream","yogurt","curd"]
general_dairy_vegan=["coconut milk","coconut butter","coconut cheese","coconut margarine","coconut cream","coconut yogurt","coconut curd"]
special_list_mapping_from=["egg","oil"]
vege_dairy=["soy","coconut","rice","almond","water chestnut","wheat"]
vege_oil=["vegetable","sesame","olive","coconut","peanut","sunflower","soy","cotton","rape","chili"]
url="https://www.allrecipes.com/recipe/165190/spicy-vegan-potato-curry/?internalSource=staff%20pick&referringId=1227&referringContentType=recipe%20hub"
myrecipe=recipe.returnRecipe(url)
print("-----------previous recipe")
print(myrecipe)
oldrecipe=copy.deepcopy(myrecipe)
ingred=myrecipe['ingredients']
#direct=myrecipe['step']

flag=0
###########################if has meat, it is not vegan, return
for i in range(len(ingred)):
    tempname=ingred[i]['name']
    if(tempname.find("egg")!=-1):
        flag=1
        break
    if(tempname.find("oil")!=-1 and not islistInclude(vege_oil,tempname)):
        flag=1
        break
    if(flag==1):
        break
    for j in general_meat:
        if(tempname.find(j)!=-1):
            flag=1
            break
    for j in general_dairy:
        if (tempname.find(j) != -1 and islistInclude(vege_dairy,tempname)):
            flag = 1
            break
if(flag==1):
    print("---------after transform")
    print(myrecipe)
else:
    for i in range(len(ingred)):
        if (flag == 1):
            break
        tempname = ingred[i]['name']
        if (tempname.find("oil")!=-1):
            ingred[i]['name'] = "lard"
            ingred[i]['measurement'] = "tablespoon"
            ingred[i]['descriptor'] = "none"
            ingred[i]['preparation'] = "none"
            break


        for j in general_vege:
            if (tempname.find(j) != -1):
                ingred[i]['name'] = "beef"
                ingred[i]['measurement'] = "pound"
                ingred[i]['descriptor'] = "none"
                ingred[i]['preparation'] = "none"
                flag = 1
                break
        if(flag!=1):
            for j in range(len(general_dairy)):
                if (tempname.find(general_dairy[j]) != -1):
                    ingred[i]['name'] = "animal "+general_dairy[j]
                    ingred[i]['measurement'] = "cup"
                    ingred[i]['descriptor'] = "none"
                    ingred[i]['preparation'] = "none"
                    flag = 1
                    break
        if(flag!=1):
            newitem={'name': 'egg', 'quantity': 1, 'measurement': 'none', 'descriptor': 'none', 'preparation': 'none'}
            ingred.append(newitem)
            break





    myrecipe['ingredients']=ingred
    myrecipe["title"]+="(to devegan)"
    print("---------after transform")
    print(myrecipe)

sl.file_name+="(to devegan style)"
sl.saving(oldrecipe,myrecipe)
